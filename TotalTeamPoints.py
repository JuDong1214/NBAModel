import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup
import pandas as pd

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

#TeamVSTeam Pace
url = r"https://www.nba.com/stats/teams/advanced/?sort=W&dir=-1&Season=2021-22&SeasonType=Regular%20Season&OpponentTeamID=1610612766&TeamID=1610612739"
driver.get(url)
print("Implicit Wait Example")
time.sleep(4)

src = driver.page_source
parser = BeautifulSoup(src, "lxml")
table = parser.find("div", attrs = {"class": "nba-stat-table__overflow"})
   
rows = table.findAll('tr')[1:]
player_stats5 = [[td.getText().strip() for td in rows[i].findAll('td')[1:]] for i in range(len(rows))]
pd.set_option('max_columns', None)
stats5 = pd.DataFrame(player_stats5, columns=headerlist1)

HomeSZNhORTG = float(stats.loc['Cleveland Cavaliers']['OffRtg'])
HomeSZNaDRTG = float(stats2.loc['Charlotte Hornets']['DefRtg'])
HomeSZNhPace = float(stats.loc['Cleveland Cavaliers']['PACE'])
HomeLast10hORTG = float(stats3.loc['Cleveland Cavaliers']['OffRtg'])
HomeLast10aDRTG = float(stats4.loc['Charlotte Hornets']['DefRtg'])
h2hPace = float(stats5.loc['Cleveland Cavaliers']['PACE'])
print('Cavs Total')
cavsTotal = ((((HomeSZNhORTG + HomeSZNaDRTG)/200)*HomeSZNhPace)+(((HomeLast10hORTG + HomeLast10aDRTG)/200)*h2hPace))/2
print(cavsTotal)

AwaySZNaORTG = float(stats2.loc['Charlotte Hornets']['OffRtg'])
AwaySZNhDRTG = float(stats.loc['Cleveland Cavaliers']['DefRtg'])
AwaySZNaPace = float(stats2.loc['Charlotte Hornets']['PACE'])
AwayLast10aORTG = float(stats4.loc['Charlotte Hornets']['OffRtg'])
AwayLast10hDRTG = float(stats3.loc['Cleveland Cavaliers']['DefRtg'])
h2hPace = float(stats5.loc['Cleveland Cavaliers']['PACE'])
print('Hornets Total')
hornetsTotal = ((((AwaySZNaORTG + AwaySZNhDRTG)/200)*AwaySZNaPace)+(((AwayLast10aORTG + AwayLast10hDRTG)/200)*h2hPace))/2
print(hornetsTotal)
Total = cavsTotal + hornetsTotal
print('Total =')
print(Total)
print('Under 219')
print('Actual: 217')

#Pacers vs Magic
driver = webdriver.Firefox()
url = r"https://www.nba.com/stats/teams/advanced/?sort=W&dir=-1&Season=2021-22&SeasonType=Regular%20Season&OpponentTeamID=1610612754&TeamID=1610612753"
driver.get(url)
print("Implicit Wait Example")
time.sleep(4)

src = driver.page_source
parser = BeautifulSoup(src, "lxml")
table = parser.find("div", attrs = {"class": "nba-stat-table__overflow"})
   
rows = table.findAll('tr')[1:]
player_statsPvM = [[td.getText().strip() for td in rows[i].findAll('td')[1:]] for i in range(len(rows))]
pd.set_option('max_columns', None)
statsPvM = pd.DataFrame(player_statsPvM, columns=headerlist1)

statsPvM.set_index("TEAM", inplace = True)

HomeSZNhORTG = float(stats.loc['Orlando Magic']['OffRtg'])
HomeSZNaDRTG = float(stats2.loc['Indiana Pacers']['DefRtg'])
HomeSZNhPace = float(stats.loc['Orlando Magic']['PACE'])
HomeLast10hORTG = float(stats3.loc['Orlando Magic']['OffRtg'])
HomeLast10aDRTG = float(stats4.loc['Indiana Pacers']['DefRtg'])
h2hPacePvM = float(statsPvM.loc['Orlando Magic']['PACE'])
print('Magic Total')
magicTotal = ((((HomeSZNhORTG + HomeSZNaDRTG)/200)*HomeSZNhPace)+(((HomeLast10hORTG + HomeLast10aDRTG)/200)*h2hPacePvM))/2
print(magicTotal)

