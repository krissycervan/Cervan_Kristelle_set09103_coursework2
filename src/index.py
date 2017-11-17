#python flask
from flask import Flask, render_template, url_for, abort, request, redirect, g
from flask import *
from functools import wraps
import sqlite3
app = Flask(__name__)
app.secret_key = 'hello123'
app.database = 'var/vegan.db'

# -*- coding: utf-8 -*-

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
 
 
@app.route('/')
@app.route('/about')
def about():
#redirect to url 
 return render_template('about.html'), 200
@app.route('/')
@app.route('/Recipes')
def recipes():
#redirect to url 
 return render_template('recipes.html'), 200
 
 
#asks the user that login is required

def login_required(test):
 @wraps(test)
 def wrap(*args, **kwargs):
  if 'logged_in' in session:
   return test(*args, **kwargs)
  else:
   flash('login required')
   return redirect(url_for('login'))
 return wrap
 
#logout 
@app.route('/logout')
def logout():
 session.pop('logged_in', None)
 flash('You are now logged out!')
 return redirect(url_for('login'))
 
 
def connect_db():
 return sqlite3.connect(app.database) 

@app.route('/hello', methods=['GET','POST'])
@login_required
def hello():
 if request.method == 'POST':
  title = request.form['title'] 
  ingredients = request.form['ingredients']
  instructions = request.form['instructions']
  g.db = connect_db()
  cur = g.db.execute("insert into veganfood values(NOT NULL,?,?,?, NOT NULL)", (title, ingredients, instructions))
  g.db.close()
  
 g.db = connect_db()
 cur = g.db.execute("select * from categories, veganfood where veganfood.category_id='categories.category_id'")
 category = [dict(category_id=row[0], category_name=row[1]) for row in cur.fetchall()]
 g.db.close()

 g.db = connect_db()
 cur = g.db.execute("select * from veganfood where title='Vegan Alfredo Pasta'")
 veganfood = [dict(title=row[1], ingredients=row[2], instructions=row[3]) for row in cur.fetchall()]
 g.db.close()
 return render_template('hello.html', veganfood=veganfood, category=category)

#login with sessions
@app.route('/login', methods=['GET', 'POST'])
def login():
 error = None
 if request.method == 'POST':
  if request.form['username'] != 'admin' or request.form['password'] != 'admin': 
   error = 'Invalid login'
  else:
   session['logged_in'] = True
   return redirect(url_for('hello'))
 return render_template('login.html', error=error)

#url redirects
@app.route('/')
@app.route('/breakfasts')
def breakfast():
#redirect to url 
 return render_template('breakfasts.html'), 200

@app.route('/')
@app.route('/mains')
def mains():
#redirect to url 
 return render_template('mains.html'), 200
 
@app.route('/')
@app.route('/desserts')
def desserts():
 #redirect to url 
 return render_template('desserts.html'), 200
 
@app.route('/')
@app.route('/sides')
def sides():
#redirect to url 
 return render_template('sides.html'), 200

#Error Notice (wrong url)
@app.errorhandler (404)
def page_not_found(error):
 return " <h1><em>Sorry! <p>Couldn't find the page you requested.</p><em></h1>", 404

#This allows the app to run website on the browser
if __name__ == "__main__":
 app.run(host='0.0.0.0', debug=True)

