#!/usr/bin/env python3

import requests
import re
from bs4 import BeautifulSoup
from time import sleep

dropbox = '/home/levo/Dropbox/Predictions/'

# setup url
baseurl = 'http://www.oddschecker.com/football/'
country = 'english/'
league = 'premier-league/'
market = 'correct-score/'


def getGameweek():
    url = 'https://allthingsfpl.com/fantasy-football/gameweek-detail/'
    fplsite = requests.get(url)
    soup = BeautifulSoup(fplsite.content, "html.parser")
    gwheading = soup.find_all("h2")
    gwnum = gwheading[0].text.split(' ')
    gameweek = int(gwnum[1])
    print("Getting Predictions for Gameweek %d" % (gameweek))
    return gameweek


# Opens files needed to complete URL as well as the file to be written to.
def read_fixtures(gameweek):
    fixturesFile = open(r'./fixtures/gameweek %d' % (gameweek), 'r')
    readFixtures = fixturesFile.readlines()
    fixturesFile.close()
    return readFixtures


def format_team(fixture):
    remove_newline = fixture.rstrip('\n')
    remove_hyphian = remove_newline.replace('-', ' ')
    return remove_hyphian


def get_oddschecker(fixtures):
    odds_data = {}
    for fixture in fixtures:
        clean_fixture = fixture.rstrip('\n')  # cleans fixture for url
        url = baseurl + country + league + clean_fixture.lower() + '/' + market
        try:
            response = requests.get(url)
        except Exception as e:
            print(e)

        soup = BeautifulSoup(response.content, "html.parser")
        tableData = soup.find_all("td", {"class": "sel nm"})
        score = tableData[0].text
        odds_data[format_team(fixture)] = score
        sleep(1)
    return odds_data


def parse_score(score):
    score_regex = re.compile(r'\d-\d')
    result = score_regex.findall(score)
    result = ''.join(result)
    return result


def get_data(gameweek):
    fixtures = read_fixtures(gameweek)
    odds = get_oddschecker(fixtures)
    return odds


def parse_winner(result):
    teamRegex = re.compile(r'^\w+\s?\w+\S\D')
    winner = teamRegex.findall(result)
    winner = ''.join(winner)
    winner = winner.rstrip()
    return winner


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
