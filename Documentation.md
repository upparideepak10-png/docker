# Docker Full-Stack Application Assignment

## Overview
This project contains a full-stack application utilizing a **Node.js/Express frontend** and a **Flask backend**. Both services are containerized using Docker and orchestrated together using Docker Compose.

## Folder Structure
- `/frontend`: Contains the Node.js Express server and HTML form.
- `/backend`: Contains the Python Flask API.
- `docker-compose.yml`: The compose file to run both services on the same network.
- `Dockerfile`: Individual dockerfiles in both frontend and backend directories.

## Execution Steps (To capture screenshots for submission)

1. **Build and Run the Containers**
   Run the following command in the root directory where `docker-compose.yml` is located:
   ```bash
   docker-compose up --build -d
   ```
   *(Take a screenshot of the terminal output showing containers building and starting)*

2. **Verify Containers are Running**
   ```bash
   docker ps
   ```
   *(Take a screenshot showing both `node_frontend` and `flask_backend` running on ports 3000 and 5000)*

3. **Test the Application**
   - Open a web browser and navigate to `http://localhost:3000`
   - Fill out the form with a Name and Message, and click Submit.
   - The response from the Flask backend will appear below the button.
   *(Take a screenshot of the browser showing the successful form submission)*

4. **Push Images to Docker Hub**
   ```bash
   docker login
   docker tag docker_mutyala_vineela_frontend yourdockerhubusername/frontend:v1
   docker tag docker_mutyala_vineela_backend yourdockerhubusername/backend:v1
   docker push yourdockerhubusername/frontend:v1
   docker push yourdockerhubusername/backend:v1
   ```
   *(Take a screenshot of the terminal showing the successful push or your Docker Hub repository page)*

5. **Push Code to GitHub**
   ```bash
   git init
   git add .
   git commit -m "Initial commit for Docker Assignment"
   git branch -M main
   git remote add origin https://github.com/YourUsername/YourRepoName.git
   git push -u origin main
   ```
   *(Take a screenshot of your GitHub repository containing the files)*

## Links
- **GitHub Repository:** [Insert your GitHub URL here]
- **Docker Hub Frontend:** [Insert Docker Hub URL here]
- **Docker Hub Backend:** [Insert Docker Hub URL here]
