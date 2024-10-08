# TPojaghiWeb

Web application built around Flask.
Latest deployed version: https://tpojaghi.onrender.com/

## Tech

The project uses a number of packages to work properly:
- Flask
- Flask-Babel
- Swiper.js
- Bootstrap 5

## Installation

You'll need [Python 3.9](https://www.python.org/downloads/release/python-3913/) installed on your machine before setting up the project (other 3.x versions might work but haven't been tested).
Once you clone the repo in your machine, step into the directory, create a virtual environment and install the required dependencies:

```sh
python -m venv env
env\Scripts\activate
pip install -r requirements.txt
```

To start the web app, just run the following command within the same virtual env:

```sh
python app.py
```

The flask app should run locally through http://127.0.0.1:10000/