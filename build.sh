#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt

python manage.py collectstatic --verbosity=3 --noinput
python manage.py makemigrations
python manage.py migrate

echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'jpcurrinir@gmail.com', 'admin')" | python manage.py shell