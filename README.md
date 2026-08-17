# Cloud Computing Lab 5

## Overview

This repository contains the implementation of Lab 5 assignments for Cloud Computing.

The assignments demonstrate deploying database services on AWS and connecting them with applications running on an EC2 instance.

---

# Assignment 1 – RDS PostgreSQL

## Objective

Deploy an application on Amazon EC2 and connect it to an Amazon RDS PostgreSQL database.

## AWS Services Used

- Amazon EC2
- Amazon RDS PostgreSQL
- Docker
- Docker Compose

## Architecture

EC2 Instance
        |
        v
Linkding Application
        |
        v
Amazon RDS PostgreSQL

## Database

Database Engine: PostgreSQL

The RDS database was connected to the Linkding application running on EC2.

## CRUD Operations

The application demonstrates:

- Create
- Read
- Update
- Delete

## Security

The EC2 instance communicates with the database through the configured Security Group rules.

No AWS access keys were hardcoded in the application.

---

# Assignment 2 – DynamoDB

## Objective

Deploy and connect an application running on EC2 to Amazon DynamoDB using an IAM Role.

## AWS Services Used

- Amazon EC2
- Amazon DynamoDB
- AWS IAM
- Python
- Flask
- Boto3

## Architecture

EC2 Instance
        |
        v
Flask DynamoDB Application
        |
        v
Amazon DynamoDB

## DynamoDB Table

Table Name:

`linkding-dynamodb`

Partition Key:

`id`

## IAM Authentication

The EC2 instance uses the IAM role:

`DynamoDB-EC2-Role`

The application uses the EC2 IAM role through Boto3.

No hardcoded AWS access keys are used.

## CRUD Operations

The application demonstrates:

- Create
- Read
- Update
- Delete

## DynamoDB Attribute Types

The application demonstrates the following DynamoDB data types:

| Attribute | Type |
|---|---|
| id | String |
| title | String |
| rating | Number |
| is_favorite | Boolean |
| tags | List |
| metadata | Map |

## Application

The Assignment 2 application is implemented using:

- Python
- Flask
- Boto3

The application runs on the EC2 instance and communicates with DynamoDB.

---

# Evidence

Screenshots and other evidence demonstrate:

- EC2 application running
- Database deployment
- IAM configuration
- CRUD operations
- DynamoDB attribute types
