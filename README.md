# creating task table
"flask db migrate -m "Initial migration."

# apply the migration to the database
"flask db upgrade"

# start app
"flask run"

# start mode development
set FLASK_ENV=development
set FLASK_APP=run.py
flask run