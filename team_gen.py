#this file works, dont change it please
import csv
def arr_load(file):
	arr = []
	for line in file:
		arr.append(line)
	return arr

def csv_arr(csv_o):
  arr = []
  for row in csv_o:
    arr.append(row)
  return arr

def invert_array(array):
  inverted = []
  for i in range(len(array)):
    inverted.append(array.pop())
  return inverted

def snake_draft(ordered_players, people_per_team):
    number_teams = len(ordered_players)//people_per_team
    teams = []
    for _ in range(number_teams):
        teams.append([])
    
    while len(ordered_players) > 0:
        for team in teams:
            team.append(ordered_players.pop(0))
        teams = invert_array(teams)
    
    return teams


def teamgen():
	import getPlayerStats
	lobby = arr_load(open("lobby.txt", 'r', encoding='utf-8'))
	if len(lobby)%3 != 0:
		print("uneven number of players for teams of 3")
	else:
		f = open("names.csv",mode='r',encoding='utf-8')
		csv_o = csv.reader(f)
		usr_arr = csv_arr(csv_o)
		b_name_lobby = []
		l = open('lobby.txt', 'r')
		for line in l:
			for usr in usr_arr:
				if line.strip('\n') == usr[0]:
					b_name_lobby.append(usr)
		for usr in b_name_lobby:
			usr.append(getPlayerStats.stat_get(usr[1], usr[2]))
		ordered_players = sorted(b_name_lobby,key=lambda l:l[3], reverse=False)
		return snake_draft(ordered_players, 3)
  