# Barcode Reader

A simple django application where you can add the barcode numbers and get 
complete details of the product and make a pdf containing the list of entered 
barcodes. 

## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/yashwanthkolli/barcode.git
$ cd barcode
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ virtualenv2 --no-site-packages env
$ source env/bin/activate
```

Then install the dependencies:

```sh
(env)$ pip install -r requirements.txt
```
Note the `(env)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `virtualenv2`.

Once `pip` has finished downloading the dependencies:
```sh
(env)$ python manage.py runserver
```
And navigate to `http://127.0.0.1:8000/`.

To setup the database, keep MySQL server running in port 3306. In `barc/settings.py` 
update your database schema name, username and password.

Prepare the migrations:
```sh
(env)$ python manage.py makemigrations
```

Then migrate the models to database:
```sh
(env)$ python manage.py migrate
```

## Walkthrough

Before you interact with the application, go to MySQL Workbench. In your schema, 
a new `sessions_barcode` table is created. Add barcode data with barcode number, 
item number, item name in the table.
Navigate to `http://127.0.0.1:8000/` and fill the session details and submit.
Add barcodes in the table to automatically update rest of the columns. Once all 
barcodes are add, click on `Generate PDF` to download a PDF of the entire session.