AwaySZNaORTG = float(stats2.loc['Indiana Pacers']['OffRtg'])
AwaySZNhDRTG = float(stats.loc['Orlando Magic']['DefRtg'])
AwaySZNaPace = float(stats2.loc['Indiana Pacers']['PACE'])
AwayLast10aORTG = float(stats4.loc['Indiana Pacers']['OffRtg'])
AwayLast10hDRTG = float(stats3.loc['Orlando Magic']['DefRtg'])
h2hPacePvM = float(statsPvM.loc['Orlando Magic']['PACE'])
print('Pacers Total')
pacersTotal = ((((AwaySZNaORTG + AwaySZNhDRTG)/200)*AwaySZNaPace)+(((AwayLast10aORTG + AwayLast10hDRTG)/200)*h2hPacePvM))/2
print(pacersTotal)
Total2 = magicTotal + pacersTotal
print('Total =')
print(Total2)
print('Under 233.5')
print('actual 236, before OT:220')

#Kings vs Pels
driver = webdriver.Firefox()
url = r"https://www.nba.com/stats/teams/advanced/?sort=W&dir=-1&Season=2021-22&SeasonType=Regular%20Season&OpponentTeamID=1610612758&TeamID=1610612740"
driver.get(url)
print("Implicit Wait Example")
time.sleep(4)

src = driver.page_source
parser = BeautifulSoup(src, "lxml")
table = parser.find("div", attrs = {"class": "nba-stat-table__overflow"})
   
rows = table.findAll('tr')[1:]
player_statsKvP = [[td.getText().strip() for td in rows[i].findAll('td')[1:]] for i in range(len(rows))]
pd.set_option('max_columns', None)
statsKvP = pd.DataFrame(player_statsKvP, columns=headerlist1)
statsKvP.set_index("TEAM", inplace = True)


HomeSZNhORTG = float(stats.loc['New Orleans Pelicans']['OffRtg'])
HomeSZNaDRTG = float(stats2.loc['Sacramento Kings']['DefRtg'])
HomeSZNhPace = float(stats.loc['New Orleans Pelicans']['PACE'])
HomeLast10hORTG = float(stats3.loc['New Orleans Pelicans']['OffRtg'])
HomeLast10aDRTG = float(stats4.loc['Sacramento Kings']['DefRtg'])
h2hPaceKvP = float(statsKvP.loc['New Orleans Pelicans']['PACE'])
print('Pels Total')
pelsTotal = ((((HomeSZNhORTG + HomeSZNaDRTG)/200)*HomeSZNhPace)+(((HomeLast10hORTG + HomeLast10aDRTG)/200)*h2hPaceKvP))/2
print(pelsTotal)

AwaySZNaORTG = float(stats2.loc['Sacramento Kings']['OffRtg'])
AwaySZNhDRTG = float(stats.loc['New Orleans Pelicans']['DefRtg'])
AwaySZNaPace = float(stats2.loc['Sacramento Kings']['PACE'])
AwayLast10aORTG = float(stats4.loc['Sacramento Kings']['OffRtg'])
AwayLast10hDRTG = float(stats3.loc['New Orleans Pelicans']['DefRtg'])
h2hPaceKvP = float(statsKvP.loc['New Orleans Pelicans']['PACE'])
print('Kings Total')
kingsTotal = ((((AwaySZNaORTG + AwaySZNhDRTG)/200)*AwaySZNaPace)+(((AwayLast10aORTG + AwayLast10hDRTG)/200)*h2hPaceKvP))/2
print(kingsTotal)
Total3 = pelsTotal + kingsTotal
print('Total =')
print(Total3)
print('Under 233.5')
print('Kings +6.5')
print('actual: 220')

