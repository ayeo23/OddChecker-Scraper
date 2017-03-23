# Oddschecker Correct Score Scraper

This script will scrape oddschecker.com for the favourite correct score for each of the
fixtures for a given round of games. At the moment this is a simple run each time script that
will dynamically create a file depending on what gameweek it is.

## How Does the Script Work?
The script will go through a number of stages to collect and format the data:
* Collect the current round gameweek
* Find the file for that gameweek and load in current fixtures
* Build the URL and download the favourite correct score for each fixture
* Build a dictonary with the fixtures as a key and the favourite correct score as value
* Use the dictonary to format a text file stored in Dropbox.
* Use workflow iOS app to load up the text file into a text message to be sent to league organiser.

## Why Was The Script Created?
For a few years I have been part of a competiton with friend where by we try and predict
the correct score and result of each weeks fixtures. Points are awarded for getting the correct
winner and extra points for the correct score.

My process of evaluating my that week was to go through various data sources, including
the betting markets to collect information on the most likely correct score. This was a long
and laborious, browsing through each page and then typing up my predictions

The script has been built to automate this process and give me a quick template to send
for that week, with small personal judgement tweeks made each week.
