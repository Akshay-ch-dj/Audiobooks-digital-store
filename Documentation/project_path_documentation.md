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
      Django>=3.1.2,<3.2.0

      flake8>=3.8.4,<3.9.0
      psycopg2>=2.8.6,<2.9.0
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
   1. To start a django project, Project name: digibook_store in the current folder.
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
             '<app_name>',
         ]
         ```

    2. Setting up the **"template"** directory, setting it in the root, then inside each apps templates go\
    specify django where to look for those html templates,
    IMP: This settings changes in new django 3.1.
    * The old django 3.0, that uses os.path.join, (joining strings of paths, BASE_DIR set is a string)
    * From version 3.1, it uses pathlib.path function, now it is easier to chain paths,
         ```python
          TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates') # only for older
          # From django 3.1 -
          # BASE_DIR = Path(__file__).resolve().parent.parent (set already)
          TEMPLATE DIR = BASE_DIR/'templates'
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
        * As from django 3.1, it is recommended to keep the template files separated in their respective app folders,\
          giving a more modular nature to it

    3. Set the STATIC FILES directory (all the css, javascript, images go there).
        ```python
         STATIC_ROOT = os.path.join(BASE_DIR, 'static') # only up to django 3.0
         STATIC_ROOT = BASE_DIR/'static'
         STATIC_URL = '/static/'

         STATICFILES_DIRS = [
            os.path.join(BASE_DIR, 'app/static') # only up to django 3.0
            BASE_DIR/'app/static'
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
   * **TIP**: Use the `\! clear`, to clear the screen, or use `\!` to use any system commands inside postgres, terminal\
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

   * Only need to create a database for our app, do that with `CREATE DATABASE ab_db;`, so "ab_db" is the database for our app.

   * Setup **pgadmin**, to visualize the data,
     * First create a server(local, pgadmin is a browser based tool), in the opened app, use any `name`,\
     set `host` to `localhost`, also ther username(`postgres`) and the password.
     * Grant all privileges to the user(postgres), in settings-> db-> privileges -> all

   * Configure Django to use on postgres, on django settings.py,

      ```python
       DATABASES = {
          'default': {
              'ENGINE': 'django.db.backends.postgresql',
              'NAME': 'ab_db', # The db name given
              'USER': 'postgres',
              'PASSWORD': '<password>',
              'HOST': 'localhost',
              'PORT': '5432', # default postgres port is 5432
          }
        }
      ```
      Now the django, postgres integration completed.
    * TIP: To use only the server when needed in windows machine, run(windows + R) the `services.msc`
      then start/stop the postgress server(here: postgressql-x64-13) as per the need,

8. ### Creating custom user model in Django,(IMPORTANT: MUST DO BEFORE FIRST MIGRATION)
    * Django comes in with a pre-built [user model](https://docs.djangoproject.com/en/3.1/ref/contrib/auth/), with username, first_name, last_name, email and password.
    * If one need to don't use this model,(like, needs email instead of username), needs to create a custom user model, refer it in `settings.py` before the initial migration.
    ```python
    AUTH_USER_MODEL = '<app_name>.User'

9. ### Adding templates and styling (prototype phase)
   * Using Semantic UI and, Using bootstrap 5 alpha 2(just cz it is a prototype, and simple also to learn it)
   * Adding bootstrap 5 alpha 3, refer to [my own notes](https://github.com/Akshay-ch-dj/CSS-Responsive-layouts-projects/blob/main/Bootsrap_practice/Bootstrap%205%20learn/Bootstrap5.md).
   * The static files added in a static folder inside the project folder (which not added to the main repo or deployment)
   ```python
   static--|_css------|_admin.css
           |          |_font awesome
           |          |_bootstrap.css
           |          |_style.css(custom)
           |
           |_js ---------|_bootstrap.js
           |_img         |_main.js
           |_webfonts
   ```
   * Then the [collectstatic](https://docs.djangoproject.com/en/3.1/howto/static-files/#deployment) is used to bring all the static files to main `static` folder in the root.
   * Using `{% load static %}` links the bootstrap css, js and local css, js to the `base.html`
   * The `base.html` created directly in the root templates folder that also contains, the partials folder.
   * Use the `{% include 'partials/<item>' %}`, jinja to include the partials in any template.
   * The index, login etc all gets [extended](https://docs.djangoproject.com/en/3.0/ref/templates/language/#template-inheritance) from it.
   * To add `static` in the root to gitignore use `\static\`.
   * Add VS code extension for Django by *Baptiste Darthenay*, for the ese of typing and color highlighting of django template language.

* Bootsrap dark themed navbar added in the partials,
* Seperated title (in the head tag for each page with `<title>{% block title %} {% endblock title %}</title>`.

### Creating admin and accessing superuser

---

1. Create [superuser](https://docs.djangoproject.com/en/3.1/topics/auth/default/#creating-superusers), `python manage.py createsuperuser`.
2. Before that it needed to change the settings to use postgresql as mentioned previously.
3. u-name: akshay.dev, aks.dev@, digibooks.1
4. For pgadmin like interface for sqlite(it did'nt store data to servers instead in a single `db.sqlite3` file). Go to [sqliteonline](https://sqliteonline.com/) and put that file in to examinte the sqlite db structure.
5. Enter admin area (/admin/), login with the superuser password. (enable cookies to login)

## MODELS IN THE PROJECT

---

* Eg of creating a simple django model,

  ```python
  from django.db import models
  # Create your models here.
  class Book(models.Model):
      name = models.CharField(max_length=80)
      pages = models.IntegerField()
  ```

* Look the django [documentation](https://docs.djangoproject.com/en/3.1/intro/tutorial02/#creating-models) for more info about models.
* Change your models (in models.py).
* Run python manage.py makemigrations to create migrations for those changes
* Run python manage.py migrate to apply those changes to the database.
* TIP: Use `python manage.py check`, python manage.py check this checks for any problems in your project without making migrations or touching the database.
* Models are created in bookshop app in a separate python package("model" folder with `__init__.py`), not all of them created in a single `models.py`, aids the modular nature
* Setup the django dev environment in VScode with Django snippets, AREPL, Python doc strings etc.

### 1. Book Model

---

1. id - auto increment id for the Book Table for DB.

    * Data type "int".
    * id - INT (serial int later if needed into other more secure uuid or something)
      (Django creates an id field automatically)

2. Need to connect author to book model - An author who is posting the book.

     * Book and author table can be connected using a FOREIGN KEY
     * author INT (FOREIGN KEY [From author table])
       (The entire author is connected to the book- can attach name, details, image from author table/db to the book listing.)

3. title - STR (MODEL-PRICE) - Title of the book,
4. description - TEXT

5. price - INT (req)
6. Discount - INT (req)

7. genre - STR (Dropdown different genres UI element(admin))

8. Listing Date(list_date) - DATE (auto fetch)
9. File path (for small files or books):
10. File link (for large files and audio books):

11. is_published - BOOL (def: True) (the produced set to be published by default)
12. thumbnail - (image)

### 2. BookImages Model

To add image of the book added as an inline field.
Image 1
Image 2
...
Can have as many images as user needed.

* Book, BookImages model created-> migrated and registered in, admin.
* Now it needed to get the foreign key related imagefield to the same page of book in the admin area.
* So need to customize the admin, admin customized, the Book Images added as inline
* In order to make link or file upload necessary, a clean validation is added in the model
* Need to add the description to list view and it need to be short, show its full form only when it is hovered over with mouse.\
With the use of format_html utility class from django description is added as a html element with title as full item, so when hovered it is gonna displayed fully.
