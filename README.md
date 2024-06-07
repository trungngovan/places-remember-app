# Places Remember App
## Overview
The Places Remember App is a web application that allows users to save and view memorable places on a map. Users can log in using their Google account, add new memories by selecting a location on the map, and view their saved memories.

## Features
- User Authentication: Log in using Google OAuth.
- Add Memories: Select a place on the map and add comments.
- View Memories: Display a list of saved memories with their details.

## Technologies Used
- Frontend: HTML, CSS, Tailwind CSS, DaisyUI
- Backend: Django
- Authentication: django-allauth, Google OAuth
- Map Integration: Google Maps API

## Setup Instructions
### Prerequisites
- Python 3.11
- Node.js and npm

### Installation
1. Clone the repository:
    ```shell
    git clone https://github.com/trungngovan/places-remember-app.git
    cd places-remember-app
    ```

2. Set up a virtual environment and activate it:
    ```shell
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install Python dependencies:
    ```shell
    pip install -r requirements.txt
    ```

4. Set up the database:
    ```shell
    python manage.py makemigrations
    python manage.py migrate
    ```
5. Install Node.js dependencies:
    ```shell
    npm install
    ```

6. Build Tailwind CSS:
    ```shell
    npm run build:css
    ```

## Configuration
1. Google OAuth Setup:
   - Go to the Google Cloud Console.
   - Create a new project or select an existing project.
   - Go to "APIs & Services" > "Credentials".
   - Click "Create Credentials" > "OAuth 2.0 Client IDs".
   - Set the application type to "Web application".
   - Configure the "Authorized redirect URIs" (e.g., http://localhost:8000/accounts/google/login/callback/).
   - Copy the Client ID and Client Secret and add them to your Django settings.
2. Update settings.py:
    ```python
    SOCIALACCOUNT_PROVIDERS = {
        'google': {
            'SCOPE': [
                'profile',
                'email',
            ],
            'AUTH_PARAMS': {
                'access_type': 'online',
            },
            'CLIENT_ID': 'YOUR_GOOGLE_CLIENT_ID',
            'SECRET': 'YOUR_GOOGLE_CLIENT_SECRET',
        }
    }
    
    GOOGLE_MAPS_API_KEY = 'YOUR_GOOGLE_MAPS_API_KEY'
    ```
## Running the Project
1. Start the Django development server:
    ```shell
    python manage.py runserver
    ```

2. Access the application:

    Open your web browser and go to http://localhost:8000/.

