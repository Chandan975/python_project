# Todo API

This project is a simple Todo API built with Django and Django REST framework. It provides CRUD operations for Todo items, user registration and login, and role-based access control.

## Features

- CRUD operations for Todo items
- User registration and login
- JWT authentication
- Role-based access control (Admin and User roles)
- Swagger documentation for API endpoints

## API Endpoints

### AuthController

- `POST /api/users/`: Register a new user
- `POST /api/token/`: Obtain JWT token
- `POST /api/token/refresh/`: Refresh JWT token

### TodoController

- `GET /api/todos/`: Get all todo items (Accessible by all authenticated users)
- `GET /api/todos/{id}/`: Get a single todo item (Admin only)
- `POST /api/todos/`: Create a new todo item (Admin only)
- `PUT /api/todos/{id}/`: Update a todo item (Admin only)
- `DELETE /api/todos/{id}/`: Delete a todo item (Admin only)

## Setup

### Prerequisites

- Python 3.x installed
- SQL Server database setup

### Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/yourusername/your-repo-name.git
    cd your-repo-name
    ```

2. Create a virtual environment and activate it:

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install dependencies:

    ```sh
    pip install -r requirements.txt
    ```

4. Configure your database settings in `myproject/settings.py`:

    ```python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sql_server',
            'NAME': 'your_db_name',
            'USER': 'your_db_user',
            'PASSWORD': 'your_db_password',
            'HOST': 'your_db_host',
            'PORT': 'your_db_port',
        }
    }
    ```

5. Apply migrations:

    ```sh
    python manage.py makemigrations
    python manage.py migrate
    ```

6. Create a superuser:

    ```sh
    python manage.py createsuperuser
    ```

7. Run the server:

    ```sh
    python manage.py runserver
    ```

### Usage

1. Register a new user:

    ```sh
    POST /api/users/
    ```

2. Obtain a JWT token:

    ```sh
    POST /api/token/
    ```

3. Refresh a JWT token:

    ```sh
    POST /api/token/refresh/
    ```

4. Access Todo items (Admin and User roles):

    ```sh
    GET /api/todos/
    ```

5. Admin operations on Todo items (Admin only):

    ```sh
    GET /api/todos/{id}/
    POST /api/todos/
    PUT /api/todos/{id}/
    DELETE /api/todos/{id}/
    ```

### Swagger Documentation

Access the Swagger UI at `http://127.0.0.1:8000/swagger/` to interact with and test the API endpoints.

### Deployment

To deploy the project to Heroku, follow the [Heroku Django deployment guide](https://devcenter.heroku.com/articles/deploying-python).

## License

This project is licensed under the MIT License.
