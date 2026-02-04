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
└── git push
└── GitHub Actions (CI/CD)
├── CI: run tests + build Docker image
└── CD: push image to GHCR
└── AWS EC2
└── Docker Compose
├── Flask API container (port 5000)
└── MySQL container (persistent volume)



