# HNG-BACKEND-TASK_TWO
### TASK INSTRUCTIONS
You are to build a simple REST API capable of CRUD operations on a "person" resource, interfacing with any database of your choice. Your API should dynamically handle parameters, such as adding or retrieving a person by name.
Your API should be flexible enough to handle dynamic input. If we provide a name (or other details), your backend should be able to process operations using that name.
Name field should only be strings; integers or any other data type should not be allowed.

## Introduction
This api was built using Flask. It relies on MySQL database to store and retrieve data.

### Installation

### 1. Clone the Repository

```bash
git clone https://github.com/SamuelNgundi/HNGX-Stage_Two
cd HNGX-Stage_Two
```

### 2. Create and Activate a Virtual Environment

```bash
# Create a virtual environment
python3 -m venv .venv
```

```bash
# Activate the virtual environment
source .venv/bin/activate # Linux/Mac
.venv\Scripts\activate # Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```


### 4. Run the App

```bash
python app.py
```

The API will run locally on 
```bash
http://localhost:5000/api/
```



##[DOCUMENTATION.md](DOCUMENTATION.md) file
## Live URL: [link](https://samuelwngundi.pythonanywhere.com/api)

### Authors
* [Samuel Ngundi](https://github.com/SamuelNgundi)
