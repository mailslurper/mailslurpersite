#!/usr/bin/env bash

USER=mailslurperweb
GROUPNAME=web

apt-get update
apt-get install htop libcap2-bin

#
# Create user and group
#
adduser $USER
addgroup $GROUPNAME
adduser $USER $GROUPNAME

#
# Put root user in web group
#
usermod -a -G $GROUPNAME root

#
# Copy the Upstart job
#
cp ./mailslurpersite.conf /etc/init

#
# Setup a home for the application executeable
# and assets.
#
cd /

if [ ! -d "/web" ]; then
	mkdir web
fi

cd /web

if [ ! -d "/web/mailslurpersite" ]; then
	mkdir mailslurpersite
fi

#
# Update permissions
#
chown -R $USER:$GROUPNAME /web
