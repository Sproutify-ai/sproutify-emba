# 🌱 Sproutify 🌱

Welcome to Sproutify, a Python AI project for human-AI collaborative evaluation of early-stage innovations.

## 📋 About the Project

Sproutify was developed to explore the impact of AI-assisted decision-making in innovation screening. Based on research conducted by Lane, Boussioux, et al. (2025), this web application implements a screening interface that can operate in three distinct modes:

1. **Human-only evaluation** (control)
2. **Black-box AI recommendations** (without explanations)
3. **Narrative AI assistance** (with detailed justifications)

The application facilitates rapid screening of early-stage innovations against predefined criteria, with an option to incorporate AI recommendations with varying degrees of transparency.

## 🎯 Research Background

This project stems from research on the "human-AI oversight paradox" - the phenomenon where AI systems intended to augment human decision-making may inadvertently reduce critical engagement as AI capabilities improve. The field experiment conducted with 228 evaluators screening 48 early-stage innovations revealed that evaluators given AI assistance were 19% more likely to align with AI recommendations compared to those making unassisted decisions.

Interestingly, while narrative explanations increased human alignment with AI recommendations, particularly for rejection decisions, they did not improve decision quality compared to simple recommendations without justifications. Both AI-assisted conditions, however, led to higher-quality screening outcomes than unassisted evaluation.

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
/solutions/<id>/98q3hiwnaj
/solutions/<id>/98hy3fqeh3
/solutions/<id>/0o3e8u5t8i
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
The app mainly was coded and designed by Ian Chen, Pei-Hsin Wang, and Camila Lin (University of Washington), with the input of Léonard Boussioux, Jacqueline Lane, Charles Ayoubi and MIT Solve.


## NOTES

The original experiment intent
1. No Justification v2
2. With Justification v3

Business target
1. Make non-expert screners be as fast and as similar to the expert screeners
2. We want the process to be fast
3. The goal is to be super lazy! Just trust AI!

V2 just give the first failure reason.
