# Meeting Organizer with Flask and SQLAlchemy

I tried to work on a single html page and did not use any Javascript. 

## How To Run
1. Install `virtualenv`:
```
$ pip install virtualenv
```

2. Open a terminal in the project root directory and run:
```
$ virtualenv env
```

3. Then run the command:
```
$ .\env\Scripts\activate
```

4. Then install the dependencies:
```
$ (env) pip install -r requirements.txt
```

5. Finally start the web server:
```
$ (env) python app.py
```

6. I used PostgreSQL as the database system. The config for postgres server can be found on app.py. You will need to change it to your username-password in order to connect your own postgresql server. 
7. The table name for meeting model is called "meetings". Also the database I created on my local machine was called flaskproject.
