PiHole FastAPI
=============================

![image alt >](https://i.imgur.com/chcAAtn.png#right)

**FastAPI** is a modern, fast (high-performance), web framework for building APIs with Python 3.6+ based on standard Python type hints.  

**Pi-hole** is a Linux network-level advertisement and Internet tracker blocking application which acts as a DNS sinkhole (and optionally a DHCP server), intended for use on a private network. It is designed for use on embedded devices with network capability, such as the Raspberry Pi, but it can be used on other machines running Linux and cloud implementations.

### PiHole FastAPI
PiHole FastAPI is using PiHole's `api.php` to create it's own, easy to use API, with backend and docs. SwaggerUI and ReDoc is included in FastAPI.  

![](https://i.imgur.com/3oyoqhK.png")

### Installing
Clone repo
```sh
$ git clone https://github.com/dunderrrrrr/Pi-hole-FastAPI.git
```
Copy and edit `settings.py`.
```sh
$ cp settings.sample.py settings.py
$ nano settings.py
```
Create virtualenv and install requirements.
```sh
$ mkvirtualenv --python=/usr/bin/python3 pihole-api
$ pip install -r requirements.txt
```
Run FastAPI.
```sh
$ python run.py
```

FastAPI: `http://127.0.0.1:8000`.  
SwaggerUI: `http://127.0.0.1:8000/docs`.  
Redoc: `http://127.0.0.1:8000/redoc`.

Your API token for Pi-hole can be found in the Pi-hole settings tab (https://your.pihole.com/settings.php?tab=api).
