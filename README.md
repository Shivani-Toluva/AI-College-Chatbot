# AI-Powered College Chatbot Using NLP

An NLP-based college enquiry chatbot developed using Python, Django, Natural Language Processing, Machine Learning, and MySQL. The application automates responses to frequently asked college-related queries through a web-based conversational interface.

## Project Overview

Students frequently require information about admissions, courses, fees, departments, timings, and other college-related services. Manually responding to repetitive enquiries can be time-consuming.

This project addresses this problem by providing an automated chatbot that processes natural-language queries and identifies the most relevant response using text similarity techniques.

The application uses TF-IDF vectorization and Cosine Similarity to match user queries with available information and integrates MySQL for storing and retrieving college-related data.

## Key Features

* Interactive college enquiry chatbot
* Natural Language Processing-based query processing
* TF-IDF text vectorization
* Cosine Similarity-based response matching
* MySQL database integration
* Database-driven college information
* Web-based chatbot interface
* Django backend
* Python-based NLP processing

## Technology Stack

### Programming Language

* Python

### Backend Framework

* Django

### Natural Language Processing and Machine Learning

* Natural Language Processing (NLP)
* NLTK
* Scikit-learn
* TF-IDF Vectorization
* Cosine Similarity

### Frontend

* HTML
* CSS
* JavaScript

### Database

* MySQL
* XAMPP

### Development Tools

* Git
* GitHub

## System Workflow

```text
User Query
    |
    v
Input Processing
    |
    v
NLP Preprocessing
    |
    v
TF-IDF Vectorization
    |
    v
Cosine Similarity
    |
    v
Relevant Information Matching
    |
    v
MySQL Database
    |
    v
Chatbot Response
```

### Workflow Description

1. The user enters a college-related question through the chatbot interface.
2. The input is processed using NLP techniques.
3. The query is converted into a numerical representation using TF-IDF vectorization.
4. Cosine Similarity is used to compare the query with available information.
5. The most relevant information is identified.
6. Required information is retrieved from the MySQL database.
7. The chatbot displays the corresponding response to the user.

## Information Handled

The chatbot is designed to handle common college-related enquiries, including:

* Admission information
* Courses and programs
* Fee information
* Department information
* College timings
* General college information
* Frequently asked questions

## Database Integration

MySQL is used to store and manage the information required by the chatbot.

The database can contain structured information related to:

* Frequently asked questions
* FAQ responses
* Courses
* Admissions
* Fees
* Departments
* Other college-related information

XAMPP can be used to run the MySQL database in the local development environment.

## Project Structure

The project follows a Django-based application structure.

```text
AI-College-Chatbot/
|
├── admin.py
├── apps.py
├── models.py
├── nlp.py
├── settings.py
├── tests.py
├── urls.py
├── views.py
├── asgi.py
├── wsgi.py
└── README.md
```

### Important Components

| File          | Description                                        |
| ------------- | -------------------------------------------------- |
| `models.py`   | Defines the application's database models          |
| `views.py`    | Handles application requests and chatbot responses |
| `nlp.py`      | Contains NLP and chatbot processing logic          |
| `urls.py`     | Defines application URL routing                    |
| `settings.py` | Contains Django project configuration              |
| `admin.py`    | Configures Django administration                   |
| `tests.py`    | Contains application tests                         |
| `asgi.py`     | ASGI configuration for deployment                  |
| `wsgi.py`     | WSGI configuration for deployment                  |

## Getting Started

### Prerequisites

Ensure the following software is installed:

* Python 3.x
* pip
* Django
* MySQL
* XAMPP
* Git

### Clone the Repository

```bash
git clone https://github.com/Shivani-Toluva/AI-College-Chatbot.git
```

### Navigate to the Project Directory

```bash
cd AI-College-Chatbot
```

### Install Dependencies

If a `requirements.txt` file is available:

```bash
pip install -r requirements.txt
```

Otherwise, install the required dependencies configured for the project.

### Configure MySQL

Start Apache and MySQL through XAMPP.

Create the required database and configure the database connection in Django's `settings.py` file.

### Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### Run the Development Server

```bash
python manage.py runserver
```

Open the local development server in a web browser to access the application.

## Application Screenshots

### Chatbot Interface

Add a screenshot of the chatbot interface:

```markdown
![College Chatbot Interface](screenshots/chatbot-interface.png)
```

### Example Conversation

Add a screenshot demonstrating an actual conversation between the user and chatbot:

```markdown
![Chatbot Conversation](screenshots/chatbot-conversation.png)
```

### System Workflow

Add an architecture or workflow diagram:

```markdown
![Chatbot Architecture](screenshots/chatbot-architecture.png)
```

## Example Queries

The chatbot can be used for queries such as:

```text
What courses are offered?

What are the admission requirements?

What are the college fees?

What departments are available?

What are the college timings?

Where can I get admission information?
```

## Project Objectives

The primary objectives of this project are to:

* Automate repetitive college enquiries
* Apply NLP techniques to real-world text queries
* Implement text similarity for response matching
* Integrate a relational database with a chatbot
* Develop a web-based application using Python and Django
* Gain practical experience with NLP and machine learning workflows

## Technical Highlights

### NLP-Based Query Processing

Natural Language Processing techniques are used to process and prepare user queries for similarity-based matching.

### TF-IDF Vectorization

TF-IDF is used to convert textual information into numerical feature vectors that can be compared computationally.

### Cosine Similarity

Cosine Similarity is used to measure the similarity between the user's query and available text information and identify the most relevant match.

### Database-Driven Responses

MySQL stores structured college information, allowing the application to retrieve relevant data dynamically.

### Django Web Application

Django provides the backend framework for integrating the chatbot processing logic, database, routing, and web interface.

## Future Enhancements

Potential improvements to the project include:

* Administrative dashboard for managing chatbot information
* User authentication and authorization
* Cloud deployment
* Voice-based interaction
* Multilingual support
* Chat analytics and usage tracking
* Advanced semantic search
* Embedding-based information retrieval
* Large Language Model integration
* Retrieval-Augmented Generation (RAG)

These features are proposed future enhancements and are not part of the current implementation.

## Learning Outcomes

This project provided practical experience in:

* Python development
* Django backend development
* Natural Language Processing
* TF-IDF vectorization
* Cosine Similarity
* Machine Learning concepts
* MySQL database integration
* Web application development
* Git and GitHub
* End-to-end chatbot development

## Author

### Toluva Laxmi Shivani

BCA Graduate | Python Developer | AI and NLP Enthusiast

Technical interests:

`Python` `Django` `NLP` `Machine Learning` `Generative AI` `Backend Development`
