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
Now you have the app docker image ready for use ;)

### 4 - Time for choosing where you run your docker image
If you want just run in your local machine, use **run.sh** script
```
sh run.sh
```
This case running in http://localhost:8888

If you deploy in **Heroku**
```
heroku login
heroku container:login
heroku create
heroku container:push django-example
heroku container:release django-example
```