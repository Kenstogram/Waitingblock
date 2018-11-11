# Waitingblock
## A Basic Django Waitinglist App built using [django_tables2](https://github.com/jieter/django-tables2), [Bootstrap4](https://getbootstrap.com/)

Ensure you have virtualenv installed and on your path

```
which virtualenv
```

should return anything other than `virtualenv not found`

Create a new virtual environment with your machine's python3 as the default python

```
virtualenv -p python3 myenv 
``` 

Activate your virtual environment

```
source myenv/bin/activate
```

Install the required dependencies for this project:

```
python3 -m pip install -r requirements.txt
```

Build the database by running all available migrations:

```
python3 manage.py migrate
```

We can set up our local server from the **Waitingblock** directory
```
python manage.py runserver
```

If you'd like to use this in production, please make sure to set the `SECRET_KEY` environment variable, like so:

```
SECRET_KEY=<a_secret_key> python3 manage.py runserver
```