#Heat vs Bucks
driver = webdriver.Firefox()
url = r"https://www.nba.com/stats/teams/advanced/?sort=W&dir=-1&Season=2021-22&SeasonType=Regular%20Season&OpponentTeamID=1610612748&TeamID=1610612749"
driver.get(url)
print("Implicit Wait Example")
time.sleep(4)

src = driver.page_source
parser = BeautifulSoup(src, "lxml")
table = parser.find("div", attrs = {"class": "nba-stat-table__overflow"})
   
rows = table.findAll('tr')[1:]
player_statsHvB = [[td.getText().strip() for td in rows[i].findAll('td')[1:]] for i in range(len(rows))]
pd.set_option('max_columns', None)
statsHvB = pd.DataFrame(player_statsHvB, columns=headerlist1)
statsHvB.set_index("TEAM", inplace = True)

HomeSZNhORTG = float(stats.loc['Milwaukee Bucks']['OffRtg'])
HomeSZNaDRTG = float(stats2.loc['Miami Heat']['DefRtg'])
HomeSZNhPace = float(stats.loc['Milwaukee Bucks']['PACE'])
HomeLast10hORTG = float(stats3.loc['Milwaukee Bucks']['OffRtg'])
HomeLast10aDRTG = float(stats4.loc['Miami Heat']['DefRtg'])
h2hPaceHvB = float(statsHvB.loc['Milwaukee Bucks']['PACE'])
print('Bucks Total')
bucksTotal = ((((HomeSZNhORTG + HomeSZNaDRTG)/200)*HomeSZNhPace)+(((HomeLast10hORTG + HomeLast10aDRTG)/200)*h2hPaceHvB))/2
print(bucksTotal)

AwaySZNaORTG = float(stats2.loc['Miami Heat']['OffRtg'])
AwaySZNhDRTG = float(stats.loc['Milwaukee Bucks']['DefRtg'])
AwaySZNaPace = float(stats2.loc['Miami Heat']['PACE'])
AwayLast10aORTG = float(stats4.loc['Miami Heat']['OffRtg'])
AwayLast10hDRTG = float(stats3.loc['Milwaukee Bucks']['DefRtg'])
h2hPaceHvB = float(statsHvB.loc['Milwaukee Bucks']['PACE'])
print('Heat Total')
heatTotal = ((((AwaySZNaORTG + AwaySZNhDRTG)/200)*AwaySZNaPace)+(((AwayLast10aORTG + AwayLast10hDRTG)/200)*h2hPaceHvB))/2
print(heatTotal)
Total4 = bucksTotal + heatTotal
print('Total =')
print(Total4)
print('Under 224.5')
print('Heat +4.5')
print('Heat +4.5, 239')


#Jazz vs Rockets
driver = webdriver.Firefox()
url = r"https://www.nba.com/stats/teams/advanced/?sort=W&dir=-1&Season=2021-22&SeasonType=Regular%20Season&OpponentTeamID=1610612745&TeamID=1610612762"
driver.get(url)
print("Implicit Wait Example")
time.sleep(4)

src = driver.page_source
parser = BeautifulSoup(src, "lxml")
table = parser.find("div", attrs = {"class": "nba-stat-table__overflow"})
   
rows = table.findAll('tr')[1:]
player_statsJvR = [[td.getText().strip() for td in rows[i].findAll('td')[1:]] for i in range(len(rows))]
pd.set_option('max_columns', None)
statsJvR = pd.DataFrame(player_statsJvR, columns=headerlist1)
statsJvR.set_index("TEAM", inplace = True)
HomeSZNhORTG = float(stats.loc['Houston Rockets']['OffRtg'])
HomeSZNaDRTG = float(stats2.loc['Utah Jazz']['DefRtg'])
HomeSZNhPace = float(stats.loc['Houston Rockets']['PACE'])
HomeLast10hORTG = float(stats3.loc['Houston Rockets']['OffRtg'])
HomeLast10aDRTG = float(stats4.loc['Utah Jazz']['DefRtg'])
h2hPaceJvR = float(statsJvR.loc['Utah Jazz']['PACE'])
print('Rockets Total')
rocketsTotal = ((((HomeSZNhORTG + HomeSZNaDRTG)/200)*HomeSZNhPace)+(((HomeLast10hORTG + HomeLast10aDRTG)/200)*h2hPaceJvR))/2
print(rocketsTotal)

