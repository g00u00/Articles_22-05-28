# Articles

git clone https://github.com/g00u00/Articles.git

или

git init

git remote add origin git@github.com:g00u00/Articles.git

git pull origin main

cd Articles

python3 -m venv env

. env/bin/activate

pip install -r requirements.txt

python manage.py runserver 10.0.2.15:8000

admin admin admin

deactivate

----------------

python manage.py shell

from django.db import models

from articl.models import Post

Post.objects.all()

Post.objects.values_list()

dir(Post.objects.filter(id__lte=20))

Post.objects.filter(id__lte=110).delete()


-------------

iptables -t nat -A PREROUTING -i eth0 -p tcp --dport 80 -j REDIRECT --to-port 8000

-------------

pip freeze > requirements.txt

pip install -r requirements.txt
