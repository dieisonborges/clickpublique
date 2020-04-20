# To Create a New Project

## Install Python 3.8
> sudo apt install python3.8

## Create Virtual Enviroment
> python3.8  -m venv clickpublique.com/venv/

## Add Activate in .bashrc to facility your programming project
alias activate-ckp="source ~/python_apps/clickpublique.com/venv/bin/activate && cd ~/python_apps/clickpublique/"
alias deactivate-ckp="source ~/python_apps/clickpublique.com/venv/bin/deactivate && cd ~/python_apps/clickpublique/"

## Install Django (3.0.5)
> pip install django

## To verify enviroment
> pip freeze

## To Upgrade Pip
> pip install --upgrade pip

## Start Django Project
> django-admin startproject clickpublique

## Start New App in Django
> ./manage.py startapp core

## Install Decouple for create .env
> pip install decouple