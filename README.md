# aichiworks

## Install Docker Desktop
docker-composeを使用するので、Docker Desktopをインストールする。

## clone this repo
this repo is private. so you need to access right.<br>
please contact me first.

## build and start

```bash
$ docker-compose build
```

start aichiworks

```
$ docker-compose up -d
```

## IP and Port setting
edit docker-compose.yml and app/firstSite/secret.py<br>
default IP and Port is 192.168.1.156 and 8081<br>

### docker-compse.yml > ports and command
```docker
services:
  app:
    container_name: app
    build: ./app
    volumes:
     - ./app/source:/django
     - ${PATHTOAICHIPRDB}:/django/aichiworks/data
    ports:
     - 8081:8081
    image: app:django
    command: python manage.py runserver 0.0.0.0:8081
    depends_on:
      - db
    restart: always

  db:
    image: mysql:5.7
    container_name: mysql
    volumes:
      - ./database/data:/var/lib/mysql
    ports:
      - 3333:3306
    environment:
      MYSQL_DATABASE: ${MYSQLDATABASE}
      MYSQL_ALLOW_EMPTY_PASSWORD: 'true'
    restart: always
```

### app/firstSite/secrets.py > ALLOWED_HOSTS
```python
ALLOWED_HOSTS = ["192.168.1.156"]
```

### Access

[`192.168.1.156:8081`](http://192.168.1.156:8081)
