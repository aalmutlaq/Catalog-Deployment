Steps of accomplishing the deployment project:
1-	Create an instance in Amazon lightsail 
2-	Generate ssh keys by $ sudo ssh-keygen 
3-	Move the private key in your directory ~/.ssh/filename
4-	Add permission to the key so no one can read or write on it except the owner by $ chmod 600 ~/.ssh/
5-	Connect to the instance using ssh. $ ssh –i ~/.ssh/key grader@ipaddress
6-	Create user $ sudo adduser grader
7-	Give grader user permission to sudo $ sudo nano /etc/sudoer.d/grader then add the following line: grader ALL =(ALL:ALL) ALL
8-	Change the ssh port form 22 to 2200 $ ~/etc/ssh/sshd_config  then edit the port form 22 to 2200
9-	Restart the ssh service  $ sudo service ssh restart
10-	Configure local time zone $ sudo timedatectl set-timezone UTC.
11-	Update packages $ sudo apt-get update. And $ sudo apt-get upgrade.
12-	Configure the firewall $ sudo ufw default deny incoming $ sudo ufw default allow outgoing || $ sudo ufw allow 2200/tcp  ||  $ sudo ufw allow www || $ sudo ufw allow ntp || $ sudo ufw enable
13-	Install apache2 $ sudo apt-get install apache2 libapache2-mod-wsgi git
14-	Enable mod_wsgi $ sudo a2enmod wsgi
15-	Install Postgres DB and its tools $ sudo apt-get install libpq-dev python-dev || and $ sudo apt-get install postgresql postgresql-contrib 
16-	Check on the DB by $ s udo cat /etc/postgresql/9.3/main/pg_hba.conf
17-	Login into the DB $ sudo su postgres || and psql  
18-	Create new user for name catalog2 $ create user catalog with password ‘password’
19-	Create DB name catalog $ CREATE DATABASE catalog WITH OWNER catalog
20-	Connect to the DB $ \c catalog2
21-	Revoke all right of public schema $ REVOKE ALL ON SCHEMA public FROM public;
22-	Make the permission only for catalog2 $ GRANT ALL ON SCHEMA public TO catalog2;
23-	Change the database connection in your application files as the following: engine = create_engine('postgresql://catalog:yourPassword@localhost/catalog')
24-	Requirements of flask dependencies:
a.	sudo pip install Flask
b.	sudo pip install requests
c.	sudo apt-get install python-pip
d.	sudo pip install httplib2 oauth2client sqlalchemy psycopg2 sqlalchemy_utils
25-	edit the vitural file sudo nano /etc/apache2/sites-available/000-default.conf
26-	create mod_wsgi. Into the directory of your application and edit it
	import sys
	import logging
	logging.basicConfig(stream=sys.stderr)
	sys.path.insert(0, "/var/www/catalog/..")

from appfilename import app as application
27-	restart apache2 $ sudo service apache2 restart
28-	if you face an issue try to clear caches in your browser beside using the following: 
29-	Clear pagecache $ echo 1 > /proc/sys/vm/drop_caches
30-	Clear dentries and inodes $ echo 2 > /proc/sys/vm/drop_caches
31-	Clear PageCache, dentries and inodes $ echo 3 > /proc/sys/vm/drop_caches
32-	Check the error logs of apachesudo tailf /var/log/apache2/error.log


