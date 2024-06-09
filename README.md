# Places Remember App

## Overview

The Places Remember App is a web application that allows users to save and view memorable places on a map. Users can log in using their Google account, add new memories by selecting a location on the map, and view their saved memories.

## Features

- User Authentication: Log in using Google OAuth (raw flow).
- Add Memories: Select a place on the map and add comments.
- View Memories: Display a list of saved memories with their details.

## Technologies Used

- Frontend: HTML, CSS, Tailwind CSS, DaisyUI
- Backend: Django
- Authentication: Google OAuth (raw flow)
- Map Integration: Google Maps API

## Setup Instructions

### Prerequisites

- Python 3.11
- Node.js and npm
- MySQL
- Conda

### Installation

1. Clone the repository:

    ```shell
    git clone https://github.com/trungngovan/places-remember-app.git
    cd places-remember-app
    ```

2. Set up a conda environment and activate it:

    ```shell
    conda create --name places-remember python=3.11
    conda activate places-remember
    ```

3. Install Python dependencies:

    ```shell
    pip install -r requirements.txt
    ```

4. Set up the MySQL database:

    ```sql
    CREATE DATABASE your_db_name;
    CREATE USER 'your_db_user'@'localhost' IDENTIFIED BY 'your_db_password';
    GRANT ALL PRIVILEGES ON your_db_name.* TO 'your_db_user'@'localhost';
    FLUSH PRIVILEGES;
    ```

5. Update the `settings.py` file:

    ```python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'your_db_name',
            'USER': 'your_db_user',
            'PASSWORD': 'your_db_password',
            'HOST': 'localhost',
            'PORT': '3306',
        }
    }
    ```

6. Set up the database schema:

    ```shell
    python manage.py makemigrations
    python manage.py migrate
    ```

7. Install Node.js dependencies:

    ```shell
    npm install
    ```

8. Build Tailwind CSS:

    ```shell
    npm run build:css
    ```

## Configuration

1. Google OAuth Setup:
    - Go to the [Google Cloud Console](https://console.cloud.google.com/).
    - Create a new project or select an existing project.
    - Go to "APIs & Services" > "Credentials".
    - Click "Create Credentials" > "OAuth 2.0 Client IDs".
    - Set the application type to "Web application".
    - Configure the "Authorized redirect URIs" (e.g., http://localhost:8000/oauth2callback/).
    - Copy the Client ID and Client Secret.

2. Update `settings.py`:

    ```python
    GOOGLE_CLIENT_ID = 'YOUR_GOOGLE_CLIENT_ID'
    GOOGLE_CLIENT_SECRET = 'YOUR_GOOGLE_CLIENT_SECRET'
    GOOGLE_REDIRECT_URI = 'http://localhost:8000/oauth2callback'
    GOOGLE_MAPS_API_KEY = 'YOUR_GOOGLE_MAPS_API_KEY'
    ```

## Running the Project

1. Start the Django development server:

    ```shell
    python manage.py runserver
    ```

2. Access the application:

    Open your web browser and go to http://localhost:8000/.

## Running Tests

1. Run the tests:

    ```shell
    python manage.py test
    ```
