# django-sample

For using this example:
```
    $ pip install --upgrade virtualenv
    $ virtualenv env
    $ source env/bin/activate
    (env) $ pip install phonenumbers 
    (env) $ pip install django-phonenumber-field 
    (env) $ pip install pip install djangorestframework
    (env) $ python manage.py migrate 
    (env) $ python manage.py createsuperuser --username admin
    (env) $ python manage.py drf_create_token admin
    (env) $ python manage.py runserver
``` 