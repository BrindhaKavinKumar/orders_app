Retail Orders App

A simple retail order backend with a complete CI/CD pipeline using GitHub Actions, Docker, and AWS EC2.

What this project does

Provides a REST API to create and list retail orders

Stores order data in a MySQL database

Automatically builds and deploys the application on every git push

Tech Stack

Python (Flask)

MySQL

Docker & Docker Compose

GitHub Actions

GitHub Container Registry (GHCR)

AWS EC2 (Ubuntu)

Architecture
Developer
   |
   | git push
   v
GitHub Actions (CI/CD)
   |
   | Build & push Docker image
   v
GitHub Container Registry (GHCR)
   |
   | Pull image
   v
AWS EC2
 ├── Flask API (Docker container)
 └── MySQL (Docker container)
