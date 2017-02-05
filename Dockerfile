FROM python:3-onbuild
COPY data/db.dump.json ./data.json
RUN python ./sources/manage.py makemigrations schema
RUN python ./sources/manage.py migrate
RUN python ./sources/manage.py loaddata ./data.json
CMD echo -e "ADMIN LOGIN = root\nADMIN PASSWORD = orange123" && \
    python ./sources/manage.py runserver 0.0.0.0:8000
