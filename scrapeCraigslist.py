""" This file stores all of the main functionality of the scraper program.
    It will take a url, regular expression(regex) and a category(cat) and
    search craigslist for the regular expression and categories that you have
    passed to the program. """


from requests import request
from pprint import pprint
from fake_useragent import UserAgent
import bs4, json, os, re

headers = {'User-Agent' : UserAgent().chrome}

def scrapeCraigslist(url, regex, cats = 'all'):

    with open(os.getcwd() + '\\data\\craigslistCats.json') as catFile:
        catData = json.load(catFile)

    userRegex = re.compile(regex)

    extens = []

    if cats == 'all':
        cats = catData.keys()
    
    for cat in cats:
         extens += [catData[cat]]

   
    
    for exten in extens:
        resp = request(method= 'GET', url = url+exten, headers = headers)
        soup = bs4.BeautifulSoup(resp.text, "lxml")
        posts = soup.select('.result-title')

        matches = {}
        
        for post in posts:
            mo = userRegex.search(post.text)
            if mo != None:
                if post.text not in matches.keys():
                    matches = goIntoPost(post, userRegex, True, matches)
            else:
                if post.text not in matches.keys():
                    matches = goIntoPost(post, userRegex, False, matches)
                

                
        print(matches)
        
                
def goIntoPost(post, userRegex, titleMatch, matches):
    resp = request(method="GET", url = post.attrs['href'], headers = headers)
    soup = bs4.BeautifulSoup(resp.text, "lxml")
    mo = userRegex.search(post.text)

    print("In goIntoPost for " + post.text)

    contentMatch = False
    
    if mo != None:
        matches[post.text] = {}
        matches[post.text]["url"] = post.attrs['href']
        matches[post.text]["titleMatch"] = titleMatch
        contentMatch = True
        matches[post.text]["contentMatch"] = contentMatch

    elif titleMatch == True:
        matches[post.text] = {}
        matches[post.text]["url"] = post.attrs['href']
        matches[post.text]["titleMatch"] = titleMatch
        matches[post.text]["contentMatch"] = contentMatch
                
            

    return matches
    
    
