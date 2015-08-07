from __future__ import with_statement

import os

from fabric.api import env
from fabric.api import run
from fabric.api import local
from fabric.api import sudo
from fabric.operations import put
from fabric.colors import red
from fabric.colors import green
from fabric.colors import yellow

sudoUser = "root"
appUser = "mailslurperweb"
appGroup = "web"

def deploy():
	"""Deploys application"""

	env.user = sudoUser
	run("cd /code/go/src/github.com/mailslurper/mailslurpersite && git pull")
	run("cd /code/go/src/github.com/mailslurper/mailslurpersite && go get")
	run("cd /code/go/src/github.com/mailslurper/mailslurpersite && go build")

	run("cp /code/go/src/github.com/mailslurper/mailslurpersite/mailslurpersite /web/mailslurpersite")
	run("cp -fR /code/go/src/github.com/mailslurper/mailslurpersite/assets/* /web/mailslurpersite/assets")
	run("cp -fR /code/go/src/github.com/mailslurper/mailslurpersite/*.ico /web/mailslurpersite")
	run("cp -fR /code/go/src/github.com/mailslurper/mailslurpersite/*.html /web/mailslurpersite")

	run("chown %s:%s /web/mailslurpersite/mailslurpersite" % (appUser, appGroup,))
	run("chown %s:%s /web/mailslurpersite/*.ico" % (appUser, appGroup,))
	run("chown %s:%s /web/mailslurpersite/*.html" % (appUser, appGroup,))
	run("chown -R %s:%s /web/mailslurpersite/assets" % (appUser, appGroup,))

def stopService():
	"""Stops site service"""

	print(green("** Stopping service... **"))

	env.user = sudoUser
	run("service mailslurpersite stop")

def startService():
	"""Starts site service"""

	print(green("** Starting service... **"))

	env.user = sudoUser
	run("setcap 'cap_net_bind_service=+ep' /web/mailslurpersite/mailslurpersite")
	run("service mailslurpersite start")
