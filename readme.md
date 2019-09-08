# Django - The Easy Way (3rd Edition)

Source code for my Django beginner book.

This book teaches you how to build a Django web application
from scratch and deploy it to a production server.

Read more: <https://samulinatri.com/shop/django-the-easy-way>

# How to use this?

In the book we create this project step-by-step but you can test the final product with following commands:

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

## Notes

- (1) You might need to use "python3 -m venv venv" or "python -m venv venv" in your system. Make sure it's **Python 3**.

- (2) Use "source venv/bin/activate" in *Unix-like* systems.

- (3) Use "cp" instead of "copy" in *Unix-like* systems and *forward* slashes.

