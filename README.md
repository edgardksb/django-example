# django-example

This is my django software example

For use this example:
```
    $ pip install --upgrade virtualenv
    $ virtualenv env
    $ source env/bin/activate
    (env) $ pip install -r requirements.txt
    (env) $ python manage.py migrate 
    (env) $ python manage.py createsuperuser --username admin
    (env) $ python manage.py drf_create_token admin
    (env) $ python manage.py runserver
``` 

For deploy this app, you follow above steps:

### 1 - Collect the static files
```
(env) $ python manage.py collectstatic
```
###  2 - Change setting
Change the settings **DEBUG** and **SECRET_KEY** in settings.py file

###  3 - Buid docker
```
sh build.sh
```