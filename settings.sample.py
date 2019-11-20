# IP or URL for PiHole api.php
url = "https://your.pihole.com/api.php"

# IP or URL for uvicorn FastAPI service
api_host = '127.0.0.1'
api_port = 8000

# HTTP BASIC AUTHENTICATION
# If PiHole Webgui is behind basic access authentication set "enabled" to True
# and enter credentials.
#
# If it's not, set enabled to False and leave "usr", "passwd" blank.
auth = {
    "enabled": True,
    "usr": "admin",
    "passwd": "password",
}
