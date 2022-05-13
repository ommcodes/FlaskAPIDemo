Demo Flask App
=================

Basic template to demo an API with Flask and MongoDB

## Technologies used

* **[Python3](https://www.python.org/downloads/)** - A programming language that lets you work more quickly.
* **[Flask](flask.pocoo.org/)** - A microframework for Python.
* **[Virtualenv](https://virtualenv.pypa.io/en/stable/)** - A tool to create isolated virtual environments
* **[MONGODB](https://www.mongodb.com/try/download/community/)** – offers a flexible document data model along with support for ad-hoc queries, secondary indexing, and real-time aggregations to provide powerful ways to access and analyze your data. 
* Minor dependencies can be found in the requirements.txt file on the root folder.

Usage
-----

Clone the repo:

    git clone https://github.com/ommcodes/FlaskAPIDemo
    cd FlaskAPIDemo

Create virtualenv:

    virtualenv venv
    source venv/bin/activate
    pip install -r requirements.txt
    python setup.py 

Run the sample server

    python runserver.py

start with the endpoints:

    curl -XGET http://localhost:5000/auth/register/
