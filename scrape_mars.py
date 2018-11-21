# import dependencies
from splinter import Browser
from bs4 import BeautifulSoup as bs
import pandas as pd
import time

def scrape():
    mars = {}

    # scrape first website for news heading and paragraph
    executable_path = {'executable_path': 'chromedriver'}
    browser = Browser('chrome', **executable_path)
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)
    time.sleep(5)
    news_soup = bs(browser.html, 'html.parser')
    news_title = news_soup.find('div', class_='content_title').get_text() 
    news_p = news_soup.find('div', class_='article_teaser_body').get_text()
    
    # add heading and paragraph to mars dictionary
    mars["news_title"] = news_title
    mars["news_para"] = news_p

   
    # scrape images website
    
    url_image = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url_image)
    full_image_elem = browser.find_by_id('full_image')
    full_image_elem.click()
    more_info = browser.find_link_by_partial_text('more info')
    more_info.click()
    featured_image_url = bs(browser.html, 'html.parser')
    featured_image_url
    image = featured_image_url.find('figure', class_='lede').find("img")["src"]
    http = "https://www.jpl.nasa.gov"
    image_url = http + image
    mars["full_image"] = image_url

    # scrape twitter weather

    mars_twitter = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(mars_twitter)
    twit_soup = bs(browser.html, 'html.parser')   
    mars_weather = twit_soup.body.find(class_='js-tweet-text')

    #scrape mars facts
    mars_facts = 'https://space-facts.com/mars/'
    browser.visit(mars_facts)
    mars_facts_df = pd.read_html(mars_facts)[0]
    facts_html = mars_facts_df.to_html()

    #scrape hemisphere website
    mars_sphere = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(mars_sphere)
    sphere_soup = bs(browser.html, 'html.parser')
    sphere_list = sphere_soup.find_all('a', class_="itemLink product-item")

    return mars

if __name__ == '__main__':
    scrape()