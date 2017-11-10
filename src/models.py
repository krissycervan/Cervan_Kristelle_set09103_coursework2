import sqlite3 as sql

def insertUser(username,password):
 con = sql.connect("database.db")
 cursor = con.cursor()
 cursor.execute("INSERT INTO users(username,password) VALUES (?,?)", (username,password,))
 con.commit()
 con.close()

def retrieveUsers():
 con = sql.connect("database.db")
 cursor = con.cursor()
 cursor.execute("SELECT username FROM users WHERE userid=?", (userid))
 users = cursor.fetchall()
 con.close()
 return users