AwaySZNaORTG = float(stats2.loc['Utah Jazz']['OffRtg'])
AwaySZNhDRTG = float(stats.loc['Houston Rockets']['DefRtg'])
AwaySZNaPace = float(stats2.loc['Utah Jazz']['PACE'])
AwayLast10aORTG = float(stats4.loc['Utah Jazz']['OffRtg'])
AwayLast10hDRTG = float(stats3.loc['Houston Rockets']['DefRtg'])
h2hPaceJvR = float(statsJvR.loc['Utah Jazz']['PACE'])
print('Jazz Total')
jazzTotal = ((((AwaySZNaORTG + AwaySZNhDRTG)/200)*AwaySZNaPace)+(((AwayLast10aORTG + AwayLast10hDRTG)/200)*h2hPaceJvR))/2
print(jazzTotal)
Total5 = rocketsTotal + jazzTotal
print('Total =')
print(Total5)
print('Under 228.5')
print('Rockets +15')
print('before OT:234 after:259, +15')

#Thunder vs Nuggets
driver = webdriver.Firefox()
url = r"https://www.nba.com/stats/teams/advanced/?sort=W&dir=-1&Season=2021-22&SeasonType=Regular%20Season&OpponentTeamID=1610612743&TeamID=1610612760"
driver.get(url)
print("Implicit Wait Example")
time.sleep(4)

src = driver.page_source
parser = BeautifulSoup(src, "lxml")
table = parser.find("div", attrs = {"class": "nba-stat-table__overflow"})
   
rows = table.findAll('tr')[1:]
player_statsTvN = [[td.getText().strip() for td in rows[i].findAll('td')[1:]] for i in range(len(rows))]
pd.set_option('max_columns', None)
statsTvN = pd.DataFrame(player_statsTvN, columns=headerlist1)
statsTvN.set_index("TEAM", inplace = True)
HomeSZNhORTG = float(stats.loc['Denver Nuggets']['OffRtg'])
HomeSZNaDRTG = float(stats2.loc['Oklahoma City Thunder']['DefRtg'])
HomeSZNhPace = float(stats.loc['Denver Nuggets']['PACE'])
HomeLast10hORTG = float(stats3.loc['Denver Nuggets']['OffRtg'])
HomeLast10aDRTG = float(stats4.loc['Oklahoma City Thunder']['DefRtg'])
h2hPaceTvN = float(statsTvN.loc['Oklahoma City Thunder']['PACE'])
print('Nuggets Total')
nuggetsTotal = ((((HomeSZNhORTG + HomeSZNaDRTG)/200)*HomeSZNhPace)+(((HomeLast10hORTG + HomeLast10aDRTG)/200)*h2hPaceTvN))/2
print(nuggetsTotal)

AwaySZNaORTG = float(stats2.loc['Oklahoma City Thunder']['OffRtg'])
AwaySZNhDRTG = float(stats.loc['Denver Nuggets']['DefRtg'])
AwaySZNaPace = float(stats2.loc['Oklahoma City Thunder']['PACE'])
AwayLast10aORTG = float(stats4.loc['Oklahoma City Thunder']['OffRtg'])
AwayLast10hDRTG = float(stats3.loc['Denver Nuggets']['DefRtg'])
h2hPaceTvN = float(statsTvN.loc['Oklahoma City Thunder']['PACE'])
print('Thunder Total')
thunderTotal = ((((AwaySZNaORTG + AwaySZNhDRTG)/200)*AwaySZNaPace)+(((AwayLast10aORTG + AwayLast10hDRTG)/200)*h2hPaceTvN))/2
print(thunderTotal)
Total6 = nuggetsTotal + thunderTotal
print('Total =')
print(Total6)
print('Under 225.5')
print('OKC +15')
print("actual 226, +15")


      
