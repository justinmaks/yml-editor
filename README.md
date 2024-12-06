# YAML File Editor Web App

## Overview

This project is a web-based YAML file editor built using Python and Flask. The application allows you to browse a directory structure, view YAML files, and edit them in real-time. It's fully containerized with Docker and supports Docker Compose for easy deployment.

---

## Features

- **File Browser**: Displays the directory structure with clickable links for `.yml` and `.yaml` files.
- **Real-Time Editing**: Edit YAML files directly in the browser and save changes in real-time.
- **Dockerized**: Fully containerized using Docker for consistent and portable deployments.
- **Easy Setup**: Supports Docker Compose for streamlined multi-container setup.

---

## Technologies Used

- **Backend**: Python (Flask, Flask-SocketIO)
- **Frontend**: HTML, JavaScript
- **Containerization**: Docker, Docker Compose

---

## Prerequisites

- Docker installed on your system
- Docker Compose installed on your system

---

## Directory Structure

```plaintext
your_project/
├── app.py               # Main application code
├── templates/
│   ├── index.html       # File browser template
│   └── editor.html      # File editor template
├── Dockerfile           # Docker image definition
├── docker-compose.yml   # Docker Compose configuration
├── requirements.txt     # Python dependencies
├── path_to_your_directory/  # Directory with YAML files
```

## Setup and Installation

```bash
docker-compose up --build
```

## config

```plaintext
- The path_to_your_directory volume in docker-compose.yml maps your local YAML files directory to the container.
- You can customize the FLASK_ENV environment variable for production or development.
```
