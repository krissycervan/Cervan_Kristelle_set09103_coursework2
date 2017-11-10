#python flask
from flask import Flask, render_template, url_for, abort, request, redirect, g
import json
import models as dbHandler
app = Flask(__name__)
#"print" will allow to show it to the html page.
#"routes" are for mapping URLs to application actions, and conversely to generate URLs
#"def" define a function
# "with" Use file to refer to the file object
#"in" is used to look inside an object.
@app.route('/')
@app.route('/index')
def index():
#redirect to url 
 return render_template('index.html'), 200
@app.route('/about')
def about():
#redirect to url 
 return render_template('about.html'), 200
@app.route('/')
@app.route('/index')
@app.route('/login', methods=['GET', 'POST'])
def login():
 error = None
 if request.method == 'POST':
  username = request.form['username']
  password = request.form['password']
  completion = validate(username, password)
  if completion ==False:
   error = 'Invalid Credentials. Please try again.'
  else:
   return redirect(url_for('secret'))
 return render_template('login.html', error=error)

def validate(username, password):
 users = dbHandler.retrieveUsers()
 completion = False
 with con:
  cur = con.cursor()
  cur.execute("SELECT * FROM users")
  rows = cur.fetchall()
  for row in rows:
   dbUser = row[0]
   dbPass = row[1]
   if dbUser==username:
    completion=check_password(dbPass, password)
 return completion

@app.route('/register', methods=['GET', 'POST'])
def register():
 if request.method=='POST':
  username = request.form['username']
  password = request.form['password']
  dbHandler.insertUser(username, password)
  users = dbHandler.retrieveUsers()
#redirect to url 
  return render_template('login.html', users=username), 200
 else:
  return render_template('register.html'), 200
#Error Notice (wrong url)
@app.errorhandler (404)
def page_not_found(error):
 return " <h1><em>Sorry! <p>Couldn't find the page you requested.</p><em></h1>", 404


#This allows the app to run website on the browser
if __name__ == "__main__":
 app.run(host='0.0.0.0', debug=True)

