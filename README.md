# Project Setup Guide

Welcome to the [Project Name] repository! This guide will help you clone and set up the Django project on your local machine.

## Prerequisites

- Python (version 3.10 or higher)
- Git

## Clone the Repository

1. Open a terminal or command prompt.
2. Navigate to the directory where you want to clone the project.
3. Run the following command to clone the repository:

   ```bash
   git clone [repository_url]
   ```

## Set Up the Virtual Environment
1. Navigate to the project directory.
   ```
   cd [project_name]
   ```
2. Create a virtual environment.
   ```
   python -m venv venv
   ```
3. Activate the virtual environment.
   ```
   <!-- linux/macOS -->
   source venv/bin/activate

   <!-- windows -->
   venv\Scripts\activate
   ```
4. Install the project dependencies.
   ```
   pip install -r requirements.txt
   ```

## Run server
1. In the project directory, run the following command:
   ```
   python manage.py runserver {port}  
   ```
2. Open a browser and go to `http://localhost:{port}` to view the project.
3. To stop the server, press `Ctrl+C` in the terminal or command prompt.
4. To deactivate the virtual environment, run the following command:
   ```
   deactivate
   ```
   