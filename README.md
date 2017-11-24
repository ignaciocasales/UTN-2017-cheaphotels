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
$ cd UTN-2017-cheaphotels\src\cheaphotels
````


- Migrate Initial Data

````bash
$ python manage.py migrate
````

- Migrate Bookings Models
````bash
$ python manage.py makemigrations bookings
$ python manage.py migrate bookings
````

- Seed premade Users

````Bash
$ python manage.py loaddata users.json
````

- Start the development server
````Bash
$ python manage.py runserver
````

- Enter the admin site at 
 
    - `http://127.0.0.1:8000/admin/`

- Premade user data:
	- Superuser:
	
		username: superuser
		
		password: super123
		
	- Admin:
	
		username: admin
		
		password: adder123
		
	- Owners:
	
		- jane.doe:
		
			username: jane.doe
			
			password: j4n3123456
			
		- john.doe:
		
			username: john.doe
			
			password: j0hn123456		

### Intellij Setup

- Install python plugin

- Define Project SDK to python

- Setup django framework

    - Project root
    
    `/YOUR_PATH/UTN-2017-cheaphotels/src/cheaphotels`
    
    - Define settings.py
    
    `/YOUR_PATH/UTN-2017-cheaphotels/src/cheaphotels/cheaphotels/settings.py`
    
    - Define manage.py
    
    `/YOUR_PATH/UTN-2017-cheaphotels/src/cheaphotels/manage.py`
    
    - Create a run configuration
