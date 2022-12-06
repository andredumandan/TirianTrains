# Tirian Trains Database

Made for the fulfillment of the 2nd Project Deliverable for the subject **CSCI 41: Information Management** for the First Semester of **A.Y. 2022 - 2023**

## Group Name: G Kain After  

### Group Members:
1. Andre Dumandan
2. Earl Felizardo
3. Rau Layug
4. Jeremy Lee
5. Ansley Sze
6. Chester Tan


## To run the this prototype:

1.) Setup a python virtual environment.

2.) Activate the virtual environment.

3.) Install Django via ```pip install django```.

4.) Install dotenv via ```pip install python-dotenv```.

5.) Install Postgres compatibility via ```pip install psycopg2```.

6.) Setup the database by running the ```tiriantrains.sql``` file in postgres.

7.) Populate the database with entries by running the ```populate.sql``` in postgres.

8.) Perform migrations by running "python manage.py makemigrations" and ```python manage.py migrate```.

9.) Run the django project by navigating through the root folder and run ```python manage.py runserver``` in the console.
