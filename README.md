# Flask Demo App

This is a simple demo Flask app designed to show basic user login and signup functionality. The app allows users to register and log in with their credentials, which are stored in a plain-text JSON file. **This is not a production-ready app and should not be used in real-world applications without proper security measures, especially password encryption.**

## Features

- **Login and Signup**: Users can sign up with their name, age, experience, username, and password. They can log in using their username and password.
- **User Info**: After logging in, the app displays the user's information in a table format.
- **Jinja2 Templates**: The app uses Jinja2 templates for rendering HTML pages.
- **Data Storage**: User data is stored in a plain-text JSON file.

## Prerequisites

- Python 3.x
- Flask
- Gunicorn (for running the app in production)

## Project Structure

```
.
├── app.py                  # Main Flask app
├── templates
│   ├── base.html           # Base template with navigation bar
│   ├── login.html          # Login page template
│   ├── signup.html         # Signup page template
│   ├── user_info.html      # Template to show user info
├── users.json              # JSON file to store user data
├── requirements.txt        # Python dependencies
├── Dockerfile              # Dockerfile for containerizing the app
├── docker-compose.yml      # Docker Compose file to run the app
└── README.md               # Project documentation
```

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/your-username/flask-demo-app.git
cd flask-demo-app
```

### 2. Install the dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Flask app

```bash
python app.py
```

### 4. Docker Support

The project supports Docker and can be run inside a container. Follow these steps to build and run the Docker container:

#### Build the Docker Image

```bash
docker build -t flask-demo-app .
```

#### Run the Docker Container

```bash
docker run -p 8000:8000 flask-demo-app
```

Now, the app will be accessible at `http://localhost:8000`.

### 5. Docker Compose Support

Alternatively, you can use Docker Compose to set up and run the application. The provided `docker-compose.yml` file simplifies this process.

#### Docker Compose Setup

```yaml
services:
  flask_app:
    build: .
    ports:
      - "8000:8000"
    expose:
      - "8000"
```

#### Run the App with Docker Compose

```bash
docker-compose up
```

This will build the image and start the app on `http://localhost:8000`.

## Important Notes

- **Password Security**: The app stores user passwords in plain text in the JSON file. This is for demo purposes only. In a production environment, **never store passwords in plain text**. Use a proper hashing algorithm like `bcrypt`.
  
- **Not Production-Ready**: This app is a demo and is not intended for production use. It lacks security measures such as CSRF protection, input validation, and password hashing.

## License

This project is open source and available under the [MIT License](LICENSE).
# FlaskAuthDemo
