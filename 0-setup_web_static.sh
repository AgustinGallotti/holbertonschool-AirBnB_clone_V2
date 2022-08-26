#!/usr/bin/env bash
# script that sets up your web servers for the deployement of web_static
apt-get update
apt-get install nginx -y
mkdir -p /data/
mkdir -p /data/web_static/
mkdir -p /data/web_static/releases/
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/current/
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test /data/web_static/current
sudo chown -hR ubuntu:ubuntu /data
sed -i "/listen 80 default_server;/a location /hbnb_static/ {alias /data/web_static/current/;}" /etc/nginx/sites-available/default
service nginx restart
exit 0
