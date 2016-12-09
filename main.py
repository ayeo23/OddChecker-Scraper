import requests
from bs4 import BeautifulSoup
import time

# Function will fetch GW number as the webpage will default to current GW.

def getGameweek():
    fplsite = requests.get('https://allthingsfpl.com/fantasy-football/gameweek-detail/')
    soup = BeautifulSoup(fplsite.content, "html.parser")
    gwheading = soup.find_all("h2")
    gwnum = gwheading[0].text.split(' ')
    gameweek = int(gwnum[1])
    return gameweek

gameweek = getGameweek()
print(str("Getting Predictions for Gameweek " + str(gameweek)))

#Setup of URL:

baseurl = 'http://www.oddschecker.com/football/'

country = 'english/'
league = 'premier-league/'
market = 'correct-score/'

# Opens files needed to complete URL as well as the file to be written to.

fixturesFile = open('D:\\Programming\\OddChecker Scraper\\fixtures\\gameweek %d' %(gameweek), 'r')
readFixtures = fixturesFile.readlines()
fixturesFile.close()
dropboxFile = open('D:\\Dropbox\\Predictions\\gameweek %d.txt' %(gameweek), 'w')


for fixture in readFixtures:

    url = baseurl + country + league + fixture.lower().rstrip('\n') + '/' + market #OddChecker.com/country/league/fixture/correct-score/
    # print(url)
    try:
        response = requests.get(url)
    except Exception as e:
        print(e)

    reFormatFix = fixture.split('-v-') # splits the teams in two separate

	# getting score
    soup = BeautifulSoup(response.content, "html.parser")
    tableData = soup.find_all("td", {"class":"sel nm"})
    score = tableData[0].text
    score = score.split(' ')

    if score[0].rstrip() != reFormatFix[1].rstrip():
        # print((reFormatFix[0].replace('-', ' ') + ' ' + score[1] + ' ' + reFormatFix[1].replace('-',' ')))
        dropboxFile.write(reFormatFix[0].replace('-', ' ') + ' ' + score[1] + ' ' + reFormatFix[1].replace('-',' '))
    else:
        score = score[1]
        # print(dropboxFile.write(reFormatFix[0].replace('-', ' ') + ' ' + score[2] + score[1] + score[0] + ' ' + reFormatFix[1].replace('-',' ')))
        dropboxFile.write(reFormatFix[0].replace('-', ' ') + ' ' + score[2] + score[1] + score[0] + ' ' + reFormatFix[1].replace('-',' '))


    time.sleep(2)

dropboxFile.close()

print("Done... Your file is in Dropbox")
