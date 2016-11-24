# flask-microblog

This is a microblog site which is based on a tutorial for begineers. It also have sqlalchemy events to send data to a target url.

## Installation:

Assuming you have python installed on your system.

### 1. Setup Virtual Environment
For [virtualenv](http://pypi.python.org/pypi/virtualenv) follow instructions at: *http://pypi.python.org/pypi/virtualenv*
```sh
sudo pip install -U pip
sudo pip install virtualenv
```

### 2. Get the latest source code
```sh
git clone *******

```

### 3. Create and Activate Virtual Environment (in your desired directory)
```sh
virtualenv -p python3 env
source env/bin/activate
```

### 4. Install the requirements
```sh
pip install -r requirements
```

###5. Run migrations
```sh
export FLASK_APP=app/__init__.py
flask db upgrade
```

###6. Run the server
```sh
python run.py
```

Open http://localhost:5000/ in the browser and explore.
