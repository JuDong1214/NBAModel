import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup
import pandas as pd

#Home All Games
driver = webdriver.Firefox()
url = r"https://www.cbssports.com/nba/schedule/"
driver.get(url)
print("Implicit Wait Example")
time.sleep(4)

src = driver.page_source
parser = BeautifulSoup(src, "lxml")
table = parser.find("div", attrs = {"class": "TableBase-overflow"})
headers= table.findAll('th')
headerlist = [h.text.strip() for h in headers[0:]]

rows = table.findAll('tr')[1:]
teamsPlaying = [[td.getText().strip() for td in rows[i].findAll('td')[0:]] for i in range(len(rows))]
pd.set_option('max_columns', None)
teamsToday = pd.DataFrame(teamsPlaying, columns=headerlist)

teamID = {
    'Atlanta': 1610612737,
    'Boston': 1610612738,
    'Brooklyn': 1610612751,
    'Charlotte': 1610612766,
    'Chicago': 1610612741,
    'Cleveland': 1610612739,
    'Dallas': 1610612742,
    'Denver': 1610612743,
    'Detroit': 1610612765,
    'Golden St.': 1610612744,
    'Houston': 1610612745,
    'Indiana': 1610612754,
    'L.A. Clippers': 1610612746,
    'L.A. Lakers': 1610612747,
    'Memphis': 1610612763,
    'Miami': 1610612748,
    'Milwaukee': 1610612749,
    'Minnesota': 1610612750,
    'New Orleans': 1610612740,
    'New York': 1610612752,
    'Oklahoma City': 1610612760,
    'Orlando': 1610612753,
    'Philadelphia': 1610612755,
    'Phoenix': 1610612756,
    'Portland': 1610612757,
    'Sacramento': 1610612758,
    'San Antonio': 1610612759,
    'Toronto': 1610612761,
    'Utah': 1610612762,
    'Washington': 1610612764
}

#Home All Games
driver = webdriver.Firefox()
url = r"https://www.nba.com/stats/teams/advanced/?sort=W&dir=-1&Season=2021-22&SeasonType=Regular%20Season&Location=Home"
driver.get(url)
print("Implicit Wait Example")
time.sleep(4)

src = driver.page_source
parser = BeautifulSoup(src, "lxml")
table = parser.find("div", attrs = {"class": "nba-stat-table__overflow"})
headers= table.findAll('th')
headerlist = [h.text.strip() for h in headers[1:]]

headerlist1 = [a for a in headerlist if not 'RANK' in a]
rows = table.findAll('tr')[1:]
player_stats = [[td.getText().strip() for td in rows[i].findAll('td')[1:]] for i in range(len(rows))]
pd.set_option('max_columns', None)
stats = pd.DataFrame(player_stats, columns=headerlist1)

#Away All Games
url = r"https://www.nba.com/stats/teams/advanced/?sort=DEF_RATING&dir=-1&Season=2021-22&SeasonType=Regular%20Season&Location=Road"
driver.get(url)
print("Implicit Wait Example")
time.sleep(4)

src = driver.page_source
parser = BeautifulSoup(src, "lxml")
table = parser.find("div", attrs = {"class": "nba-stat-table__overflow"})

rows = table.findAll('tr')[1:]
player_stats2 = [[td.getText().strip() for td in rows[i].findAll('td')[1:]] for i in range(len(rows))]
pd.set_option('max_columns', None)
stats2 = pd.DataFrame(player_stats2, columns=headerlist1)

#Home Last 10 Games
url = r"https://www.nba.com/stats/teams/advanced/?sort=W&dir=-1&Season=2021-22&SeasonType=Regular%20Season&Location=Home&LastNGames=10"
driver.get(url)
print("Implicit Wait Example")
time.sleep(4)

src = driver.page_source
parser = BeautifulSoup(src, "lxml")
table = parser.find("div", attrs = {"class": "nba-stat-table__overflow"})

rows = table.findAll('tr')[1:]
player_stats3 = [[td.getText().strip() for td in rows[i].findAll('td')[1:]] for i in range(len(rows))]
pd.set_option('max_columns', None)
stats3 = pd.DataFrame(player_stats3, columns=headerlist1)

#Road Last 10 Games
url = r"https://www.nba.com/stats/teams/advanced/?sort=W&dir=-1&Season=2021-22&SeasonType=Regular%20Season&Location=Road&LastNGames=10"
driver.get(url)
print("Implicit Wait Example")
time.sleep(4)

