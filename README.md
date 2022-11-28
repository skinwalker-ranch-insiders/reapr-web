# reapr-web

Installing:
```
$ git clone git@github.com:skinwalker-ranch-insiders/reapr-web.git
$ cd reapr-web/
$ sudo docker build -t python-docker .
$ sudo docker run --name reapr-web -d -p 5000:5000 python-docker
```

To view collected records open: http://[DockerIP]:5000
