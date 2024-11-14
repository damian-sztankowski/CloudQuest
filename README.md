<p align="center">
<img src="images/craft-logo2.svg" alt="description" width="300" height="300" align="center"><p>

# Cloud Quest: Real-World Engineer Simulator

Welcome to **Cloud Quest**, the interactive cloud engineering simulator designed to help you learn real-world cloud architecture skills through hands-on challenges. Whether you're deploying infrastructure with Terraform, setting up CI/CD pipelines, or managing IAM roles, Cloud Quest offers a range of challenges to enhance your cloud knowledge and proficiency.

## Table of Contents

- [Cloud Quest: Real-World Engineer Simulator](#Cloud Quest-real-world-engineer-simulator)
  - [Table of Contents](#table-of-contents)
  - [Features](#features)
  - [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
  - [Running the Project](#running-the-project)
  - [Adding New Challenges](#adding-new-challenges)
  - [Contribution Guidelines](#contribution-guidelines)
  - [License](#license)

---

## Features

- 🛠 **Real-World Challenges**: Complete challenges such as deploying web applications, managing IAM roles, or implementing CI/CD pipelines.
- 🚀 **Deploy Cloud Infrastructure**: Use Terraform to deploy infrastructure on Google Cloud with real inputs like projectID, folderID, or organizationID.
- 🖥 **Interactive Learning**: Hands-on experience with infrastructure as code (IaC) tools, cloud services, and DevOps workflows.
- 🔍 **Search and Filter**: Easily search for and filter challenges by technology (Terraform, Docker, Google Cloud, etc.).
- 📊 **Dynamic Feedback**: Get real-time feedback on deployments with visual output for success or failure.

---

## Getting Started

### Prerequisites

To run Cloud Quest locally, ensure you have the following tools installed:

- [Node.js](https://nodejs.org/en/download/)
- [npm](https://www.npmjs.com/get-npm) or [Yarn](https://yarnpkg.com/getting-started/install)
- [Python 3.x](https://www.python.org/downloads/) (for backend services)
- [Terraform](https://www.terraform.io/downloads.html)

### Local Installation

1. **Clone the repository**:

   ```bash
    git clone https://github.com/damian-sztankowski/Cloud Quest.git
    cd Cloud Quest
    ```
2. Install frontend dependencies:

    ```bash
        cd frontend-app
        npm install
    ```
3. Install backend dependencies:
    ```bash
        cd ../backend-app
        pip install -r requirements.txt
    ```
---


## Project Structure

The Cloud Quest project is structured into several main directories:
    
```bash
    Cloud Quest/
    │
    ├── frontend-app/             # Vue.js frontend code
    │   ├── src/
    │   ├── public/
    │   └── ...
    │
    ├── backend-app/              # Python Flask backend code
    │   ├── app.py                # Main server logic for handling API requests
    │   └── ...
    │
    ├── terraform-modules/        # Terraform modules used for cloud deployments
    │   └── ...
    │
    ├── README.md                 # Project README (this file)
    ├── CONTRIBUTING.md           # Contribution guidelines for the project
    └── LICENSE                   # License file (MIT)
```

---

## Running the Project

1. Running the Frontend
To start the Vue.js frontend application, use the following command from the frontend-app directory:

    ```bash
        npm run serve
    ```
This will start the frontend on ***localhost:8080***.

2.  Running the Backend
To start the Python backend server for handling deployments and communication with Terraform, use the following command from the backend-app directory:

    ```bash
        python app.py
    ```
This will start the backend on ***localhost:5000***.

---

## Adding New Challenges
To add new challenges to the CloudTinker platform, follow these steps:

1. Add new assets (if applicable):

   * Place any new icons or assets for your challenge in the /src/assets/ folder.
2. Add the challenge to the data file:

    * Update the challenge list in frontend-app/src/components/DeploymentForm.vue by adding a new entry with your challenge details (title, description, technologies). Remember to change ID number!
    ```javascript
        {
            id: 4,
            title: 'Deploy a Kubernetes Cluster',
            description: 'Deploy a Kubernetes cluster on Google Cloud using Terraform.',
            technologies: [
                require('@/assets/kubernetes-svgrepo-com.svg'),
                require('@/assets/terraform-svgrepo-com.svg')
            ],
        requiredInput: 'projectID'
        }
    ```


3. Test the new challenge:

    * After making the necessary changes, test the challenge by interacting with the frontend and backend services.
---
### Backend API Endpoints
The backend service exposes several endpoints to handle the deployment and destruction of infrastructure using Terraform. Below are some common API routes:

* Deploy Challenge: ***POST /deploy/<challenge-name>***

    * This endpoint triggers a Terraform deployment.
    * Request body should include required fields like projectID, folderID, or orgID.
    ```json

        {
            "projectID": "your-project-id"
        }
    ```

* Destroy Challenge: ***POST /destroy/<challenge-name>***

    * This endpoint triggers a Terraform destroy operation to clean up resources.

## Contribution Guidelines
We encourage contributions to improve the project. Please refer to the [Contribution Guidelines](/CONTRIBUTION.md) for information on how to contribute, report bugs, request features, or add new challenges.

## License
This project is licensed under the MIT License.