src = driver.page_source
parser = BeautifulSoup(src, "lxml")
table = parser.find("div", attrs = {"class": "nba-stat-table__overflow"})

rows = table.findAll('tr')[1:]
player_stats4 = [[td.getText().strip() for td in rows[i].findAll('td')[1:]] for i in range(len(rows))]
pd.set_option('max_columns', None)
stats4 = pd.DataFrame(player_stats4, columns=headerlist1)

stats.set_index("TEAM", inplace = True)
stats2.set_index("TEAM", inplace = True)
stats3.set_index("TEAM", inplace = True)
stats4.set_index("TEAM", inplace = True)

for i in range(len(teamsToday)):
    homeTeam = teamsToday.at[i,'Home']
    awayTeam = teamsToday.at[i,'Away']
    
    #TeamVSTeam Pace
    driver = webdriver.Firefox()
    url = r"https://www.nba.com/stats/teams/advanced/?sort=W&dir=-1&Season=2021-22&SeasonType=Regular%20Season&OpponentTeamID=" + str(teamID[awayTeam]) + r"&TeamID=" + str(teamID[homeTeam])
    driver.get(url)
    print("Implicit Wait Example")
    time.sleep(4)

    src = driver.page_source
    parser = BeautifulSoup(src, "lxml")
    table = parser.find("div", attrs = {"class": "nba-stat-table__overflow"})
    
    if table is not None:

        rows = table.findAll('tr')[1:]
        player_stats5 = [[td.getText().strip() for td in rows[i].findAll('td')[1:]] for i in range(len(rows))]
        pd.set_option('max_columns', None)
        stats5 = pd.DataFrame(player_stats5, columns=headerlist1)


        stats5.set_index("TEAM", inplace = True)


        if homeTeam == 'Atlanta':
            homeTeam = 'Atlanta Hawks'
        if homeTeam == 'Boston':
            homeTeam = 'Boston Celtics'
        if homeTeam == 'Brooklyn':
            homeTeam = 'Brooklyn Nets'
        if homeTeam == 'Charlotte':
            homeTeam = 'Charlotte Hornets'
        if homeTeam == 'Chicago':
            homeTeam = 'Chicago Bulls'
        if homeTeam == 'Cleveland':
            homeTeam = 'Cleveland Cavaliers'
        if homeTeam == 'Dallas':
            homeTeam = 'Dallas Mavericks'
        if homeTeam == 'Denver':
            homeTeam = 'Denver Nuggets'
        if homeTeam == 'Detroit':
            homeTeam = 'Detroit Pistons'
        if homeTeam == 'Golden St.':
            homeTeam = 'Golden State Warriors'
        if homeTeam == 'Houston':
            homeTeam = 'Houston Rockets'
        if homeTeam == 'Indiana':
            homeTeam = 'Indiana Pacers'
        if homeTeam == 'L.A. Clippers':
            homeTeam = 'LA Clippers'
        if homeTeam == 'L.A. Lakers':
            homeTeam = 'Los Angeles Lakers'
        if homeTeam == 'Memphis':
            homeTeam = 'Memphis Grizzlies'
        if homeTeam == 'Miami':
            homeTeam = 'Miami Heat'
        if homeTeam == 'Milwaukee':
            homeTeam = 'Milwaukee Bucks'
        if homeTeam == 'Minnesota':
            homeTeam = 'Minnesota Timberwolves'
        if homeTeam == 'New Orleans':
            homeTeam = 'New Orleans Pelicans'
        if homeTeam == 'New York':
            homeTeam = 'New York Knicks'
        if homeTeam == 'Oklahoma City':
            homeTeam = 'Oklahoma City Thunder'
        if homeTeam == 'Orlando':
            homeTeam = 'Orlando Magic'
        if homeTeam == 'Philadelphia':
            homeTeam = 'Philadelphia 76ers'
        if homeTeam == 'Phoenix':
            homeTeam = 'Phoenix Suns'
        if homeTeam == 'Portland':
            homeTeam = 'Portland Trail Blazers'
        if homeTeam == 'Sacramento':
            homeTeam = 'Sacramento Kings'
        if homeTeam == 'San Antonio':
            homeTeam = 'San Antonio Spurs'
        if homeTeam == 'Toronto':
            homeTeam = 'Toronto Raptors'
        if homeTeam == 'Utah':
            homeTeam = 'Utah Jazz'
        if homeTeam == 'Washington':
            homeTeam = 'Washington Wizards'


        if awayTeam == 'Atlanta':
            awayTeam = 'Atlanta Hawks'
        if awayTeam == 'Boston':
            awayTeam = 'Boston Celtics'
        if awayTeam == 'Brooklyn':
            awayTeam = 'Brooklyn Nets'
        if awayTeam == 'Charlotte':
            awayTeam = 'Charlotte Hornets'
        if awayTeam == 'Chicago':
            awayTeam = 'Chicago Bulls'
        if awayTeam == 'Cleveland':
            awayTeam = 'Cleveland Cavaliers'
        if awayTeam == 'Dallas':
            awayTeam = 'Dallas Mavericks'
        if awayTeam == 'Denver':
            awayTeam = 'Denver Nuggets'
        if awayTeam == 'Detroit':
            awayTeam = 'Detroit Pistons'
        if awayTeam == 'Golden St.':
            awayTeam = 'Golden State Warriors'
        if awayTeam == 'Houston':
            awayTeam = 'Houston Rockets'
        if awayTeam == 'Indiana':
            awayTeam = 'Indiana Pacers'
        if awayTeam == 'L.A. Clippers':
            awayTeam = 'LA Clippers'
        if awayTeam == 'L.A. Lakers':
            awayTeam = 'Los Angeles Lakers'
        if awayTeam == 'Memphis':
            awayTeam = 'Memphis Grizzlies'
        if awayTeam == 'Miami':
            awayTeam = 'Miami Heat'
        if awayTeam == 'Milwaukee':
            awayTeam = 'Milwaukee Bucks'
        if awayTeam == 'Minnesota':
            awayTeam = 'Minnesota Timberwolves'
        if awayTeam == 'New Orleans':
            awayTeam = 'New Orleans Pelicans'
        if awayTeam == 'New York':
            awayTeam = 'New York Knicks'
        if awayTeam == 'Oklahoma City':
            awayTeam = 'Oklahoma City Thunder'
        if awayTeam == 'Orlando':
            awayTeam = 'Orlando Magic'
        if awayTeam == 'Philadelphia':
            awayTeam = 'Philadelphia 76ers'
        if awayTeam == 'Phoenix':
            awayTeam = 'Phoenix Suns'
        if awayTeam == 'Portland':
            awayTeam = 'Portland Trail Blazers'
        if awayTeam == 'Sacramento':
            awayTeam = 'Sacramento Kings'
        if awayTeam == 'San Antonio':
            awayTeam = 'San Antonio Spurs'
        if awayTeam == 'Toronto':
            awayTeam = 'Toronto Raptors'
        if awayTeam == 'Utah':
            awayTeam = 'Utah Jazz'
        if awayTeam == 'Washington':
            awayTeam = 'Washington Wizards'






        HomeSZNhORTG = float(stats.loc[homeTeam]['OffRtg'])
        HomeSZNaDRTG = float(stats2.loc[awayTeam]['DefRtg'])
        HomeSZNhPace = float(stats.loc[homeTeam]['PACE'])
        HomeLast10hORTG = float(stats3.loc[homeTeam]['OffRtg'])
        HomeLast10aDRTG = float(stats4.loc[awayTeam]['DefRtg'])
        h2hPace = float(stats5.loc[homeTeam]['PACE'])
        print(homeTeam, "Total")
        homeTotal = ((((HomeSZNhORTG + HomeSZNaDRTG)/200)*HomeSZNhPace)+(((HomeLast10hORTG + HomeLast10aDRTG)/200)*h2hPace))/2
        print(homeTotal)

        AwaySZNaORTG = float(stats2.loc[awayTeam]['OffRtg'])
        AwaySZNhDRTG = float(stats.loc[homeTeam]['DefRtg'])
        AwaySZNaPace = float(stats2.loc[awayTeam]['PACE'])
        AwayLast10aORTG = float(stats4.loc[awayTeam]['OffRtg'])
        AwayLast10hDRTG = float(stats3.loc[homeTeam]['DefRtg'])
        h2hPace = float(stats5.loc[homeTeam]['PACE'])
        print(awayTeam, "Toal")
        awayTotal = ((((AwaySZNaORTG + AwaySZNhDRTG)/200)*AwaySZNaPace)+(((AwayLast10aORTG + AwayLast10hDRTG)/200)*h2hPace))/2
        print(awayTotal)
        Total = homeTotal + awayTotal
        print('Total =')
        print(Total)
