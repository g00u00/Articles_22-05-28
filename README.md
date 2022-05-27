# Articles

git clone https://github.com/g00u00/Articles_22-05-28.git

<или>

git init

git remote add origin git@github.com:g00u00/Articles_22-05-28.git

git pull origin main

</или>

cd Articles_22-05-28

su

root

apt install python3.8-venv

exit


python3 -m venv env

. env/bin/activate

pip install -r requirements.txt

python manage.py runserver

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
