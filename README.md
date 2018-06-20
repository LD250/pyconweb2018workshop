Database queries optimization workshop.
=======================================

Requirements
------------
- python3.5/3.6
- mysql5.7/sqlite

Setup
-----

1. Install Requirements.
`pip install -r requirements/dev.txt`

1. install MySQL

    * If you have docker and docker compose, you can use
`docker-compose up`

    * If you have sqlite, you can change settings in `mysite/settings.py`

    * To check that everything ok, run `./manage.py showmigrations`

1. Run migrations
`./manage.py migrate`

1. Create superuser
`./manage.py createsuperuser`


Additional setup information
----------------------------

[Install python environment](http://docs.python-guide.org/en/latest/dev/virtualenvs/)

[Docker](https://www.docker.com/get-docker)

[Install MySQL Ubuntu](https://www.digitalocean.com/community/tutorials/how-to-install-mysql-on-ubuntu-16-04)

[Install MySQL Mac](https://gist.github.com/nrollr/3f57fc15ded7dddddcc4e82fe137b58e)
