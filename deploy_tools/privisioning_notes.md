## Required Packages:
* nginx
* Python
* Git
* pip
* virtualenv

e.g. on Ubuntu:
    sudo apt-get install nginx git python python-pip
    sudo apt-get install virtualenv

## Nginx Virtual Host Config
* see nginx.template.conf
* replace SITENAME with, e.g., staging.domain.com

## Upstart job
* see gunicorn-upstart.template.conf
* replace SITENAME with, e.g., staging.domain.com

## Folder structure
Assuming user account at /home/ubuntu

└── sites
    └── SITENAME
        ├── database
        ├── source
        ├── static
        └── virtualenv

