Retail Orders App

A simple retail order backend with a complete CI/CD pipeline using GitHub Actions, Docker, and AWS EC2.

What this project does
Exposes a REST API to create and list retail orders
Stores data in MySQL
Automatically builds and deploys on every git push

Tech Stack
Python (Flask)
MySQL
Docker & Docker Compose
GitHub Actions
GitHub Container Registry (GHCR)
AWS EC2 (Ubuntu)

Architecture (high level)
Git push
   ↓
GitHub Actions (CI/CD)
   ↓
GHCR (Docker Image)
   ↓
AWS EC2 (Docker Compose)
