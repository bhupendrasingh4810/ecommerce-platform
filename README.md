# Enterprise E-Commerce Platform

An enterprise-grade, production-ready, multi-tenant SaaS e-commerce platform built with **Django**, **Django REST Framework**, and **PostgreSQL** using a **feature-based modular architecture** and clean engineering principles.

This project is designed to demonstrate how large-scale software is built in real-world organizations. It emphasizes scalability, maintainability, security, and developer experience while implementing modern backend design patterns.

## Core Features

* Multi-Tenant SaaS Architecture
* Multi-Vendor Marketplace
* JWT Authentication & Refresh Tokens
* Role-Based Access Control (RBAC)
* User, Tenant & Membership Management
* Product Catalog & Inventory
* Shopping Cart & Checkout
* Order & Shipment Management
* Payment Integration
* Pricing & Promotions
* Notifications (Email, SMS, Push)
* Audit Logs & Activity Tracking
* AI-powered Features
* Analytics & Reporting
* WebSocket-based Real-time Features
* Background Jobs with Celery & Redis
* Swagger / OpenAPI Documentation
* Enterprise-grade Exception Handling
* Repository & Service Pattern
* Soft Delete & Audit Fields
* Docker-ready Deployment
* CI/CD Friendly Project Structure

## Tech Stack

* Python
* Django
* Django REST Framework
* PostgreSQL
* Redis
* Celery
* Django Channels
* WebSockets
* JWT Authentication
* drf-spectacular (Swagger/OpenAPI)
* Elasticsearch
* Docker
* Nginx
* GitHub Actions

This repository is intended as a reference implementation for developers preparing for senior backend interviews, learning enterprise Django architecture, or building production-scale SaaS applications.


### custom management command
`python manage.py create_feature tenancy tenants create`

### Get forlder structure
`tree -L 3 modules`

### Get all file paths
`find modules -name "*.py"`

### Creates the whole sub-domain skeleton.
`python manage.py create_subdomain tenancy domains`

### Remove all migrations
`find modules -path "*/migrations/*.py" ! -name "__init__.py" -delete`
`find modules -path "*/migrations/*.pyc" -delete`