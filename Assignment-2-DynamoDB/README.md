# Assignment 2 – Deploy and Connect DynamoDB for EC2 Application

## Objective

Deploy an application on an EC2 instance and connect it to Amazon DynamoDB using an IAM Role.

## AWS Services Used

- Amazon EC2
- Amazon DynamoDB
- AWS IAM

## Technologies Used

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

## DynamoDB Configuration

- Table Name: `linkding-dynamodb`
- Partition Key: `id`
- Region: `ap-south-1`

## IAM Configuration

The EC2 instance uses the IAM role:

`DynamoDB-EC2-Role`

Boto3 uses the IAM role attached to the EC2 instance to access DynamoDB.

No AWS access keys are hardcoded in the application.

## Application

The application is a Flask-based Bookmark Manager.

It runs on the EC2 instance and communicates with DynamoDB using Boto3.

## CRUD Operations

The application demonstrates all CRUD operations:

### Create

A new bookmark is created through the Flask application and stored in DynamoDB.

### Read

Stored bookmarks are retrieved from DynamoDB and displayed by the application.

### Update

Existing bookmark attributes such as title, rating and tags are updated through the application.

### Delete

A bookmark is deleted from DynamoDB through the application.

## DynamoDB Attribute Types

The application demonstrates the following DynamoDB data types:

| Attribute | DynamoDB Type |
|---|---|
| `id` | String (S) |
| `title` | String (S) |
| `rating` | Number (N) |
| `is_favorite` | Boolean (BOOL) |
| `tags` | List (L) |
| `metadata` | Map (M) |

## Security

DynamoDB access is performed using the EC2 IAM Role instead of hardcoded AWS credentials.

## Evidence

The practical evidence includes:

- EC2 application running
- Application accessible through EC2
- DynamoDB table
- Create operation
- Read operation
- Update operation
- Delete operation
- DynamoDB attribute types
- IAM Role attached to EC2
