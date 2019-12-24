# This script is used for testing purposes.
# Use it like this in unix-like systems:
# source build.sh
python3 -m venv venv && \
source venv/bin/activate && \
pip install -r requirements.txt && \
python manage.py migrate && \
python manage.py loaddata ../data/data.json && \
cp -fr ../data/media_files media && \
python manage.py runserver
~
