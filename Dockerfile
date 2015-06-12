from ubuntu:14.04

maintainer softworks 

ENV DEBIAN_FRONTEND noninteractive

run apt-get update
run apt-get install -y build-essential git
run apt-get install -y python3.4 python3.4-dev python-setuptools
run apt-get install -y nginx supervisor
run apt-get install -y libpq-dev

# install uwsgi now because it takes a little while
run apt-get install -y python3-pip
run pip3 install uwsgi

# install nginx
run apt-get install -y python-software-properties
run apt-get install -y sqlite3

# install our code
add . /home/docker/code/

# setup all the configfiles
run echo "daemon off;" >> /etc/nginx/nginx.conf
run rm /etc/nginx/sites-enabled/default
run ln -s /home/docker/code/prod/nginx-app.conf /etc/nginx/sites-enabled/
run ln -s /home/docker/code/prod/supervisor-app.conf /etc/supervisor/conf.d/

# run pip install
run pip3 install -r /home/docker/code/requirements.txt

#setup django stuff
run cd /home/docker/code && python3 manage.py collectstatic --noinput

expose 80
cmd ["supervisord", "-n"]
