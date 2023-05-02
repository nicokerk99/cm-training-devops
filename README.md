# DevOps

## Docker Exercise

Goal: build a container and run it locally

Requirements:
 - Add a “Dockerfile” to your repo
 - Make it so “docker build .” will build your container, including your application
 - To test if it works => “docker run your-container” and check your browser

Tips:
- https://docs.docker.com/get-started/02_our_app/#build-the-apps-container-image
- For your web server to be accessible, don’t forget to expose the port!

## CICD Exercises

Create CICD pipeline for a python application.
3 exercises:
1. Exercise 1: Simple github actions pipeline
2. Exercise 2: Continuous Integration
3. Exercise 3: Continuous Delivery

Starting point from SWE exercise

### Exercise 1: Simple github actions pipeline

Goal: play around with a github actions pipeline

Requirements:
- Create a github pipeline
- Print “hello world” in your pipeline

Tip: https://docs.github.com/en/actions/quickstart

### Exercise 2: Continuous Integration

Goal: assert quality of code

Requirements:
- CI pipeline
- Pipeline runs on every push to the repo
- Only add code to main via PR merge (via Branch policies settings)
- Block PR if CI pipeline fails (via Branch policies settings)
- Bonus: try to show test coverage in the UI

Tip: https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches#require-status-checks-before-merging

### Exercise 3: Continuous Delivery

Goal: release python package

Requirements:
- CD pipeline
  - Container build
    - Build the container
    - Tag the image with the datetime
    - Push it to the github container registry
- Pipeline only runs when push to main
- Pull your created container locally and run it

Tip: https://dev.to/willvelida/pushing-container-images-to-github-container-registry-with-github-actions-1m6b

## Use full commands for you exercises

### Docker

Following commands are examples, adjust them to your needs.

```bash
# Build the container
docker build -t <image_name> .

# Run the container with port forwarding
docker run -p 5000:5000 <image_name>

# Push the container to github container registry
docker tag <image_name> ghcr.io/<github_username>/<image_name>:<tag>
docker push ghcr.io/<github_username>/<image_name>:<tag>

# Pull the container from github container registry
docker pull ghcr.io/<github_username>/<image_name>:<tag>
```

### Pre-commit

```bash
pre-commit install
pre-commit run --all-files
```

### Poetry

```bash
# Install poetry
pip install poetry

# Install dependencies
poetry install
```

### Pytest

```bash
# Run tests with coverage
pytest --cov=./ --cov-report=xml
```
