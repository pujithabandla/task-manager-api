\# Task Manager API



\## Overview

A RESTful backend API built using Flask that allows users to manage tasks with full CRUD functionality.



\## Features

\- Create tasks

\- Retrieve all tasks

\- Retrieve a single task

\- Update tasks

\- Delete tasks



\## Tech Stack

\- Python

\- Flask

\- REST API



\## How to Run

1\. Create virtual environment:

&#x20;  python -m venv venv



2\. Activate:

&#x20;  venv\\Scripts\\activate



3\. Install dependencies:

&#x20;  pip install flask



4\. Run the app:

&#x20;  python app.py



\## API Endpoints



GET /tasks  

GET /tasks/<id>  

POST /tasks  

PUT /tasks/<id>  

DELETE /tasks/<id>



\## Sample Response



{

&#x20; "id": 1,

&#x20; "title": "Learn Flask",

&#x20; "description": "Build API",

&#x20; "done": false

}

