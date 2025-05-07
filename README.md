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

### Evaluation Process

The screening interface presents solutions alongside five hierarchical criteria:

1. **Completeness and intelligibility**: Is the solution application complete, appropriate, and intelligible?
2. **Development stage**: Is the solution at least at the prototype stage?
3. **Challenge alignment**: Does the solution address the challenge question?
4. **Technology integration**: Is the solution powered by technology?
5. **Overall quality**: Is the quality good enough for external review?

Evaluators assess submissions sequentially against these criteria, failing solutions at the first criterion they do not meet. Only solutions passing all five criteria advance to the next evaluation stage.

## 📊 Key Features

- Three distinct evaluation interfaces (human-only, black-box AI, narrative AI)
- Structured five-criteria hierarchical evaluation process
- AI-generated recommendations calibrated with few-shot learning from past decisions
- Timer functionality to limit decision time per solution
- Mouse tracking for analyzing user engagement
- Confidence scoring for each decision

## 📝 License

This project is licensed under the MIT License.

## 🔬 Research Implementation

The AI recommendation system is based on an LLM trained through few-shot learning on past screening decisions. It evaluates each solution against the five criteria and provides:

- Pass/fail recommendations for each criterion
- Confidence scores (interpreted as probabilities)
- In the narrative condition, approximately 200-word rationales explaining the decision

The interface design includes visual indicators (green checkmarks for 'pass' and red X marks for 'fail') consistent across AI-assisted conditions.

## 📝 License

This project is licensed under the MIT License.

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the issues page.

## 👥 Contributors

The original research and experimental design was conducted by:
- Jacqueline N. Lane (Harvard Business School & Digital Data and Design Institute at Harvard)
- Léonard Boussioux (University of Washington)
- Charles Ayoubi (Harvard Business School)
- Ying Hao Chen (University of Washington)
- Camila Lin (University of Washington)
- Rebecca Spens (MIT Solve)
- Pooja Wagh (MIT Solve) 
- Pei-Hsin Wang (University of Washington)

The application was primarily developed by Ian Chen, Pei-Hsin Wang, and Camila Lin (University of Washington), with input from Léonard Boussioux, Jacqueline Lane, Charles Ayoubi and MIT Solve.

## 📄 Abstract

This field experiment investigated whether AI-generated narrative explanations enhance or diminish human oversight in early-stage innovation screening. With 228 evaluators screening 48 innovations under three conditions (human-only, black-box AI recommendations, and narrative AI with explanations), the research revealed a human-AI oversight paradox: screeners with AI assistance were 19% more likely to align with AI recommendations, particularly when AI suggested rejection. Despite increased scrutiny of AI rejection recommendations (shown by higher mouse activity), narrative explanations still increased deference to AI. Evaluators were equally influenced by substantive quality and mere persuasiveness, using narrative coherence as a primary heuristic. While both AI-assisted conditions yielded higher-quality screening outcomes than unassisted evaluation, narrative explanations provided no incremental quality benefits beyond black-box recommendations despite increasing compliance. These findings suggest that high-volume information processing tasks may inherently benefit from algorithmic assistance, challenging how organizations balance efficiency with meaningful human judgment.
