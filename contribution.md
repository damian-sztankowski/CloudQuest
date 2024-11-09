# Contribution Guidelines

Thank you for your interest in contributing to **CloudCraft: Real-World Engineer Simulator**! We welcome contributions from everyone. These guidelines will help you understand how to participate in the project, the steps to contribute effectively, and the standards for submitting changes. Please read through the guidelines carefully before making any contributions.

## Table of Contents

- [Contribution Guidelines](#contribution-guidelines)
  - [Table of Contents](#table-of-contents)
  - [Code of Conduct](#code-of-conduct)
  - [How Can I Contribute?](#how-can-i-contribute)
    - [Reporting Bugs](#reporting-bugs)
    - [Suggesting Enhancements](#suggesting-enhancements)
    - [Adding a New Challenge](#adding-a-new-challenge)
      - [Step 1: Fork the repository](#step-1-fork-the-repository)
      - [Step 2: Create a new challenge](#step-2-create-a-new-challenge)
      - [Step 3: Implement challenge logic](#step-3-implement-challenge-logic)
      - [Step 4: Test the new challenge](#step-4-test-the-new-challenge)
      - [Step 5: Commit changes and create a pull request](#step-5-commit-changes-and-create-a-pull-request)
  - [Development Setup](#development-setup)
  - [Submitting Contributions](#submitting-contributions)
    - [Pull Request Process](#pull-request-process)
  - [Coding Standards](#coding-standards)
  - [License](#license)

---

## Code of Conduct

We have adopted the [Contributor Covenant Code of Conduct](https://www.contributor-covenant.org/version/2/0/code_of_conduct/) to foster an open, welcoming, and inclusive community. Please adhere to this code when interacting with the community and contributing to the project.

## How Can I Contribute?

### Reporting Bugs

If you find a bug in the project, please submit a detailed issue report. Follow these steps:

1. **Check for duplicates**: Search the [issue tracker](https://github.com/your-username/your-repo/issues) to ensure the issue has not already been reported.
2. **Create a new issue**: If it hasn’t been reported, open a [new issue](https://github.com/your-username/your-repo/issues/new) and fill out the provided template with details including:
   - Description of the bug
   - Steps to reproduce the issue
   - Any relevant logs or screenshots

### Suggesting Enhancements

Enhancements to the project are always welcome! Please follow these steps to suggest a new feature or improvement:

1. **Check for similar suggestions**: Review the existing [feature requests](https://github.com/your-username/your-repo/issues?q=is%3Aissue+is%3Aopen+label%3Aenhancement).
2. **Create a new suggestion**: If your suggestion hasn’t been made, open a new issue and describe your enhancement, including:
   - Motivation for the feature
   - Potential use cases
   - Any possible drawbacks

### Adding a New Challenge

You can contribute by adding new challenges to the CloudCraft platform. Follow these steps to add a new challenge:

#### Step 1: Fork the repository

1. Fork the repository by clicking the **Fork** button on the project’s GitHub page.
2. Clone the forked repository to your local machine:

```bash
   git clone https://github.com/your-username/your-forked-repo.git
   cd your-forked-repo
```

#### Step 2: Create a new challenge

Each challenge must follow a consistent structure to ensure it works correctly with the platform. Here’s how to add a new challenge:

1. Add challenge assets:
 
- Go to the ***/src/assets*** directory and add any necessary images (icons for technologies like Terraform, Docker, etc.) required for your challenge.
  
2. Update challenges data:

In ***/src/components/ChallengeData.vue*** add a new entry to the challenges array. 

Example format:

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
This ensures your challenge appears in the challenges list.

#### Step 3: Implement challenge logic


- If needed, create backend logic or a shell script for the challenge (e.g., to run a Terraform deployment) in the /***backend-app*** directory.

- Adjust the frontend to handle any specific deployment or destroy actions by adding methods in the component ***/src/components/ChallengeActions.vue*** or a similar file handling deployment logic.

#### Step 4: Test the new challenge

Run the application locally to test your new challenge and ensure that the deployment process works correctly:

```bash
npm run serve
```
#### Step 5: Commit changes and create a pull request

1. Add and commit your changes:

```bash
git add .
git commit -m "Added new challenge: Deploy Kubernetes Cluster"
```
2. Push your changes to your forked repository:

```bash
git push origin your-branch-name
```

3. Open a Pull Request from your forked repository to the main repository. Make sure to provide a descriptive title and explain the purpose of your changes.

## Development Setup

To contribute to the project, you need to set up your development environment. Here’s how to get started:

1. Install dependencies: Make sure you have Node.js, npm, and any other project dependencies installed:

```bash
Copy code
npm install
```


This will start the project on localhost:8080 in development mode.

2. Linting: Ensure your code meets the project's linting standards:

```bash
npm run lint
```
3. Install backend dependencies: Install the required Python libraries for the backend:

```bash
pip install -r requirements.txt
```

4. Run the project locally:

```bash
npm run serve
python app.py
```


## Submitting Contributions
### Pull Request Process
To submit your contributions, follow this pull request process:

1. Fork the repo: Fork the repository and clone your fork.
2. Create a new branch: Create a new branch for your feature or bug fix.
3. Make your changes: Implement your feature, bug fix, or new challenge.
4. Commit and push: Commit your changes to your forked repository.
5. Open a Pull Request: Open a pull request on the original repository, following these guidelines:
6. Explain what changes you made and why.
7. Provide screenshots if you are adding a frontend feature.
8. Link any relevant issues.

## Coding Standards

* ***Code Formatting:*** Follow the ESLint rules for JavaScript and Vue.js code. We use Prettier for consistent formatting.

* ***Commit Messages:*** Use clear and concise commit messages. Follow Conventional Commits for commit messages where possible:

  * ```feat```: A new feature
  * ```fix```:  A bug fix
  * ```docs```: Documentation only changes
  * ```style```: Code style changes (e.g., formatting)
  * ```refactor```: Code changes that neither fix bugs nor add features
  * ```test```: Adding or updating tests
  * ```chore```: Maintenance tasks

* ***Testing:*** Write tests for new features and bug fixes. Use unit tests for functionality and integration tests if applicable.

## License
By contributing, you agree that your contributions will be licensed under the MIT License.

----

Thank you for contributing! We’re excited to have you on board and appreciate your effort to make CloudCraft better for the community.
