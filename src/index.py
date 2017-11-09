#python flask
from flask import Flask, render_template, url_for, abort, request
import json
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
@app.route('/tops')
def tops():
#redirect to url 
 return render_template('tops.html'), 200
 
@app.route('/tops')
@app.route('/tops/floral')
def tops_floral():
 clothes = [] #this refers json file  array objects 

 with open('static/js/fashion.json', 'r') as f:  # Use file to refer to the file object
     clothes = json.load(f)
     f.close()

 p = {} #this refers to the objects in the json file
 for item in clothes:
     if item['name'] == "Black Floral Top":
       print item
       p = item
#redirect to url 
 return render_template('blackfloral.html', blackfloral=p), 200
 
@app.route('/tops')
@app.route('/tops/croptop')
def tops_croptop():
 clothes = [] 
 with open('static/js/fashion.json', 'r') as f: 
     clothes = json.load(f)
     f.close()

 p = {}
 for item in clothes:
     if item['name'] == "Stripes Croptop":
       print item
       p = item
#redirect to url 
 return render_template('croptop.html', croptop=p), 200
 
@app.route('/tops')
@app.route('/tops/chokersweater')
def tops_chokersweater():
 clothes = []
 with open('static/js/fashion.json', 'r') as f:
     clothes = json.load(f)
     f.close()

 p = {}
 for item in clothes:
     if item['name'] == "Purple Knit Sweater":
       print item
       p = item
#redirect to url 
 return render_template('purplesweater.html', sweater=p), 200

@app.route('/tops')
@app.route('/tops/poncho')
def tops_poncho():
 clothes = []
 with open('static/js/fashion.json', 'r') as f:
     clothes = json.load(f)
     f.close()

 p = {}
 for item in clothes:
     if item['name'] == "Navy Poncho Top":
       print item
       p = item
#redirect to url 
 return render_template('poncho.html', poncho=p), 200

@app.route('/bottoms')
def bottoms():
#redirect to url 
 return render_template('bottoms.html'), 200

@app.route('/botoms')
@app.route('/bottoms/whitetrouser')
def bottoms_whitetrouser():
 clothes = []
 with open('static/js/fashion.json', 'r') as f:
     clothes = json.load(f)
     f.close()

 p = {}
 for item in clothes:
     if item['name'] == "White Trouser":
       print item
       p = item
#redirect to url 
 return render_template('whitetrouser.html', whitetrouser=p), 200
 
@app.route('/bottoms')
@app.route('/bottoms/jeans')
def bottoms_jeans():
 clothes = []
 with open('static/js/fashion.json', 'r') as f:
     clothes = json.load(f)
     f.close()

 p = {}
 for item in clothes:
     if item['name'] == "Blue Skinny Jeans":
       print item
       p = item
#redirect to url 
 return render_template('blueskinnyjeans.html', bluejeans=p), 200
 
@app.route('/bottoms')
@app.route('/bottoms/shorts')
def bottoms_shorts():
 clothes = []
 with open('static/js/fashion.json', 'r') as f:
     clothes = json.load(f)
     f.close()

 p = {}
 for item in clothes:
     if item['name'] == "Blue Denim Shorts":
       print item
       p = item
#redirect to url 
 return render_template('blueshorts.html', shorts=p), 200

@app.route('/bottoms')
@app.route('/bottoms/leggings')
def bottoms_leggings():
 clothes = []
 with open('static/js/fashion.json', 'r') as f:
     clothes = json.load(f)
     f.close()

 p = {}
 for item in clothes:
     if item['name'] == "Ankle length leggings (black)":
       print item
       p = item
#redirect to url 
 return render_template('leggings.html', leggings=p), 200
 


@app.route('/shoes')
def shoes():
#redirect to url 
 return render_template('shoes.html'), 200

