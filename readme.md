# GRE Question Generator

This Django project utilizes a large language model to create GRE-style practice questions in JSON format. It provides users with multiple-choice questions with explanations for the correct answers.

## Features

* Generates questions with varying difficulty levels (single blank, double blank, triple blank)
* Selects random vocabulary words from predefined groups
* Avoids including synonyms of the correct answer in the option list
* Provides explanations for the chosen answer

## Installation

1. Clone this repository.
2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt   



 

    

Usage

Run the development server:
    
    ```bash
    python manage.py runserver

   

Access the application in your web browser at http://127.0.0.1:8000/

Contributing

Contributions are welcome! Please feel free to open a pull request with your changes.
