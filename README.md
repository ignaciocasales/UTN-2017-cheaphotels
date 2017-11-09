# Cheap Hotels

> UTN - 2017

Made by

 - _Ignacio Casales_
 - _Santiago Blanc_

### Project Setup

- Install **python 3.6.3**

- Install **pip**

- Install **Django 1.11.7** 
```Bash
$ pip install Django==1.11.7
```

- Install **pillow**

````Bash
$ pip install Pillow
````

- Go to the project root

````Bash
$ cd UTN-2017-cheaphotels
````

- Migrate & Create superuser

````bash
$ python manage.py migrate

$ python manage.py makemigrations

$ python manage.py createsuperuser
````

- Start the development server
````Bash
$ python manage.py runserver
````

- Enter the admin site at 
 
    - `http://127.0.0.1:8000/admin/`

### Intellij Setup

- Install python plugin

- Define Project SDK to python

- Setup django framework

    - Project root
    
    `/YOUR_PATH/UTN-2017-cheaphotels`
    
    - Define settings.py
    
    `/YOUR_PATH/UTN-2017-cheaphotels/cheaphotels/settings.py`
    
    - Define manage.py
    
    `/YOUR_PATH/UTN-2017-cheaphotels/manage.py`
    
    - Create a run configuration
