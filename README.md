# Oddschecker Correct Score Scraper

This script will scrape oddschecker.com for the favourite correct score for each of the fixtures for a given round of games. At the moment this is a simple run each time script that will dynamically create a file depending on what gameweek it is.

## How Does the Script Work?
The script will go through a number of stages to collect and format the data:
* Collect the current round gameweek
* Find the local  with fixtures for that gameweek and load in current fixtures
* Build the URL and download the favourite correct score for each fixture
* Build a dictonary with the fixtures as a key and the favourite correct score as value
* Use the dictonary to format a text file stored in Dropbox.
* Use workflow iOS app to load up the text file into a text message to be sent to league organiser.

## Configurations
If you were to use the script yourself you will need to need to change the **dropbox** variable to the path of your own dropbox location or any other location you want the file.

allthingsfpl is used as it will automatically directs you to the current gameweek. As the fixtures have been scrapped from this website to, it was an easy way to structure the current round of fixtures.
**Work needs to be done on handling any changes to fixtures.**

More work may need to be done to make the functions more modulated as currently the script can't be detatched to handle other markets due to **get_oddschecker()** is also used to build the dictonary.

### Oddschecker.com
http://www.oddschecker.com is a market comparison website looking at the odds across the bookmarker market for a variety of sports and betting markets.

Specially picked oddschecker as the page renders a table which is sorted by the favourite first. The way this is organised is the lowest odds across all the bookmarkers will be at the top of the table.

## Why Was The Script Created?
For a few years I have been part of a competiton with friend where by we try and predict the correct score and result of each weeks fixtures. Points are awarded for getting the correct winner and extra points for the correct score.

My process of evaluating my that week was to go through various data sources, including the betting markets to collect information on the most likely correct score. This was a long and laborious, browsing through each page and then typing up my predictions

The script has been built to automate this process and give me a quick template to send for that week, with small personal judgement tweeks made each week.
