# public-example-django
Simple django app for use in the docker-local-dev blog.  

Related repositories:
* [public-docker-local-dev](https://github.com/vidahealth/public-docker-local-dev) is the main repository for the local dev environment
* https://github.com/vidahealth/public-example-django (this respository) is the example main backend webserver service
* [public-example-microservice](https://github.com/vidahealth/public-example-microservice) is an example of a "microservice" that makes calls back to the main backend web service

#
```shell
pyenv virtualenv 3.9.7 example-django
pip install -r requirements.txt

django-admin startproject tutorial
cd tutorial
./manage.py startapp quickstart

```
Followed DRF quickstart
https://www.django-rest-framework.org/tutorial/quickstart/

# testing
when deployed with PyCharm
```shell
curl localhost:8000/status
```

# setting up database
We use the postgres admin account for simplicity, so we do not need
to create users or give permissions.


```shell
# migrate the database
./manage.py migrate
```

```shell
python manage.py createsuperuser
Username: admin
Email address: admin@example.com
Password: password
```

## differences from django tutorial
If we did not use the postgres admin user, we would need to create a new user
If we did, that might look like the following from local dev postgres (docker exec)
```shell
createuser --pwprompt mydatabaseuser
createdb mydatabase -O mydatabaseuser

# enable the test user to create test databases
psql -c "alter user mydatabaseuser createdb" -d mydatabase
```

if you forgot to set the password of the database user
```shell
psql -c "ALTER ROLE mydatabaseuser WITH PASSWORD 'mypassword'"
```