@app.route('/shoes')
@app.route('/shoes/pinkshoes')
def shoes_pinkshoes():
 clothes = []
 with open('static/js/fashion.json', 'r') as f:
     clothes = json.load(f)
     f.close()

 p = {}
 for item in clothes:
     if item['name'] == "Pink Shoes":
       print item
       p = item
#redirect to url 
 return render_template('pinkshoes.html', pinkshoes=p), 200
 
 
@app.route('/shoes')
@app.route('/shoes/sandals')
def shoes_sandals():
 clothes = []
 with open('static/js/fashion.json', 'r') as f:
     clothes = json.load(f)
     f.close()

 p = {}
 for item in clothes:
     if item['name'] == "Tan Sandals":
       print item
       p = item
#redirect to url 
 return render_template('sandals.html', sandals=p), 200
 
 
@app.route('/shoes')
@app.route('/shoes/ankleboots')
def shoes_ankleboots():
 clothes = []
 with open('static/js/fashion.json', 'r') as f:
     clothes = json.load(f)
     f.close()

 p = {}
 for item in clothes:
     if item['name'] == "Faux Suede Ankle Boots":
       print item
       p = item
#redirect to url 
 return render_template('ankleboots.html', ankleboots=p), 200
 

@app.route('/shoes')
@app.route('/shoes/longboots')
def shoes_longboots():
 clothes = []
 with open('static/js/fashion.json', 'r') as f:
     clothes = json.load(f)
     f.close()

 p = {}
 for item in clothes:
     if item['name'] == "Dark Brown Longboots":
       print item
       p = item
#redirect to url 
 return render_template('longboots.html', longboots=p), 200
 

@app.route('/accessories')
def accessories():
#redirect to url 
 return render_template('accessories.html'), 200
 
@app.route('/accessories')
@app.route('/accessories/hairaccessory')
def accessories_hairaccessory():
 clothes = []
 with open('static/js/fashion.json', 'r') as f:
     clothes = json.load(f)
     f.close()

 p = {}
 for item in clothes:
     if item['name'] == "Flower Hair Accessory":
       print item
       p = item
#redirect to url 
 return render_template('hairacc.html', hairacc=p), 200
 
 
@app.route('/accessories')
@app.route('/accessories/sunglasses')
def accessories_sunglasses():
 clothes = []
 with open('static/js/fashion.json', 'r') as f:
     clothes = json.load(f)
     f.close()

 p = {}
 for item in clothes:
     if item['name'] == "Cateye Sunglass":
       print item
       p = item
#redirect to url 
 return render_template('sunglasses.html', sunglasses=p), 200
 
 
@app.route('/accessories')
@app.route('/accessories/scarf')
def accessories_scarf():
 clothes = []
 with open('static/js/fashion.json', 'r') as f:
     clothes = json.load(f)
     f.close()

 p = {}
 for item in clothes:
     if item['name'] == "Classic Waffle Knit Scarf (Grey)":
       print item
       p = item
#redirect to url 
 return render_template('scarf.html', scarf=p), 200
 

@app.route('/accessories')
@app.route('/accessories/hatgloves')
def accessories_hatgloves():
 clothes = []
 with open('static/js/fashion.json', 'r') as f:
     clothes = json.load(f)
     f.close()

 p = {}
 for item in clothes:
     if item['name'] == "People Tree Grey Gloves and Hat":
       print item
       p = item
#redirect to url 
 return render_template('hatgloves.html', hatgloves=p), 200
 

#Seasons Outfits links 
@app.route('/all')
def all():
 return render_template('all.html'), 200
#Spring
@app.route('/all')
@app.route('/all/springstyle')
def springstyle():
#redirect to url 
 return render_template('springstyle.html'), 200
 
@app.route('/all')
@app.route('/all/springstyle')
@app.route('/all/springstyle/top')
def all_springstyle_top():
 clothes = []
 with open('static/js/fashion.json', 'r') as f:
     clothes = json.load(f)
     f.close()

 p = {}
 for item in clothes:
     if item['name'] == "Black Floral Top":
       print item
       p = item
