scoreFile = open('C:\\Users\\Levo\\Desktop\\scores.txt', 'r')
scores = scoreFile.readlines()
scoreFile.close()

fixtureFile = open('C:\\Users\\Levo\\Desktop\\fix.txt', 'r')
fixtures = fixtureFile.readlines()
fixtureFile.close()

reFormatFix = list()

for fixture in fixtures:
    fix = fixture.split(' v ')
    reFormatFix.append(fix)


scoreList = list()

for score in scores:
    scoreSplit = score.split(' ')
    scoreList.append(scoreSplit)
