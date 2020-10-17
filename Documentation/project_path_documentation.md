# Audiobooks Digital store Project
---

Books and Audiobooks store project made with django,

1. ### Create a python virtual environment for the project. (on windows)
   * lets name the local environment Ab-local
     ```bash
     python -m venv Ab-local
     ```
   * To activate, run the script on windows terminal
     ```bash
     Ab-local\Scripts\activate.bat
     ```
     On git-bash or linux
     ```bash
     # cd to Ab-local\Scripts, then run
     . activate
     ```
   * To deactivate, just type deactivate with environment active
     ```bash
     deactivate
     ```
2. ### To update, install pip, python..etc
   * In linux,

      ```bash
      # For a specific version
      sudo apt-get install python 3.8.3

      # To get pip
      pip --version
      sudo apt install python3-pip

      # To install requirements.txt
      pip install -r requirements.txt
      ```
   * Install required packages with `pip install`

   * To Show all the packages installed,

      ```bash
      pip freeze

      # To create a requirements.txt with current files
      pip freeze > requirements.txt
      ```
   * Use the [gitignore.io](https://www.toptal.com/developers/gitignore) to setup `.gitignore` file, also add the local environment folder to gitignore, (only need the requirements.txt in github)

   * Basic things needed in the `requirements.txt`
      ```txt
      Django>=3.1,<3.2.0

      flake8>=3.8.0,<3.8.3
      psycopg2>=2.8.5,<2.9.0
      Pillow>=7.2.0,<7.3.0
      ```
3. ### Django Help

   * To get help with Django commands
     ```bash
     django-admin --help

     # manage.py commands
     python manage.py help
     ```
5. ## Django Project initialization
   ---
   1. To start a django project, Project name: digibook_store
   ```python
    django-admin startproject digibook_store .
   ```
   2. To see the basic boilerplate run the localserver, go to localaddress to see the page, `127.0.0.1:8000`
   ```python
    python manage.py runserver 0.0.0.0:8000
   ```
   3. To start a new app, create a main app for the models (set the User model if needed)
   ```python
    python manage.py startapp <app_name>
   ```
6. ## Django basic `settings.py` settings
    1. Add the created apps to the `settings.py`, `INSTALLED_APPS` (add the postgres too,)
         ```python
         INSTALLED_APPS = [
             'django.contrib.admin',
             'django.contrib.auth',
             'django.contrib.contenttypes',
             'django.contrib.sessions',
             'django.contrib.messages',
             'django.contrib.staticfiles',
             'django.contrib.postgres',
             '<app_name'>
         ]
         ```

    2. Setting up the **"template"** directory, setting it in the root, then inside each apps templates go\
    specify django where to look for those html templates,
         ```python
          TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')

          # specify in the TEMPLATES LIST
         TEMPLATES = [
             {
                 'BACKEND': 'django.template.backends.django.DjangoTemplates',
                 'DIRS': [TEMPLATE_DIR],
                 'APP_DIRS': True,
                 'OPTIONS': {
                     'context_processors': [
                         'django.template.context_processors.debug',
                         'django.template.context_processors.request',
                         'django.contrib.auth.context_processors.auth',
                         'django.contrib.messages.context_processors.messages',
                     ],
                 },
             },
         ]
         ```
    3. Set the STATIC FILES directory (all the css, javascript, images go there).
        ```python
         STATIC_ROOT = os.path.join(BASE_DIR, 'static')
         STATIC_URL = '/static/'

         STATICFILES_DIRS = [
            os.path.join(BASE_DIR, 'app/static')
         ]
        ```
        So the static directory also setup in the root,\
        But the django admin static files are on another directory, to set all of them together\
        Also instead of every time adding static files directly to that(like only the compiled css and js)\
        can use the `python manage.py collectstatic` to grab all static files from `\static\` into the root\

        Now the STATIC_ROOT contains, all our custom static folders and files, also the admin css, js files\
        when it is deploying the static files taken from this root.

    4. Also set up media directory (only if needed),
        ```python
         # Tells django where to look and store media.
         MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

         MEDIA_URL = '/media/'
        ```
7. ## Postgress installation and setup local, and integration with django
   ---

   * Install `pscopg2` using pip.
   * Install postgress locally, GUI pgadmin also comes with it.
   * The default user is "postgres", it is OK for the development-local, change in production.
   * Open postgres with the default user, To set password for user `postgres` use `\PASSWORD postgres` basic postgres commands,

     ```sql
     /* for basic help */
     psql --help
     /* list available DB's */
     psql --list
     /* To know version */
     psql --version

     /* To get into account, username default postgres */
     psql -U <username>
     ```

   * Also listing commands, `\dt`(list tables), `\du`(list users), `\l`(list databases),\
   `\d`(list table), `\c`(connect to), to quit from psql use `\q`.
     ```sql
     /* Connect to a database */
     \c <db_name>
     ```

   * Basic database commands
     ```sql
     /* Creating a database */
     CREATE DATABASE <name>;
     /* Creating a table (eg) */
     CREATE TABLE <name> (
       id BIGSERIAL NOT NULL PRIMARY KEY,
       first_name VARCHAR(50) NOT NULL,
       last_name VARCHAR(50) NOT NULL,
       date_of_birth DATE NOT NULL
     );
     /* basically "column_name" + "data_type" + "constraints" , if any
     /* insert into table for eg.*/
     INSERT INTO <table-name> (
       first_name,
       last_name,
       date_of_birth
     ) VALUES ('John', 'Philip', DATE '1995-01-24');
     /* Show table */
     SELECT * FROM <table_name>;
     /* others */
     /* Use "WHERE", "AND", "IN", "BETWEEN", "LIKE", "ILIKE" etc for sorting,*/
     ```
   * With django, dont need to run any database control commands, Django ORM, got it all covered, can do all
   CRUD operations with Django models.

   * Only need to create a database for our app, do that with `CREATE DATABASE Abdmdb;`, so "Abdmdb" is the database for our app.

   * Setup **pgadmin**, to visualize the data,
     * First create a server(local, pgadmin is a browser based tool), in the opened app, use any `name`,\
     set `host` to `localhost`, also ther username(`postgres`) and the password.
     * Grant all privileges to the user(postgres), in settings-> db-> privileges -> all

   * Configure Django to use on postgres, on django settings.py,

      ```python
       DATABASES = {
          'default': {
              'ENGINE': 'django.db.backends.postgresql',
              'NAME': 'Abdmdb', # The db name given
              'USER': 'postgres',
              'PASSWORD': '<password>',
              'HOST': 'localhost',
              'PORT': '5432', # default postgres port is 5432
          }
        }
      ```
      Now the django, postgres integration completed.

8. ### Creating custom user model in Django,(IMPORTANT: MUST DO BEFORE FIRST MIGRATION)
    * Django comes in with a pre-built [user model](https://docs.djangoproject.com/en/3.1/ref/contrib/auth/), with username, first_name, last_name, email and password.
    * If one need to don't use this model,(like, needs email instead of username), needs to create a custom user model, refer it in `settings.py` before the initial migration.
    ```python
    AUTH_USER_MODEL = '<app>.User'
