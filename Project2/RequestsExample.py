# Simple requests & beautiful soup project that scrapes google results!
#
# Description:
#    Once ran, you can give it any keyword, and it will return a few top google results for that keyword!
#

import requests
from bs4 import BeautifulSoup


def googleSearch(keyword):
    # Making a GET request
    url = "https://www.google.com/search?q=" + str(keyword)
    result = requests.get(url)
    return result




print("Welcome to my Google Scraper Program!\n")


keyword = input("Please input a single word you would like to google search, and we will return the top results.\n")


result = googleSearch(keyword)


soup = BeautifulSoup(result.text, 'html.parser')


headings = soup.find_all('h3')


print("\nResults: ")


i = 1
for info in headings:
    print("\t", i, ": ", info.getText())
    print()
    i = i + 1


print("Done")
