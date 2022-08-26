#!/usr/bin/env bash
# script that sets up your web servers for the deployement of web_static
server {
  root /data;

  location /web_static/releases {
    try_files $uri /web_static/releases;
  }

  location /web_static/shared {
    try_files $uri /web_static/shared;
  }

  location /web_static/releases/test {
    try_files $uri /web_static/releases/test;
  }

  location /web_static/releases/test/index.html {
    alias /data/web_static/releses/test/index.html;
    try_files $uri /web_static/releases/test/index.html;
  }
}
LN -s /data/web_static/current/ /data/web_static/releses/test/
#GRANTS owner /data/ USER ubuntu
sudo chown -R www-data:www-data ubuntu /data/web_static_releases/test/index.html
location /index.html/ { alias /data/web_static/releases/test/index.html; }
service nginx restart
