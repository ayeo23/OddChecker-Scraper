#!/usr/bin/env python3

import requests
import re
from bs4 import BeautifulSoup
from time import sleep

# direct to dropbox location
dropbox = '/home/levo/Dropbox/Predictions/'

# setup url
baseurl = 'http://www.oddschecker.com/'
sport = 'football/'
country = 'english/'
league = 'premier-league/'
market = 'correct-score/'


# uses allthingsfpl to collect the current GW,
# this is used to pick and write correct files
def getGameweek():
    url = 'https://allthingsfpl.com/fantasy-football/gameweek-detail/'
    fplsite = requests.get(url)
    soup = BeautifulSoup(fplsite.content, "html.parser")
    gwheading = soup.find_all("h2")
    gwnum = gwheading[0].text.split(' ')
    gameweek = int(gwnum[1])
    print("Getting Predictions for Gameweek %d" % (gameweek))
    return gameweek


# Opens files needed to complete URL and download the fixtures for that week.
def read_fixtures(gameweek):
    fixturesFile = open(r'./fixtures/gameweek %d' % (gameweek), 'r')
    readFixtures = fixturesFile.readlines()
    fixturesFile.close()
    return readFixtures


# formats fixtures in a way to make comparison and help write Dp file
def format_team(fixture):
    remove_newline = fixture.rstrip('\n')
    remove_hyphian = remove_newline.replace('-', ' ')
    return remove_hyphian


# Collects the fav correct score, which is sorted on the site by fav first
def get_oddschecker(fixtures):
    odds_data = {}
    for fixture in fixtures:
        clean_fixture = fixture.rstrip('\n')  # cleans fixture for url
        url = baseurl + sport + country + league + clean_fixture.lower() + '/' + market
        try:
            response = requests.get(url)
        except Exception as e:
            print(e)

        soup = BeautifulSoup(response.content, "html.parser")
        tableData = soup.find_all("td", {"class": "sel nm"})
        score = tableData[0].text
        # creates a dict with team as key and fav correct score as value
        odds_data[format_team(fixture)] = score
        sleep(1)
    return odds_data


# return just the score line
def parse_score(score):
    score_regex = re.compile(r'\d-\d')
    result = score_regex.findall(score)
    result = ''.join(result)
    return result


# collect the information
def get_data(gameweek):
    fixtures = read_fixtures(gameweek)
    odds = get_oddschecker(fixtures)
    return odds


# returns either home or away team draw
def parse_winner(result):
    teamRegex = re.compile(r'^\D+')
    winner = teamRegex.findall(result)
    winner = ''.join(winner)
    winner = winner.rstrip()
    return winner


# writes the dropbox file using the dict compares fixture with
# fav correct score to arrange the data in the write order
def write_dropbox(result_dict):
    dropbox_file = open(dropbox + 'gameweek %d.txt' % (gameweek), 'w')
    for key, value in result_dict.items():
        score = parse_score(value)
        winner = parse_winner(value)
        teams = key.split(' v ')
        if winner != teams[0]:
            res = teams[0] + ' ' + score[2] + '-' + score[0] + ' ' + teams[1] + '\n'
            print(res)
            dropbox_file.write(res)
        else:
            res = teams[0] + ' ' + score + ' ' + teams[1] + '\n'
            print(res)
            dropbox_file.write(res)
    dropbox_file.close()


gameweek = getGameweek()
result_dict = get_data(gameweek)
write_dropbox(result_dict)
