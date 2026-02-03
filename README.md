Chemical Equipment Parameter Visualizer
Hybrid Web + Desktop Application

 Project Overview

The Chemical Equipment Parameter Visualizer is a hybrid application that works as both a Web Application and a Desktop Application.
It allows users to upload a CSV file containing chemical equipment data, performs analytics using a common backend, and visualizes results through charts and summaries.
Both frontends (React Web and PyQt Desktop) consume the same Django REST API, demonstrating a true hybrid architecture.

 Tech Stack

| Layer             | Technology                    |
| ----------------- | ----------------------------- |
| Backend           | Django, Django REST Framework |
| Data Processing   | Pandas                        |
| Database          | SQLite                        |
| Web Frontend      | React.js, Chart.js, Axios     |
| Desktop App       | PyQt5, Matplotlib             |
| API Communication | REST                          |
| Version Control   | Git & GitHub                  |

Project Structure

chemical_visualizer/
│
├── Backend/
│   ├── backend/          # Django project
│   ├── equipment/        # Django app
│   └── venv/             # Virtual environment
│
├── web-frontend/         # React web application
│
├── desktop-app/          # PyQt desktop application
│
├── sample_equipment_data.csv
│
└── README.md

Backend Features (Django)

CSV file upload API
Data analytics using Pandas
Summary statistics:
Total equipment count
Average flowrate
Average pressure
Average temperature
Equipment type distribution
SQLite database to store datasets
CORS enabled for frontend integration

API Endpoint
POST http://127.0.0.1:8000/api/upload/

Web Application (React)

Features
CSV file upload
Summary display
Bar chart visualization using Chart.js
Live API integration with Django backend

How to Run
cd web-frontend
npm install
npm start
Runs at:
http://localhost:3000

Desktop Application (PyQt)
Features

CSV file upload

Summary display

Bar chart visualization using Matplotlib

Uses the same backend API as the web app

How to Run
cd Backend
.\venv\Scripts\Activate.ps1
cd ..\desktop-app
python app.py

How to Run the Backend
cd Backend
.\venv\Scripts\Activate.ps1
cd backend
python manage.py runserver

Backend runs at:
http://127.0.0.1:8000

Visualization

Web: Interactive bar charts using Chart.js
Desktop: Matplotlib bar charts
Both visualizations represent equipment type distribution

Hybrid Architecture Explanation

A single Django REST API serves both platforms
React (Web) and PyQt (Desktop) independently consume the API
Ensures consistency and reusability of backend logic

Key Learning Outcomes

Full-stack application development
REST API design
CSV data processing using Pandas
Frontend–backend integration
Desktop and web hybrid architecture
Debugging real-world dependency and configuration issues
