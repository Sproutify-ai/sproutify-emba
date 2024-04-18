# 🌱 Sproutify 🌱

Welcome to Sproutify, a Python AI project.

## 🚀 Getting Started

1. Clone the repository.
2. Install the dependencies with pip:

```sh
pip install -r requirements.txt
```

3. Run the project:

```sh
./start.sh
```

## 🖥️ Usage

To switch different versions of the solution, you can use the following URLs:
```
/solutions/<id>/v1
/solutions/<id>/v2
/solutions/<id>/v3
```

## 📚 Project Structure

- `sproutify/`: Main application code.
  - `auth.py`: Authentication related code.
  - `config.py`: Configuration related code.
  - `db.py`: Database related code.
  - `main.py`: Main application entry point.
  - `models.py`: Database models.
  - `templates/`: HTML templates for the application.
- `migrations/`: Alembic migrations.
- `manage.py`: Management commands for the application.
- `requirements.txt`: Project dependencies.
- `start.sh`: Script to start the application.

## 📝 License

This project is licensed under the MIT License.

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

## 🙏 Acknowledgments

Thanks to all contributors who have helped to improve this project.



## NOTES

The original experiment intent
1. No Justification v2
2. With Justification v3

Business target
1. Make non-expert screners be as fast and as similar to the expert screeners
2. We want the process to be fast
3. The goal is to be super lazy! Just trust AI!

V2 just give the first failure reason.