#! /bin/bash
#================================================================================
# HANDLE PREREQUISITES / PRE-INSTALL CHECK
#================================================================================
postgres --version
sudo apt-get update -y
sudo apt-get install -y lsb-release
#================================================================================
# SETUP POSTGRES REPO
#================================================================================
# https://www.postgresql.org/docs/10/server-start.html
sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'
wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
sudo apt-get update
#================================================================================
# INSTALL POSTGRES
#================================================================================
sudo apt-get -y install postgresql
#================================================================================
# CONFIGURE POSTGRES / POST-INSTALL CHECK
#================================================================================
sudo pg_ctlcluster 13 main start
service postgresql restart
sudo -u postgres psql
# postgres -D /usr/local/var/postgres
# pg_ctl -D /usr/local/var/postgres -l /usr/local/var/postgres/server.log start
postgres --version
#================================================================================
# SETUP PG-ADMIN REPO
#================================================================================
# Install the public key for the repository (if not done previously):
sudo curl https://www.pgadmin.org/static/packages_pgadmin_org.pub | sudo apt-key add

# Create the repository configuration file:
sudo sh -c 'echo "deb https://ftp.postgresql.org/pub/pgadmin/pgadmin4/apt/$(lsb_release -cs) pgadmin4 main" > /etc/apt/sources.list.d/pgadmin4.list && apt update'
#================================================================================
# INSTALL PG-ADMIN
#================================================================================
# Install for both desktop and web modes:
sudo apt install pgadmin4 -y

# Install for desktop mode only:
# sudo apt install pgadmin4-desktop -y

# Install for web mode only: 
# sudo apt install pgadmin4-web -y
# Configure the webserver, if you installed pgadmin4-web:
# sudo /usr/pgadmin4/bin/setup-web.sh
#================================================================================
# CONFIGURE PG-ADMIN
#================================================================================
