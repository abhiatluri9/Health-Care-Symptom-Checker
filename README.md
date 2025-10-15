# Healthcare Symptom Checker

This is a small project that helps people check their health symptoms using a website. The user can select symptoms from a list or type their symptoms in a textbox. After submitting, the website will show possible health conditions and give basic advice. This tool is not meant to replace a doctor. It is only for learning and basic understanding.

## What this project does

The project has two parts. The first part is the front-end, which is the website that people see and use. It is made using HTML, CSS, and JavaScript. The second part is the back-end, which is the brain of the project. It is made using Python and FastAPI. The back-end receives the symptoms, checks them, and sends back the results. The project also saves each symptom check in a small database using SQLite.

## What you need to run this project

To run this project, you need Python installed on your computer. You also need some Python packages like FastAPI, Uvicorn, and Pydantic. You can install them using pip, which is a tool that comes with Python. You also need a web browser like Chrome or Firefox to open the website.

## How to set it up

First, open your project folder in your computer. You can use a tool like PyCharm or just use File Explorer. Then open Git Bash or any terminal in that folder. Run the following commands to install the required packages:

```
pip install fastapi uvicorn pydantic jinja2
```

After that, run the server using this command:

```
uvicorn app:app --reload
```

This will start the server. Now open your browser and go to this address:

```
http://localhost:8000
```

You will see the symptom checker website. You can now select symptoms or type them in the textbox and click the button to check.

## How the project works

When you select symptoms or type them, the website sends that information to the server. The server checks the symptoms using a Python file called `llm_utils.py`. It looks for keywords like "fever", "headache", or "vomiting" and gives possible conditions and advice. The result is shown on the website. At the same time, the server saves your symptom and result in a database file called `symptom_history.db`.

## Files in the project

- `index.html`: This is the website file. It has the form and buttons.
- `app.py`: This is the main server file. It connects the website to the logic.
- `llm_utils.py`: This file checks the symptoms and gives results.
- `database.py`: This file saves the symptom and result in the database.
- `schemas.py`: This file defines the format of the data sent and received.
- `symptom_history.db`: This is the database file. It is created automatically when you run the project.

## Important note

This project is only for learning. It does not give real medical advice. If you are sick or have serious symptoms, you should go to a doctor. This tool is just for practice and understanding how websites and servers work together. And also you can integrate with real API key for better analysis. Here only few conditions are given,if integrated, it would provide a better analysis. 


