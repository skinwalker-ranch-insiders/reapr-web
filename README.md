# reapr-web

Installing:
```
$ git clone git@github.com:skinwalker-ranch-insiders/reapr-web.git
$ cd reapr-web/
$ [Edit settings.py with your favorite editor and save it]
$ sudo docker build -t python-docker .
$ sudo docker run --name reapr-web -d -p 5000:5000 python-docker
```
To view collected records open: http://[DockerIP]:5000

This will display the contents of the table: yt_events in the database you specify in settings.py

You can customize the HTML template in templates/table.html
