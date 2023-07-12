# REMINDER APP

## Project Stack

| Name           | Version  |
|:--------------:|:--------:|
| Python         | 3.11     |
| Django         | 4.2.3    |
| Postgres       | 15       |
| Git            | 2.33     |


## Development Environment Configuration

### Clone the Django Project

The first thing you need to do is to install the project stacks on your system and then clone the repository.

### Python Env Setup

Create a virtual environment to install dependencies inside it and activate it.



#### [Poetry](https://python-poetry.org/docs/cli/#new)

__Install Poetry on Linux__

```sh
curl -sSL https://install.python-poetry.org | python3 -
```

__Install Poetry on Windows__

**TIP**: do bellow command on Powershell Administrator

```ps
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -
```

__Install Poetry on Macos__

```sh
brew install poetry
```
__CONFIG__

1) To installing the config build env in the program directory

```sh
# Creates the address of the .env folder in the program directory, It is null by default
poetry config virtualenvs.in-project true
# The address of the .env folder
poetry config virtualenvs.path .
```


2) To install all packages with poetry that is documented in `poetry.lock` do bellow command:

```sh
poetry install
```

3) To activate poetry environment:

```sh
poetry shell
```

## Prepare Settings

### Django Configuration
Transfer the __settings-template.toml__ file from the __configs/settings__ folder to the base directory

Then change its name in the settings.toml

These are sample settings only for fast startup, you need to change it later

1) Config Database in Django by `settings.toml` For example:

Just change these two keys

```toml
[settings.django]

DEBUG=true
ALLOWED_HOSTS="localhost,127.0.0.1"
SECRET_KEY="e2JOV6YfyPmcM1IxoK9LX4FAzPCRyA2MfyPmcM1IxoK9LXRL"

[settings.database]

DB_NAME="reminder_db"
DB_USER="reminder_user"
DB_PASSWORD="LTMC46Y4FAzPCRyA2MRLnqfyPmcM1IxoK9LX2IHLstw"
DB_HOST="localhost"
DB_PORT="5432"
DB_TEST="reminder_user_test"
```

2) Create a Database in PSQL
 
Enter the terminal page, Connect to `psql`

```sh
CREATE DATABASE reminder_db;

CREATE USER reminder_user WITH PASSWORD'LTMC46Y4FAzPCRyA2MRLnqfyPmcM1IxoK9LX2IHLstw';

ALTER ROLE reminder_user SET client_encoding TO 'utf8';

ALTER ROLE reminder_user SET default_transaction_isolation TO 'read committed';

ALTER ROLE reminder_user SET timezone TO 'UTC';

ALTER USER reminder_user CREATEDB;

ALTER USER reminder_user LOGIN;

ALTER DATABASE reminder_db OWNER TO reminder_user;

ALTER ROLE reminder_user WITH CREATEDB;

GRANT ALL PRIVILEGES ON DATABASE reminder_db TO reminder_user;


# If you encounter a database error, execute these commands, otherwise there is no need
\c reminder_db
grant usage on schema public to reminder_user;`
grant create on schema public to reminder_user;`

```


3) Create migration  in virtual environment activate

```py
python3 manage.py makemigrations
python3 manage.py migrate
```

4) Create user for admin

```py
python3 manage.py createsuperuser
```

#### Run Project

You can now run the app:

```sh
python3 manage.py runserver
```