#redirect to url 
 return render_template('blackfloral.html', blackfloral=p), 200

@app.route('/all')
@app.route('/all/springstyle')
@app.route('/all/springstyle/bottom')
def all_springstyle_bottom():
 clothes = []
 with open('static/js/fashion.json', 'r') as f:
     clothes = json.load(f)
     f.close()

 p = {}
 for item in clothes:
     if item['name'] == "Black Floral Top":
       print item
       p = item
#redirect to url 
 return render_template('whitetrouser.html', whitetrouser=p), 200

@app.route('/all')
@app.route('/all/springstyle')
@app.route('/all/springstyle/shoes')
def all_springstyle_shoes():
 clothes = []
 with open('static/js/fashion.json', 'r') as f:
     clothes = json.load(f)
     f.close()

 p = {}
 for item in clothes:
     if item['name'] == "Pink Shoes":
       print item
       p = item
#redirect to url 
 return render_template('pinkshoes.html', pinkshoes=p), 200

@app.route('/all')
@app.route('/all/springstyle')
@app.route('/all/springstyle/accessory')
def all_springstyle_accessory():
 clothes = []
 with open('static/js/fashion.json', 'r') as f:
     clothes = json.load(f)
     f.close()

 p = {}
 for item in clothes:
     if item['name'] == "Flower Hair Accessory":
       print item
       p = item
#redirect to url 
 return render_template('hairacc.html', hairacc=p), 200
 
#Summer
@app.route('/all')
@app.route('/all/summerstyle')
def summerstyle():
#redirect to url 
 return render_template('summerstyle.html'), 200
 
@app.route('/all')
@app.route('/all/summerstyle')
@app.route('/all/summerstyle/top')
def all_summerstyle_top():
 clothes = []
 with open('static/js/fashion.json', 'r') as f:
     clothes = json.load(f)
     f.close()

 p = {}
 for item in clothes:
     if item['name'] == "Stripes Croptop":
       print item
       p = item
#redirect to url 
 return render_template('croptop.html', croptop=p), 200

@app.route('/all')
@app.route('/all/summerstyle')
@app.route('/all/summerstyle/bottom')
def all_summerstyle_bottom():
 clothes = []
 with open('static/js/fashion.json', 'r') as f:
     clothes = json.load(f)
     f.close()

 p = {}
 for item in clothes:
     if item['name'] == "Blue Denim Shorts":
       print item
       p = item
#redirect to url 
 return render_template('blueshorts.html', shorts=p), 200

@app.route('/all')
@app.route('/all/summerstyle')
@app.route('/all/summerstyle/shoes')
def all_summerstyle_shoes():
 clothes = []
 with open('static/js/fashion.json', 'r') as f:
     clothes = json.load(f)
     f.close()

 p = {}
 for item in clothes:
     if item['name'] == "Tan Sandals":
       print item
       p = item
#redirect to url 
 return render_template('sandals.html', sandals=p), 200

@app.route('/all')
@app.route('/all/summerstyle')
@app.route('/all/summerstyle/accessory')
def all_summerstyle_accessory():
 clothes = []
 with open('static/js/fashion.json', 'r') as f:
     clothes = json.load(f)
     f.close()

 p = {}
 for item in clothes:
     if item['name'] == "Cateye Sunglass":
       print item
       p = item
#redirect to url 
 return render_template('sunglasses.html', sunglasses=p), 200

#Fall
@app.route('/all')
@app.route('/all/fallstyle')
def fallstyle():
#redirect to url 
 return render_template('fallstyle.html'), 200

@app.route('/all')
@app.route('/all/fallstyle')
@app.route('/all/fallstyle/top')
def all_fallstyle_top():
 clothes = []
 with open('static/js/fashion.json', 'r') as f:
     clothes = json.load(f)
     f.close()

 p = {}
 for item in clothes:
     if item['name'] == "Purple Knit Sweater":
       print item
       p = item
