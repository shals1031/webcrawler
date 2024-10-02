import requests
from bs4 import BeautifulSoup
import logging
import datetime

def readURLFromFile(filePath: str):
    with open(filePath, "r") as file:
        urlist = []
        # Read line by line
        for line in file:
            line.replace('\n', '')
            urlist.append(line)
        return urlist

# This is the main function

def main():
    logger = logging.getLogger(None)
    logging.basicConfig(filename='SiteVisits.log', encoding='utf-8', level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    logger.info(f"Starting the web crawler")
    logger.info("-------------------------------------------------------------------------------")
    
     # initialize the list of discovered urls with the first page to visit
    urls = readURLFromFile("urls.txt")
    
    # until all pages have been visited
    while len(urls) != 0:
        # get the page to visit from the list
        current_url = urls.pop()
        
        # crawling logic
        response = requests.get(current_url)
        soup = BeautifulSoup(response.content, "html.parser")
    
        link_elements = soup.select("a[href]")
        logger.info(f"Visited this site {current_url} having {len(link_elements)} links on it")
    
    logger.info(f"Ending the web crawler")
    logger.info("-------------------------------------------------------------------------------")


main()