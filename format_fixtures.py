import os

teams_names = {
    'Leicester City': 'Leicester',
    'Manchester City': 'Man City',
    'Huddersfield Town': 'Huddersfield',
    'Stoke City': 'Stoke',
    'Manchester United': 'Man Utd',
    'West Ham United': 'West Ham',
    'Newcastle United': 'Newcastle',
    'Tottenham Hotspur': 'Tottenham',
    'Swansea City': 'Swansea',
    'West Bromwich Albion': 'West Brom',
    'AFC Bournemouth': 'Bournemouth',
}

scraped_dir = '/home/levo/Documents/projects/epl_round_sorter/fixtures/2017_18/'
write_dir = './2017_18/fixtures/'

if not os.path.exists(write_dir):
    os.makedirs(write_dir)

for i in range(1, 39):
    with open((scraped_dir + 'gameweek%d.txt') % (i), 'r') as fixtures_file:
        fixtures = fixtures_file.read()
    for key, values in teams_names.items():
        fixtures = fixtures.replace(key, values)
    fixtures = fixtures.replace(' ', '-')
    with open((write_dir + 'gameweek%d.txt') % (i), 'w') as write_file:
        write_file.write(fixtures)
