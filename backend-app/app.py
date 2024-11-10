import os
import subprocess
import time
import json
from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)

def init_db():
    conn = sqlite3.connect('terraform_state.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS state (
            id INTEGER PRIMARY KEY,
            state_data TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

init_db()

def save_state(state):
    conn = sqlite3.connect('terraform_state.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM state')
    cursor.execute('INSERT INTO state (state_data) VALUES (?)', (json.dumps(state),))
    conn.commit()
    conn.close()

def load_state():
    conn = sqlite3.connect('terraform_state.db')
    cursor = conn.cursor()
    cursor.execute('SELECT state_data FROM state')
    row = cursor.fetchone()
    conn.close()
    return json.loads(row[0]) if row else {}

def clear_state():
    conn = sqlite3.connect('terraform_state.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM state')
    conn.commit()
    conn.close()

@app.route('/deploy', methods=['POST'])
def deploy():
    data = request.get_json()
    deployment_type = data.get('deploymentType')
    project_id = data.get('project_id')
    #service_account_email = data.get('service_account_email')
    zone = data.get('zone')
    region = data.get('region')

    base_path = './terraform-modules'
    terraform_directory = os.path.join(base_path, deployment_type)

    init_command = 'terraform init'
    apply_command = f'terraform apply -auto-approve -var="project_id={project_id}" ' \
                    f'-var="zone={zone}" -var="region={region}"'

    try:
        # Initialize Terraform
        init_result = subprocess.run(
            init_command,
            cwd=terraform_directory,
            shell=True,
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        # Apply Terraform configuration
        apply_result = subprocess.run(
            apply_command,
            cwd=terraform_directory,
            shell=True,
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        # Save the state to the database
        state = load_state() 
        state['last_apply'] = apply_result.stdout.decode('utf-8')
        save_state(state)

        return jsonify(), 200

    except subprocess.CalledProcessError as e:
        error_message = e.stderr.decode('utf-8') if e.stderr else 'No error message'
        return {
            "error": "Deployment failed.",
            "details": error_message,
            "project_id": project_id,
            "deployment_type": deployment_type
        }, 500

@app.route('/destroy', methods=['POST'])
def destroy():
    data = request.get_json()
    deployment_type = data.get('deploymentType')
    project_id = data.get('project_id')
    #service_account_email = data.get('service_account_email')
    zone = data.get('zone')
    region = data.get('region')

    base_path = './terraform-modules'
    terraform_directory = os.path.join(base_path, deployment_type)

    init_command = 'terraform init'
    destroy_command = f'terraform destroy -auto-approve -var="project_id={project_id}" ' \
                      f'-var="zone={zone}" -var="region={region}"'

    try:
        state = load_state()
        subprocess.run(init_command, cwd=terraform_directory, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        return {"error": "Failed to initialize Terraform.", "details": str(e)}, 500

    max_retries = 3
    for attempt in range(max_retries):
        try:
            subprocess.run(destroy_command, cwd=terraform_directory, shell=True, check=True)
            clear_state()
            return jsonify(), 200
        except subprocess.CalledProcessError as e:
            error_message = e.stderr.decode('utf-8') if e.stderr else 'No error message'
            if "Error acquiring the state lock" in error_message:
                time.sleep(5) 
            else:
                return {
                    "error": "Destruction failed.",
                    "details": error_message,
                    "project_id": project_id,
                    "deployment_type": deployment_type
                }, 500

    clear_state()
    return {"error": "Max retries reached. Terraform destroy failed due to state lock."}, 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
