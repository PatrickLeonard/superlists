Provisioning a new site
=======================

## Required packages:
* nginx
* Python 3
* Git
* pip
* virtualenv

e.g.,, on Ubuntu:

	sudo apt-get update
	sudo apt-get install nginx git python3 python3-pip
	sudo pip3 install virtualenv

## Nginx Virtual Host Config
* see nginx.template.conf
* replace SITENAME with, e.g., staging.my-domain.com

## Systemd Service
* see gunicorn-systemd.template.service
* replace SITENAME with, e.g., staging-my-domain.com

## Folder Structure
Assume we have a user account at home/username

/home/username
|____sites
     |______SITENAME
           |____ database
	   |____ source
	   |____ static
	   |____ virtualenv



