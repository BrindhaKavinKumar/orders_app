# **Retail Orders App**

A simple **retail order backend** demonstrating a complete **CI/CD pipeline** using  
**GitHub Actions**, **Docker**, and **AWS EC2**.

---

## **What this project does**

- Provides REST APIs to create and list retail orders  
- Stores order data in a MySQL database  
- Automatically builds and deploys the application on every `git push`

---

## **Tech Stack**

- **Language:** Python (Flask)
- **Database:** MySQL
- **Containers:** Docker, Docker Compose
- **CI/CD:** GitHub Actions
- **Container Registry:** GitHub Container Registry (GHCR)
- **Cloud:** AWS EC2 (Ubuntu)

---

## **Architecture**

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
