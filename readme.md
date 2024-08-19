
---

# GRE Question Generator

This Django project utilizes a large language model to create GRE-style practice questions in JSON format. It provides users with multiple-choice questions, along with explanations for the correct answers.

## Features

- **Question Variety:** Generates questions with varying difficulty levels (single blank, double blank, triple blank).
- **Vocabulary Selection:** Selects random vocabulary words from predefined groups.
- **Distractor Options:** Avoids including synonyms of the correct answer in the option list.
- **Answer Explanations:** Provides explanations for the chosen answer.

## Installation

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

3. **Install the required packages:**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Run the development server:**
   ```bash
   python manage.py runserver
   ```

2. **Access the application:**
   Open your web browser and navigate to [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

## Contributing

Contributions are welcome! Please feel free to open a pull request with your changes.

---

