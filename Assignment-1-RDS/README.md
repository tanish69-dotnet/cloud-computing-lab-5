# Assignment 1 – Deploy and Connect Database for EC2 Application

## Objective

Deploy an application on an EC2 instance and connect it to an Amazon RDS PostgreSQL database.

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

## RDS Configuration

- Database Engine: PostgreSQL
- Database: Linkding
- RDS Instance: linkding-rds
- Region: ap-south-1 (Mumbai)

## EC2 Application

The Linkding application was deployed using Docker and Docker Compose on the EC2 instance.

The application was accessed through the EC2 public IP.

## Database Connection

The Linkding application was configured to connect to the PostgreSQL database.

The PostgreSQL database was verified from the EC2 environment.

The deployed database contained multiple application tables.

## CRUD Operations

CRUD operations were demonstrated through the running Linkding application:

### Create
A new bookmark was created through the application.

### Read
The created bookmark was displayed in the bookmarks list.

### Update
The bookmark details were modified through the application.

### Delete
The bookmark was deleted through the application.

## Security

The EC2 Security Group was configured to allow the required application/database communication.

No AWS access keys were hardcoded into the application.

## Evidence

Evidence includes:

- EC2 instance running
- RDS PostgreSQL database
- Database schema
- Docker containers
- Linkding application
- Create, Read, Update and Delete operations
