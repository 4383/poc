FROM python:3-onbuild
COPY data/db.dump.json ./data.json
RUN python ./sources/manage.py makemigrations schema
RUN python ./sources/manage.py migrate
RUN python ./sources/manage.py loaddata ./data.json
#RUN echo "from django.contrib.auth.models import User; User.objects.filter(email='root@root.com').delete(); User.objects.create_superuser('root', 'root@root.com', 'rootroot')" | \
#    python sources/manage.py shell
#RUN echo "from django.contrib.auth.models import User; User.objects.filter(email='exploit1@exploit1.com').delete(); User.objects.create_superuser('exploit1', 'exploit1@exploit1.com', 'exploit1exploit1')" | \
#    python sources/manage.py shell
CMD echo -e "ADMIN LOGIN = root\nADMIN PASSWORD = rootroot" && python ./sources/manage.py runserver 0.0.0.0:8000
