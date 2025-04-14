# Docker & Kubernetes Learning Projects

This repository contains a collection of beginner-friendly projects designed to learn and demonstrate core concepts of Docker and Kubernetes. Each project builds upon the previous one, introducing new concepts progressively.

**Date:** April 14, 2025
**Location:** Bengaluru, India

## Table of Contents

* [Prerequisites](#prerequisites)
* [Repository Structure](#repository-structure)
* [Project 1: Static Website Hosting](#project-1-static-website-hosting)
    * [Description](#description-1)
    * [Technologies](#technologies-1)
    * [Running with Docker](#running-with-docker-1)
    * [Deploying to Kubernetes](#deploying-to-kubernetes-1)
* [Project 2: Basic Web Application](#project-2-basic-web-application)
    * [Description](#description-2)
    * [Technologies](#technologies-2)
    * [Running with Docker](#running-with-docker-2)
    * [Deploying to Kubernetes](#deploying-to-kubernetes-2)
* [Project 3: Multi-Container Web App + Database](#project-3-multi-container-web-app--database)
    * [Description](#description-3)
    * [Technologies](#technologies-3)
    * [Running with Docker Compose](#running-with-docker-compose-3)
    * [Deploying to Kubernetes](#deploying-to-kubernetes-3)
* [Learning & Contribution](#learning--contribution)

## Prerequisites

Before you begin, ensure you have the following tools installed and configured:

* **Git:** For cloning the repository.
* **Docker Desktop:** Includes Docker Engine, Docker CLI, and optionally Kubernetes (enable it in settings). Or, separate Docker Engine + CLI and a local K8s cluster like Minikube, Kind, or k3s.
* **kubectl:** The Kubernetes command-line tool.
* * **Node.js & npm** (if using Node.js)
* **Python & pip** (if using Python)

## Repository Structure

```
├── project-1-static-site/
│   ├── index.html
│   ├── Dockerfile
│   ├── deployment.yaml
│   └── service.yaml
├── project-2-basic-app/
│   ├── app.py          # Or server.js, etc.
│   ├── requirements.txt # Or package.json, etc.
│   ├── Dockerfile
│   ├── deployment.yaml
│   └── service.yaml
├── project-3-multi-container/
│   ├── web-app/          # Directory for your web app code
│   │   ├── app.py        # Or server.js, etc.
│   │   ├── requirements.txt # Or package.json, etc.
│   │   └── Dockerfile
│   ├── docker-compose.yml
│   ├── k8s/              # Directory for Kubernetes manifests
│   │   ├── web-deployment.yaml
│   │   ├── web-service.yaml
│   │   ├── db-deployment.yaml # Or db-statefulset.yaml
│   │   ├── db-service.yaml
│   │   ├── db-pvc.yaml     # Optional: PersistentVolumeClaim
│   │   └── configmap.yaml  # Optional: ConfigMap/Secret
│   └── README.md         # Optional: Project-specific README
└── README.md             # This file
```

## Project 1: Static Website Hosting

<details>
<summary>Click to expand Project 1 details</summary>

### Description 

A simple project demonstrating how to containerize a basic static HTML website using Nginx and deploy it to Kubernetes.

### Technologies                     

* HTML
* Nginx (via Docker image `nginx:alpine`)
* Docker
* Kubernetes

### Running with Docker 

1.  Navigate to the `project-1-static-site` directory:
    ```bash
    cd project-1-static-site
    ```
2.  Build the Docker image:
    ```bash
    docker build -t static-website:v1 .
    ```
3.  Run the container:
    ```bash
    docker run -d -p 8080:80 --name static-web static-website:v1
    ```
4.  Access the site at `http://localhost:8080`.
5.  Stop and remove the container when done:
    ```bash
    docker stop static-web
    docker rm static-web
    ```

### Deploying to Kubernetes 

1.  Ensure your Kubernetes cluster is running. We will be using Docker Desktop for this entire project.
2.  Navigate to the `project-1-static-site` directory:
    ```bash
    cd project-1-static-site
    ```
3.  Apply the Kubernetes manifests:
    ```bash
    # Ensure the image name in deployment.yaml matches your built image
    # For local images, you might need imagePullPolicy: Never in deployment.yaml
    kubectl apply -f deployment.yaml
    kubectl apply -f service.yaml
    ```
4.  Check the status:
    ```bash
    kubectl get deployments
    kubectl get services
    kubectl get pods
    ```
5.  Access the service:
    * If using Minikube: `minikube service static-website-service`
    * Otherwise, find the NodePort (`kubectl get svc static-website-service`) and access `http://<NodeIP>:<NodePort>` or `http://localhost:<NodePort>` (often works with Docker Desktop).
6.  Delete the resources when done:
    ```bash
    kubectl delete -f service.yaml
    kubectl delete -f deployment.yaml
    ```

</details>

## Project 2: Basic Web Application

<details>
<summary>Click to expand Project 2 details</summary>

### Description 

Containerizing a simple dynamic web application (e.g., built with Python/Flask or Node.js/Express) and deploying it to Kubernetes.

### Technologies 

* * Python (Flask/Django)
    * Node.js (Express)
    * * Docker
* Kubernetes

### Running with Docker 

1.  Navigate to the `project-2-basic-app` directory:
    ```bash
    cd project-2-basic-app
    ```
2.  Build the Docker image:
    ```bash
    # Replace 'basic-app' with your chosen image name
    docker build -t basic-app:v1 .
    ```
3.  Run the container (replace `5000` with your app's actual port if different):
    ```bash
    # Example for Flask default port 5000
    docker run -d -p 5000:5000 --name my-basic-app basic-app:v1
    ```
4.  Access the app at `http://localhost:5000`.
5.  Stop and remove the container when done:
    ```bash
    docker stop my-basic-app
    docker rm my-basic-app
    ```

### Deploying to Kubernetes 

1.  Ensure your Kubernetes cluster is running.
2.  Navigate to the `project-2-basic-app` directory:
    ```bash
    cd project-2-basic-app
    ```
3.  Apply the Kubernetes manifests:
    ```bash
    # Ensure the image name in deployment.yaml matches your built image
    # For local images, you might need imagePullPolicy: Never in deployment.yaml
    kubectl apply -f deployment.yaml
    kubectl apply -f service.yaml
    ```
4.  Check the status:
    ```bash
    kubectl get deployments
    kubectl get services
    kubectl get pods
    ```
5.  Access the service (check the NodePort or use `minikube service <service-name>`). The `targetPort` in `service.yaml` should match your application's port (e.g., 5000).
6.  Delete the resources when done:
    ```bash
    kubectl delete -f service.yaml
    kubectl delete -f deployment.yaml
    ```

</details>

## Project 3: Multi-Container Web App + Database

<details>
<summary>Click to expand Project 3 details</summary>

### Description 

Deploying a more complex application consisting of a web frontend/API interacting with a database (e.g., PostgreSQL, MongoDB, Redis). This project introduces Docker Compose for local development and multi-component Kubernetes deployments.

### Technologies 

* * Python (Flask/Django)
    * Node.js (Express)
    * * * PostgreSQL
    * MongoDB
    * Redis
    * * Docker & Docker Compose
* Kubernetes (Deployments/StatefulSets, Services, ConfigMaps/Secrets, PersistentVolumeClaims)

### Running with Docker Compose 

1.  Navigate to the `project-3-multi-container` directory:
    ```bash
    cd project-3-multi-container
    ```
2.  Build and start the services:
    ```bash
    docker-compose up --build -d
    ```
3.  Access the web application (check `docker-compose.yml` for the exposed port, e.g., `http://localhost:8000`).
4.  Stop and remove the containers, networks, and volumes:
    ```bash
    docker-compose down -v
    ```

### Deploying to Kubernetes 

1.  Ensure your Kubernetes cluster is running and supports PersistentVolumes if using PVCs.
2.  Build the web application Docker image (if not already done):
    ```bash
    cd project-3-multi-container/web-app # Navigate to your web app directory
    # Replace <your-dockerhub-username>/multi-app-web:v1 with your image name/tag
    # You might need to push this image to a registry like Docker Hub if your K8s cluster can't access local images easily.
    docker build -t <your-dockerhub-username>/multi-app-web:v1 .
    # docker push <your-dockerhub-username>/multi-app-web:v1 # If needed
    cd ../.. # Go back to the main repo directory
    ```
3.  Navigate to the Kubernetes manifests directory:
    ```bash
    cd project-3-multi-container/k8s
    ```
4.  Apply the Kubernetes manifests:
    ```bash
    # Apply configuration and storage first (if applicable)
    # kubectl apply -f configmap.yaml # Or secret.yaml
    # kubectl apply -f db-pvc.yaml

    # Apply database deployment/statefulset and service
    kubectl apply -f db-deployment.yaml # Or db-statefulset.yaml
    kubectl apply -f db-service.yaml

    # Apply web app deployment and service
    # *** Ensure the image name in web-deployment.yaml is correct! ***
    kubectl apply -f web-deployment.yaml
    kubectl apply -f web-service.yaml
    ```
5.  Check the status (wait for Pods to become Ready):
    ```bash
    kubectl get deployments,statefulsets,services,pods,pvc,configmaps,secrets
    ```
6.  Access the web application service (check the NodePort or use `minikube service <web-service-name>`).
7.  Delete the resources when done (delete in reverse order of application, roughly):
    ```bash
    kubectl delete -f web-service.yaml
    kubectl delete -f web-deployment.yaml
    kubectl delete -f db-service.yaml
    kubectl delete -f db-deployment.yaml # Or db-statefulset.yaml
    # kubectl delete -f db-pvc.yaml
    # kubectl delete -f configmap.yaml # Or secret.yaml
    ```

</details>

## Learning & Contribution

Feel free to clone this repository, experiment with the projects, and modify them. The goal is to provide a hands-on learning experience for Docker and Kubernetes fundamentals.

If you find issues or have suggestions for improvement, please feel free to open an issue or submit a pull request.

