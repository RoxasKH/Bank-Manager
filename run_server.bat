cd %cd%
python init_db.py
set FLASK_APP=app
set FLASK_ENV=development
flask run
PAUSE