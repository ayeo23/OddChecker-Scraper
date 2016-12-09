import requests
from bs4 import BeautifulSoup
import time

baseurl = 'https://allthingsfpl.com/fantasy-football/gameweek-detail/?gw='

i = 15

while i < 38:
    response = requests.get(baseurl + str(i))
    soup = BeautifulSoup(response.content, "html.parser")
    tableData = soup.find_all("tr", {"class":"gwhead"})
    fixturelist = []
    gwfile = open('D:\\Programming\\OddChecker Scraper\\fixtures\\gameweek %d' %(i),'w')
    for fixture in tableData:
        fixturelist.append(fixture.text + '\n')


    gwfile.writelines(fixturelist)
    gwfile.close()
    i+= 1
    time.sleep(1)
