# Scalable API

A backend API project built with FastAPI, PostgreSQL, SQLAlchemy, and Docker.

## Project Overview

This project is being built to practise professional backend development with a clean, scalable structure. It currently supports basic user creation and retrieval using FastAPI and PostgreSQL.

## Tech Stack

- Python
- FastAPI
- PostgreSQL
- SQLAlchemy
- Docker
- Git / GitHub

## Current Features

- FastAPI application setup
- Modular project structure
- User routes in a dedicated router
- Service layer for user logic
- Schemas for request and response validation
- PostgreSQL database integration
- SQLAlchemy user model
- GET `/users` endpoint
- POST `/users` endpoint
- Interactive API docs with Swagger at `/docs`

## Project Structure

```text
scalable-api/
│
├── app/
│   ├── main.py
│   ├── api/
│   │   └── users.py
│   ├── core/
│   │   ├── config.py
│   │   └── database.py
│   ├── models/
│   │   └── user.py
│   ├── schemas/
│   │   └── user.py
│   └── services/
│       └── user_service.py
│
├── tests/
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
├── .env
├── .gitignore
└── README.md