# HNG-BACKEND-TASK_TWO
### TASK INSTRUCTIONS
You are to build a simple REST API capable of CRUD operations on a "person" resource, interfacing with any database of your choice. Your API should dynamically handle parameters, such as adding or retrieving a person by name.
Your API should be flexible enough to handle dynamic input. If we provide a name (or other details), your backend should be able to process operations using that name.
Name field should only be strings; integers or any other data type should not be allowed.

### Introduction
This api was built using Flask. It relies on MySQL database to store and retrieve data.
### Usage
* The api is hosted on pythonanywhere and can be accessed at: https://samuelwngundi.pythonanywhere.com/api
* The endpoint to get a list of all people in the database is at: https://samuelwngundi.pythonanywhere.com/api
### API Endpoints
| HTTP Verbs | Endpoints | Action |
| --- | --- | --- |
| POST | https://samuelwngundi.pythonanywhere.com/api | To create a new person |
| GET | https://samuelwngundi.pythonanywhere.com/api | To retrieve all data from the database |
| GET | https://samuelwngundi.pythonanywhere.com/api/user_id | To retrieve details of a person by their user ID |
| PUT | https://samuelwngundi.pythonanywhere.com/api/user_id | To edit the details of a person by their user ID |
| DELETE | https://samuelwngundi.pythonanywhere.com/api/user_id | To delete details of a person by their user ID |
### Technologies Used
* [Flask](https://flask.palletsprojects.com/en/2.3.x/) Flask is a web application framework written in Python. 
* [MySQL](https://www.mysql.com) MySQL is a relational database management system.

### Authors
* [Samuel Ngundi](https://github.com/SamuelNgundi)