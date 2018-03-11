""" This file is used to grab all of the possible categories from craigslist
    and their extensions and stores the information into a json file
    in the data directory of craigslistScraper"""

from requests import request
from pprint import pprint
import bs4, json, os

if __name__ == '__main__':
        
    url = "https://sacramento.craigslist.com"
    resp = request(method = 'GET', url=url)
    resp.raise_for_status()
    soup = bs4.BeautifulSoup(resp.text, "lxml")
    categories = soup.select('.cats a')

    craigslistCats = {}
    for cat in categories:
        craigslistCats[cat.text] = cat.attrs['href']

    with open(os.getcwd() + '\\data\\craigslistCats.json', 'w') as file:
        json.dump(craigslistCats, file)

    

    
    
    

    #main()
