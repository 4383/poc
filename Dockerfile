FROM python:3-onbuild
COPY data/db.dump.json ./dump.json
#RUN python ./sources/manage.py makemigrations
#RUN python ./sources/manage.py migrate
RUN python ./sources/manage.py loaddata /usr/src/app/dump.json
RUN rm ./dump.json
CMD echo -e "ADMIN LOGIN = root\nADMIN PASSWORD = orange123" && python ./sources/manage.py runserver 0.0.0.0:8000