#redirect to url 
 return render_template('purplesweater.html', sweater=p), 200

@app.route('/all')
@app.route('/all/fallstyle')
@app.route('/all/fallstyle/bottom')
def all_fallstyle_bottom():
 clothes = []
 with open('static/js/fashion.json', 'r') as f:
     clothes = json.load(f)
     f.close()

 p = {}
 for item in clothes:
     if item['name'] == "Blue Skinny Jeans":
       print item
       p = item
#redirect to url 
 return render_template('blueskinnyjeans.html', bluejeans=p), 200

@app.route('/all')
@app.route('/all/fallstyle')
@app.route('/all/fallstyle/shoes')
def all_fallstyle_shoes():
  clothes = []
  with open('static/js/fashion.json', 'r') as f:
     clothes = json.load(f)
     f.close()
  
  p = {}
  for item in clothes:
     if item['name'] == "Faux Suede Ankle Boots":
       print item
       p = item
#redirect to url 
  return render_template('ankleboots.html', ankleboots=p), 200

@app.route('/all')
@app.route('/all/fallstyle')
@app.route('/all/fallstyle/accessory')
def all_fallstyle_accessory():
 clothes = []
 with open('static/js/fashion.json', 'r') as f:
     clothes = json.load(f)
     f.close()

 p = {}
 for item in clothes:
     if item['name'] == "Classic Waffle Knit Scarf (Grey)":
       print item
       p = item
#redirect to url 
 return render_template('scarf.html', scarf=p), 200
 
#Winter
 
@app.route('/all')
@app.route('/all/winterstyle')
def winterstyle():
#redirect to url 
 return render_template('winterstyle.html'), 200

@app.route('/all')
@app.route('/all/winterstyle')
@app.route('/all/winterstyle/top')
def all_winterstyle_top():
 clothes = []
 with open('static/js/fashion.json', 'r') as f:
     clothes = json.load(f)
     f.close()

 p = {}
 for item in clothes:
     if item['name'] == "Navy Poncho Top":
       print item
       p = item
#redirect to url 
 return render_template('poncho.html', poncho=p), 200

@app.route('/all')
@app.route('/all/winterstyle')
@app.route('/all/winterstyle/bottom')
def all_winterstyle_bottom():
 clothes = []
 with open('static/js/fashion.json', 'r') as f:
     clothes = json.load(f)
     f.close()

 p = {}
 for item in clothes:
     if item['name'] == "Ankle length leggings (black)":
       print item
       p = item
#redirect to url 
 return render_template('leggings.html', leggings=p), 200

@app.route('/all')
@app.route('/all/winterstyle')
@app.route('/all/winterstyle/shoes')
def all_winterstyle_shoes():
 clothes = []
 with open('static/js/fashion.json', 'r') as f:
     clothes = json.load(f)
     f.close()

 p = {}
 for item in clothes:
     if item['name'] == "Dark Brown Longboots":
       print item
       p = item
#redirect to url 
 return render_template('longboots.html', longboots=p), 200

@app.route('/all')
@app.route('/all/winterstyle')
@app.route('/all/winterstyle/accessory')
def all_winterstyle_accessory():
 clothes = []
 with open('static/js/fashion.json', 'r') as f:
     clothes = json.load(f)
     f.close()

 p = {}
 for item in clothes:
     if item['name'] == "People Tree Grey Gloves and Hat":
       print item
       p = item
#redirect to url 
 return render_template('hatgloves.html', hatgloves=p), 200
 
#Error Notice (wrong url)
@app.errorhandler (404)
def page_not_found(error):
 return " <h1><em>Sorry! <p>Couldn't find the page you requested.</p><em></h1>", 404


#This allows the app to run website on the browser
if __name__ == "__main__":
 app.run(host='0.0.0.0', debug=True)



