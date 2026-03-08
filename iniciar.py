import os

os.environ['FLASK_APP'] = 'application.py'
os.environ['FLASK_ENV'] = 'development'

os.system('flask run --host=0.0.0.0 --port=5000')
