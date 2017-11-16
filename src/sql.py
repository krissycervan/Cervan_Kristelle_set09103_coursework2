import sqlite3

with sqlite3.connect("var/vegan.db") as connection:
 c = connection.cursor()

 c.execute("""DROP TABLE veganfood""")
 c.execute("""CREATE TABLE veganfood(veganfood_id integer PRIMARY KEY, title text NOT NULL, ingredients text NOT NULL, instructions text NOT NULL, category_id integer NOT NULL, FOREIGN KEY (category_id) REFERENCES categories(category_id))""")
 c.execute('INSERT INTO veganfood VALUES(NOT NULL,"Vegan Alfredo Pasta", "cashew nuts", "cook", "2")')


 c.execute("""DROP TABLE categories""")
 c.execute("""CREATE TABLE categories(category_id integer PRIMARY KEY, category_name text NOT NULL)""")
 c.execute('INSERT INTO categories VALUES(NOT NULL, "Breakfast")')
 c.execute('INSERT INTO categories VALUES(NOT NULL, "Mains")')
 c.execute('INSERT INTO categories VALUES(NOT NULL, "Desserts")')
 c.execute('INSERT INTO categories VALUES(NOT NULL, "Sides")')