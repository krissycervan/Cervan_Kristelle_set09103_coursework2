import sqlite3 as sql
#connect to database
#with sqlite3.connect("var/veganrecipe.db") as connection:
 #c = connection.cursor()
#delete if exists and create table 
 #c.execute("""DROP TABLE veganfood""")
 #c.execute("""CREATE TABLE veganfood(title text NOT NULL, ingredients text NOT NULL, instructions text NOT NULL)""")
 #recipes
 #c.execute("insert into veganfood (title, ingredients, instructions) values (?,?,?)", (title, ingredients, instructions))
 #c.execute('INSERT INTO veganfood VALUES("Vegan Alfredo Pasta", "4 ounces gluten-free uncooked spaghetti (120 g), 1 tsp extra virgin olive oil, 1 tsp extra virgin olive oil, 3/4 cup unsweetened almond milk (175 ml),1 cup raw cauliflower (100 g), chopped,Salt and ground black pepper to taste, 1 tbsp nutritional yeast, 1/2 tbsp lemon juice", " First cook the pasta al dente according to package directions. Heat the oil in a frying pan and cook the garlic over medium-high heat for about 3 to 4 minutes or until golden brown.Add the almond milk and bring it to a boil. Low the heat to medium-high, add the cauliflower, salt and pepper and cook for about 7 minutes or until the cauliflower is soft. Transfer to a blender and add the nutritional yeast and lemon juice. Blend until smooth. Drain the pasta and pour it into the pan with the sauce. Stir and serve (we added some dried oregano on top). Keep in a sealed container in the fridge for up to 4 days. ")')
 #c.execute('INSERT INTO veganfood VALUES("Apple Pie Oats", "3/4 cups oats, 1-2 tbsp maple syrup, 1 tbsp flax or chia seeds (optional), 1 cup non-dairy milk, 1/4 cup unsweetened apple sauce, 1/2 tsp cinnamon, 1/4 tsp vanilla extract (optional), 1/2 apple sliced into small pieces (optional)", "Add on ingredients (except for the apple slices) into a pretty mason jar that you probably paid too much money for and mix well together. Or be cheap, more environmentally friendly and awesome by reusing an old pasta sauce jar. Add apple slices on top and maybe a few sprinkles of oats to make it look pretty. Cover and refrigerate overnight.Eat it cold and straight out of the jar in the morning, or you can heat it up first.")')
 
def insertRecipe(title, ingredients, instructions):
 con = sql.connect("var/veganrecipe.db")
 cur = con.cursor()
 cur.execute("INSERT INTO veganfood (title, ingredients, instructions) VALUES (?,?,?)", (title, ingredients, instructions))
 con.commit()
 con.close()
  