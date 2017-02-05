# POC
POC download available on [docker hub](https://hub.docker.com/r/4383/poc/)

## Usage

### With docker
```shell
$ docker pull 4383/poc
$ docker run -it --publish 80:8000 4383/poc
$ # now open your webbrowser at container ip
$ # connect you with login:root, password:rootroot
```

### Local installation
```shell
$ git clone https://github.com/4383/poc
$ cd poc
$ pip install -r requirements.txt
$ python sources/manage.py makemigrations schema
$ python sources/manage.py migrate
$ python sources/manage.py loaddata data/db.dump.json
$ python sources/manage.py runserver
$ # now open your webbrowser at container ip
$ # connect you with login:root, password:rootroot
```
## Author
[Hervé BERAUD](http://github.com/4383)
