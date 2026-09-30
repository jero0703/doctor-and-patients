Doctor and Patient Management API

A RESTful API built using FastAPI, Python, SQLAlchemy, PyMySQL, and MySQL for managing doctors and patients.

Features

Doctor Management

Create a doctor

Get all doctors

Get a doctor by ID

Validate doctor email

Prevent duplicate doctor emails

Set doctor active/inactive status

Patient Management

Create a patient

Get all patients

Validate patient age

Validate patient name and phone number

Technologies Used

Python 3.9+

FastAPI

Uvicorn

Pydantic

SQLAlchemy

PyMySQL

MySQL

Swagger UI

Project Structure

doctor and patients/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   └── schemas.py
│
├── requirements.txt
├── README.md
└── .gitignore

Database Setup

Create the MySQL database:

CREATE DATABASE IF NOT EXISTS doctor_patient_db;

USE doctor_patient_db;

Doctors Table

CREATE TABLE IF NOT EXISTS doctors (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    specialization VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    is_active BOOLEAN DEFAULT TRUE
);

Patients Table

CREATE TABLE IF NOT EXISTS patients (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    age INT NOT NULL,
    phone VARCHAR(15) NOT NULL
);

MySQL Configuration

Open:

app/database.py

Configure the MySQL connection:

DATABASE_URL = "mysql+pymysql://root:YOUR_PASSWORD@localhost:3306/doctor_patient_db"

If your MySQL password contains special characters, URL-encode them.

For example, if the password is:

jero@2026

use:

DATABASE_URL = "mysql+pymysql://root:jero%402026@localhost:3306/doctor_patient_db"

Installation

Open PowerShell in the project root:

cd "C:\Users\Jero\Desktop\stackly\doctor and patients"

Create a virtual environment:

python -m venv venv

Activate it:

.\venv\Scripts\Activate.ps1

Install dependencies:

python -m pip install -r requirements.txt

Requirements

The requirements.txt file should contain:

fastapi
uvicorn
email-validator
sqlalchemy
pymysql

Run the Application

Run the FastAPI application from the project root:

python -m uvicorn app.main:app --reload

The API will run at:

http://127.0.0.1:8000

Swagger API Documentation

FastAPI automatically provides interactive API documentation.

Open:

http://127.0.0.1:8000/docs

You can test all API endpoints directly from Swagger UI.

API Endpoints

Doctor APIs

Create Doctor

POST /doctors

Example request:

{
    "name": "Dr. John Smith",
    "specialization": "Cardiologist",
    "email": "john@example.com",
    "is_active": true
}

Get All Doctors

GET /doctors

Get Doctor by ID

GET /doctors/{doctor_id}

Example:

GET /doctors/1

Patient APIs

Create Patient

POST /patients

Example request:

{
    "name": "Karthik Raja",
    "age": 25,
    "phone": "9876543210"
}

Get All Patients

GET /patients

Validation

The API performs request validation using Pydantic.

Doctor Validation

Name must contain at least 2 characters.

Specialization must contain at least 2 characters.

Email must be a valid email address.

Doctor email must be unique.

is_active defaults to true.

Patient Validation

Name must contain at least 2 characters.

Age must be greater than 0.

Phone number must contain between 10 and 15 characters.

HTTP Status Codes

Status Code

Meaning

200

Request successful

201

Resource created

400

Bad request / duplicate doctor email

404

Resource not found

422

Validation error

Testing Workflow

Start MySQL.

Create the doctor_patient_db database.

Configure the MySQL password in database.py.

Start the FastAPI server.

Open Swagger UI.

Create doctors using POST /doctors.

Retrieve doctors using GET /doctors.

Retrieve an individual doctor using GET /doctors/{doctor_id}.

Create patients using POST /patients.

Retrieve patients using GET /patients.

Example Response

Doctor

{
    "id": 1,
    "name": "Dr. John Smith",
    "specialization": "Cardiologist",
    "email": "john@example.com",
    "is_active": true
}

Patient

{
    "id": 1,
    "name": "Karthik Raja",
    "age": 25,
    "phone": "9876543210"
}

Error Example

If a doctor with the same email already exists:

{
    "detail": "Doctor with this email already exists"
}

If a doctor ID does not exist:

{
    "detail": "Doctor not found"
}

