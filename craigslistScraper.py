"""  craigslistScraper.py -
    Description: Grabs queries from craigslist and stores them for the user.
"""
import argparse



def parser():

    parser = argparse.ArgumentParser(description='Craigslist Scraper Program')
    parser.add_argument('-u','--locationURL', help='URL to your craigslist location. EX: https://sacramento.craigslist.org/', required=True, dest = 'url')
    parser.add_argument('-r','--regex', help='Regular expression that we will search through craigslist for.', required=True, dest = 'regex')
    parser.add_argument('-c','--categories', help='Command To Execute, Wrap in quotes(\'\') for commands with multiple fields.', required=False, dest = 'cat')

    return parser.parse_args()

    

if __name__ == "__main__":

    args = parser()

    url = args.url
    print("Url: " + url)
    regex = args.regex
    print("Regex: " + regex)

    if 'cat' in vars(args):
        cat = args.cat
        print("Category: " + str(cat))
    
    
    
    #main()
