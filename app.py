
from flask import Flask, render_template, jsonify
from flask_pymongo import PyMongo
# import python script that scrapes the websites
import scrape_mars

app = Flask(__name__)

mongo = PyMongo(app)

@app.route("/")
def index():
    data = scrape()
    return render_template('index.html')

@app.route("/scrape")
def scrape():
    # connecting to mongo db called mars
    mars = mongo.db.mars
    # run scrape_mars.scrape() function to gather data from dif website
    mars_data = scrape_mars.scrape()
    mars.update(
        {},
        mars_data,
        upsert=true
    )
    return "Scraping was successful"

if __name__ == "__main__":
    app.run(debug=True)
