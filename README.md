Hivemind Powerball
=====================
Store drones' favorite powerball numbers and generate a composite number based on the most frequently selected values.

## Installation and Setup
After cloning this repo, you'll need to decide how you'd like to run the application.  The easiest way is probably 
to follow the steps described in the `Running the containerized app` section.

If you don't want to deal with docker, you can follow the steps described in `Running the app locally`.  It's only 
slightly more work.  The hardest part is likely setting up your postgres user and database if you haven't done it before.

## Running the containerized app
####Host Requirements
* docker
* docker-compose

####Steps
Start the containers:
```bash
$ docker-compose up
```

Open a browser and navigate to [http://127.0.0.1:8000/](http://127.0.0.1:8000/):
```bash
$ open http://127.0.0.1:8000/
```

To stop the app, hit `ctrl-c` then type:
```
$ docker-compose down
```

## Running the app locally
####System Requirements
* PostgreSQL
* Python3

####Steps
create a new python3 virtual environment (if you aren't using `virtualenvwrapper` your commands will differ)
```bash
$ mkvirtualenv -p python3 <envname>
```

install the project requirements
```bash
$ pip install -r requirements/local.txt
```

create a postgres role and database locally (you can use different names, just make sure you edit `config/settings/local.py` to match)
```sql
$ psql
psql (9.6.1)
Type "help" for help.

user=# CREATE USER overmind WITH CREATEDB PASSWORD '0b3y!';
CREATE ROLE
user=# CREATE DATABASE hivemind_powerball OWNER overmind;
CREATE DATABASE
user=# \q
```

run the database migrations using the `local` settings
```bash
$ cd hivemind_powerball
$ python manage.py migrate --settings=config.settings.local
```

run the server using the `local` settings
```bash
$ cd hivemind_powerball
$ python manage.py runserver --settings=config.settings.local
```

Open a browser and navigate to [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
```bash
$ open http://127.0.0.1:8000/
```

When you're finished, type `ctrl-c`

####Useful Local Commands
Running the unit tests
```bash
$ cd hivemind_powerball
$ python manage.py test --settings=config.settings.local
$ python manage.py test -v 2 --settings=config.settings.local
```

Generating Test Coverage
```bash
$ cd hivemind_powerball
$ coverage run manage.py test --settings=config.settings.local
$ coverage html --omit="admin.py" && open cov_report/index.html
```

Connect to project database
```bash
$ cd hivemind_powerball
$ python manage.py dbshell --settings=config.settings.local
```

##Running the Functional Tests
**NOTE: Due to a change in firefox, the functional tests no longer launch a browser.  While I haven't figured out a workaround, I decided to leave the incomplete test in place.**

####System Requirements
* firefox
* geckodriver

####Steps
As of Firefox 47.0 selenium expects the geckodriver to be on your system path.  [Installation varies](https://stackoverflow.com/questions/37761668/cant-open-browser-with-selenium-after-firefox-update/37765661#37765661).  On Mac using homebrew run:
```bash
$ brew install geckodriver
```

Next start the development server using either the docker command:
```bash
$ docker-compose up
```

Or the local command:
```bash
$ python manage.py runserver --settings=config.settings.local
```

Then run the functional tests (incomplete):
```bash
$ cd hivemind_powerball
$ python functional_tests.py
```
