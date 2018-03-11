"""  craigslistScraper.py -
    Description: Grabs queries from craigslist and stores them for the user.
"""
import argparse, json, os
from scrapeCraigslist import scrapeCraigslist


def parser():
    
    parser = argparse.ArgumentParser(description='Craigslist Scraper Program')
    parser.add_argument('-u','--locationURL', help='URL to your craigslist location. EX: https://sacramento.craigslist.org/', required=True, dest = 'url')
    parser.add_argument('-r','--regex', help='Regular expression that we will search through craigslist for.', required=True, dest = 'regex')
    parser.add_argument('-c','--categories', help='Categories that you would like to search through.  If not passed will search through all categories.',
                        required=False, dest = 'cats', default = 'all',nargs = '*')

    return parser.parse_args()

    

if __name__ == "__main__":

    args = parser()

    print(args)

    url = args.url
    regex = args.regex

    if 'cats' in args.__dict__:
        cats = args.cats
        results = scrapeCraigslist(url, regex, cats)
    else:
        results = scrapeCraigslist(url, regex)
    
    

