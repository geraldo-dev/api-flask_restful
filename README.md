## create virtual environment
````
python -m venv env
````
## activate virtual environment
in the window
````
env\scripts\active.bat
````

##  install dependencies
````
pip install -r requirements.txt
````

## creating task table
````
flask db migrate -m "Initial migration."
````

## apply the migration to the database
````
flask db upgrade
````

## start production app
````
flask run
````

## start mode development
````
set FLASK_ENV=development
set FLASK_APP=run.py
flask run
````
