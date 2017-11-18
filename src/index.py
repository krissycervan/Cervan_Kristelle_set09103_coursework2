#python flask
from flask import Flask, render_template, url_for, abort, request, redirect, g
from flask import *
from functools import wraps
import sqlite3
import sql as dbHandler
app = Flask(__name__)
app.secret_key = 'hello123'
app.database = 'var/veganrecipe.db'

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

@app.route('/account', methods=['GET','POST'])
@login_required
def account():
 if request.method == 'POST':
  title = request.form['title'] 
  ingredients = request.form['ingredients']
  instructions = request.form['instructions']
  dbHandler.insertRecipe(title, ingredients, instructions)
  
 g.db = connect_db()
 cur = g.db.execute("select * from veganfood")
 veganfood = [dict(title=row[0], ingredients=row[1], instructions=row[2]) for row in cur.fetchall()]
 g.db.close()
  

 return render_template('hello.html', veganfood=veganfood)


 

#login with sessions
@app.route('/login', methods=['GET', 'POST'])
def login():
 error = None
 if request.method == 'POST':
  if request.form['username'] != 'admin' or request.form['password'] != 'admin': 
   error = 'Invalid login'
  else:
   session['logged_in'] = True
   return redirect(url_for('account'))
 return render_template('login.html', error=error)

 
 
 
#BREAKFASTS
#url redirects
@app.route('/')
@app.route('/breakfasts')
def breakfast():
#redirect to url 
 return render_template('breakfasts.html'), 200
 
@app.route('/')
@app.route('/breakfasts')
@app.route('/breakfasts/tofuscrambledegg')
def tofuscrambledegg():
#get recipe from database based on title and display to url
 g.db = connect_db()
 cur = g.db.execute("select * from veganfood where title='Tofu Scrambled Egg'")
 veganfood = [dict(title=row[0], ingredients=row[1], instructions=row[2]) for row in cur.fetchall()]
 g.db.close()
 return render_template('tofu.html', veganfood=veganfood), 200
@app.route('/')
@app.route('/breakfasts')
@app.route('/breakfasts/applepieoats')
def applepieoats():
#get recipe from database based on title and display to url
 g.db = connect_db()
 cur = g.db.execute("select * from veganfood where title='Apple Pie Oats'")
 veganfood = [dict(title=row[0], ingredients=row[1], instructions=row[2]) for row in cur.fetchall()]
 g.db.close()

 return render_template('applepieoats.html', veganfood=veganfood), 200
 
@app.route('/')
@app.route('/breakfasts')
@app.route('/breakfasts/bruschetta')
def bruschetta():
#get recipe from database based on title and display to url
 g.db = connect_db()
 cur = g.db.execute("select * from veganfood where title='Easy Bruschetta'")
 veganfood = [dict(title=row[0], ingredients=row[1], instructions=row[2]) for row in cur.fetchall()]
 g.db.close()
 return render_template('mugcake.html', veganfood=veganfood), 200
 
 
@app.route('/')
@app.route('/breakfasts')
@app.route('/breakfasts/frenchtoast')
def frenchtoast():
#get recipe from database based on title and display to url
 g.db = connect_db()
 cur = g.db.execute("select * from veganfood where title='French Toast'")
 veganfood = [dict(title=row[0], ingredients=row[1], instructions=row[2]) for row in cur.fetchall()]
 g.db.close()
 return render_template('mugcake.html', veganfood=veganfood), 200
 
 
 
 
 
 
 #MAINS 

@app.route('/')
@app.route('/mains')
def mains():
#redirect to url 
 return render_template('mains.html'), 200
 
@app.route('/')
@app.route('/mains')
@app.route('/mains/alfredo')
def alfredo():
#get recipe from database based on title and display to url
 g.db = connect_db()
 cur = g.db.execute("select * from veganfood where title='Vegan Alfredo Pasta'")
 veganfood = [dict(title=row[0], ingredients=row[1], instructions=row[2]) for row in cur.fetchall()]
 g.db.close()
 return render_template('alfredopasta.html', veganfood=veganfood), 200

 
@app.route('/')
@app.route('/mains')
@app.route('/mains/greencurry')
def greencurry():
#get recipe from database based on title and display to url
 g.db = connect_db()
 cur = g.db.execute("select * from veganfood where title='Sweet Potato Green Curry'")
 veganfood = [dict(title=row[0], ingredients=row[1], instructions=row[2]) for row in cur.fetchall()]
 g.db.close()
 return render_template('greencurry.html', veganfood=veganfood), 200

 
@app.route('/')
@app.route('/mains')
@app.route('/mains/stirfry')
def stirfry():
#get recipe from database based on title and display to url
 g.db = connect_db()
 cur = g.db.execute("select * from veganfood where title='Peanut Teriyaki Stir Fry'")
 veganfood = [dict(title=row[0], ingredients=row[1], instructions=row[2]) for row in cur.fetchall()]
 g.db.close()
 return render_template('stirfry.html', veganfood=veganfood), 200
 
 
@app.route('/')
@app.route('/mains')
@app.route('/mains/pumpkinpasta')
def pumpkinpasta():
#get recipe from database based on title and display to url
 g.db = connect_db()
 cur = g.db.execute("select * from veganfood where title='Creamy Pumpkin Pasta'")
 veganfood = [dict(title=row[0], ingredients=row[1], instructions=row[2]) for row in cur.fetchall()]
 g.db.close()
 return render_template('pumpkinpasta.html', veganfood=veganfood), 200


 
#SIDES













 
#DESSERTS
 
 
@app.route('/')
@app.route('/desserts')
def desserts():
 #redirect to url 
 return render_template('desserts.html'), 200
 
@app.route('/')
@app.route('/desserts')
@app.route('/desserts/mugcake')
def peanutbuttermugcake():
#get recipe from database based on title and display to url
 g.db = connect_db()
 cur = g.db.execute("select * from veganfood where title='Peanut Butter Mug Cake'")
 veganfood = [dict(title=row[0], ingredients=row[1], instructions=row[2]) for row in cur.fetchall()]
 g.db.close()
 return render_template('mugcake.html', veganfood=veganfood), 200
 
@app.route('/delete', methods=['POST'])
def delete_recipe():
   g.db = connect_db()
   g.db.execute('delete from veganfood where rowid =?')
   veganfood = [dict(title=row[0], ingredients=row[1], instructions=row[2]) for row in cur.fetchall()]
   g.db.close()
   return render_template('hello.html', veganfood=veganfood)
 
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

