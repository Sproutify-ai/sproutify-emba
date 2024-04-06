Here's a recommended project structure for a modular Flask application that follows best practices:

```
myapp/
├── app/
│   ├── __init__.py
│   ├── main/
│   │   ├── __init__.py
│   │   ├── views.py
│   │   ├── models.py
│   │   └── forms.py
│   ├── auth/
│   │   ├── __init__.py
│   │   ├── views.py
│   │   ├── models.py
│   │   └── forms.py
│   ├── templates/
│   │   ├── base.html
│   │   ├── main/
│   │   │   ├── index.html
│   │   │   └── ...
│   │   └── auth/
│   │       ├── login.html
│   │       └── ...
│   ├── static/
│   │   ├── css/
│   │   ├── js/
│   │   └── img/
│   └── utils/
│       ├── __init__.py
│       └── helpers.py
├── tests/
│   ├── __init__.py
│   ├── test_main.py
│   └── test_auth.py
├── config.py
├── requirements.txt
├── run.py
└── .env
```

Explanation:

- `app/`: The main application package.
  - `__init__.py`: Initializes the Flask application and imports the necessary modules.
  - `main/`: A blueprint for the main functionality of the application.
    - `__init__.py`: Initializes the main blueprint.
    - `views.py`: Contains the view functions for the main blueprint.
    - `models.py`: Defines the database models for the main blueprint.
    - `forms.py`: Defines the forms for the main blueprint.
  - `auth/`: A blueprint for the authentication functionality.
    - `__init__.py`: Initializes the auth blueprint.
    - `views.py`: Contains the view functions for the auth blueprint.
    - `models.py`: Defines the database models for the auth blueprint.
    - `forms.py`: Defines the forms for the auth blueprint.
  - `templates/`: Contains the HTML templates for the application.
    - `base.html`: The base template that other templates extend.
    - `main/`: Templates for the main blueprint.
    - `auth/`: Templates for the auth blueprint.
  - `static/`: Contains static files (CSS, JavaScript, images, etc.).
  - `utils/`: Contains utility modules and helper functions.
    - `__init__.py`: Makes the utils directory a Python package.
    - `helpers.py`: Contains helper functions used across the application.

- `tests/`: Contains the unit tests for the application.
  - `__init__.py`: Makes the tests directory a Python package.
  - `test_main.py`: Contains unit tests for the main blueprint.
  - `test_auth.py`: Contains unit tests for the auth blueprint.

- `config.py`: Contains the configuration settings for the application.
- `requirements.txt`: Lists the dependencies required by the application.
- `run.py`: The entry point for running the application.
- `.env`: Stores environment variables for the application.

This structure organizes the application into modular blueprints (`main` and `auth`), separates concerns (views, models, forms), and follows a clear directory structure. It also includes separate directories for templates, static files, and utility modules.

Remember to keep your application code modular, write unit tests, use configuration files, and follow Flask best practices and conventions while building your application.
