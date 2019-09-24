# Django - The Easy Way (3rd Edition)

<img align="left" width="100" src="misc/cover.png">

<h3>Source code for my Django beginner book: https://leanpub.com/django-the-easy-way/</h3>

This book teaches you how to build a Django web application from scratch and deploy it to a production server.

<br>

Check out the introduction video:

[<img src="https://img.youtube.com/vi/C65X2qWuU5A/maxresdefault.jpg" width="50%">](https://youtu.be/C65X2qWuU5A)

## About the author

Hi, my name is Samuli Natri. I’m a programmer focusing on **Python** and **Django**. I also dabble with C/C++ and OpenGL. I’m familiar with Node.js, Asp.Net Core, Drupal, C#, JavaScript, PHP, HTML and CSS. I attended Helsinki University of Technology (Computer Science) and Helsinki University (Social Sciences).

## How to use this?

In the book we create this project step-by-step but you can test the final product like this:

### Windows

```
mkdir demo
cd demo
git clone git@github.com:SamuliNatri/Django-The-Easy-Way-Source-Code.git code
py -m venv venv
venv\Scripts\activate.bat
cd code
pip install -r requirements.txt
python manage.py migrate
copy assets\local_settings_local.py mysite\local_settings.py
python manage.py loaddata assets\flowers2.json
python manage.py createsuperuser
python manage.py runserver
```

### macOS, Linux (Unix-like systems)

```
mkdir demo
cd demo
git clone git@github.com:SamuliNatri/Django-The-Easy-Way-Source-Code.git code
python3 -m venv venv
source venv/bin/activate
cd code
pip install -r requirements.txt
python manage.py migrate
cp assets/local_settings_local.py mysite/local_settings.py
python manage.py loaddata assets/flowers2.json
python manage.py createsuperuser
python manage.py runserver
```
