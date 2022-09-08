# Installation for django Enviroment

###  1. Install pip and python first

`sudo apt install -y python3-pip python-is-python3`

### 2. Install virtualenv using pip

` pip install virtualenv `

### 3. Create a virtual environment

` virtualenv venv `

### 4. Active your virtual environment:

` source venv/bin/active `

### 5. install django and other models in virtual environment: (e.g. telephone, rest_framework, markdown...etc.)

`pip install django djangorestframework markdown django-filter django-phonenumber-field[phonenumbers] drf-yasg django-cors-headers `

# Django developing for Axtasy Web UI

## When you want to start up the MJS(Make Job system) you need to mkdir 2 Forlders on the path /home/minghsuan/Desktop

- Django Phone Model https://github.com/stefanfoulis/django-phonenumber-field 
- React read CSRF token from cookie https://www.learnfk.com/question/reactjs/50732815.html
- Django read json from React https://stackoverflow.com/questions/6541767/python-urllib-error-attributeerror-bytes-object-has-no-attribute-read
- (Django login page) [https://learndjango.com/tutorials/django-login-and-logout-tutorial]

## Tipps

- get request User after login https://stackoverflow.com/questions/62580622/how-to-access-current-user-from-django-to-react
- Kann durch `request.user` zu nehmen das Information, wer dies Website request sendt.
- `from django.contrib.auth import authenticate` to import authenticate function and use `authenticate` with `username` and `password` to authenticate, which user is using now.
