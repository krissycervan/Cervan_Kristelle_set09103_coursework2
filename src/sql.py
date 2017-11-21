import sqlite3 as sql
def insertRecipe(title, ingredients, instructions):
 con = sql.connect("var/veganrecipe.db")
 cur = con.cursor()
 cur.execute("INSERT INTO veganfood (title, ingredients, instructions) VALUES (?,?,?)", (title, ingredients, instructions))
 con.commit()
 con.close()
  