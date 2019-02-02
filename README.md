# Waitingblock
## Django Waitinglist App

### Setup Enviroment

Ensure you have virtualenv installed and on your path
```
$ which virtualenv
```
should return anything other than `virtualenv not found`
Create a new virtual environment with your machine's python3 as the default python
```
$ virtualenv -p python3 myenv
```
Activate your virtual environment
```
$ source myenv/bin/activate
```
Install the required dependencies for developing this project:
```
$ python3 -m pip install -r requirements-dev.txt
```
### Prepare database
```
$ python3 manage.py makemigrations
$ python3 manage.py migrate
$ python manage.py migrate --run-syncdb
```
### Start development server
```
$ python3 manage.py runserver
```
### Production
If you'd like to use this in production, please make sure to set the `SECRET_KEY` environment variable, like so:
```
SECRET_KEY=<a_secret_key> python manage.py runserver
```
