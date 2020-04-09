#!/usr/bin/env bash
# Script to configure server to deploy a fake web static
apt-get -y update
apt-get -y install nginx
mkdir -p /data/web_static/releases/test
mkdir -p /data/web_static/shared/
echo "<html>
   <head>
   </head>
   <body>
      Holberton School is the law
   </body>
 </html>" | sudo tee /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data
sed -i '43i\\n\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t\t autoindex on;\n\t}\n' /etc/nginx/sites-available/default
service nginx reload
exit 0
