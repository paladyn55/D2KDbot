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
	#print(str(people_per_team))
	number_teams = len(ordered_players)//people_per_team
	teams = []
	for _ in range(number_teams):
		teams.append([])
	
	while len(ordered_players) > 0:
		for team in teams:
			team.append(ordered_players.pop(0))
		teams = invert_array(teams)
	return teams


def teamgen(lobby, num):
	import getPlayerStats
	#print("Snake Lobby:",lobby)
	f = open("names.csv",mode='r',encoding='utf-8')
	csv_o = csv.reader(f)
	usr_arr = csv_arr(csv_o)
	b_name_lobby = []
	for player in lobby:
		#print(player)

		if player == "Singham, Son of Iron Lord Mikey#7874":
			temp_arr = ['Singham, Son of Iron Lord Mikey#7874','Cudotza²','#8174']
			b_name_lobby.append(temp_arr)
		for usr in usr_arr:
			
			if player.strip('\n') == usr[0]:
				b_name_lobby.append(usr)
	#print(b_name_lobby)
	for usr in b_name_lobby:
		print(usr)
		usr.append(getPlayerStats.stat_get(usr[1], usr[2]))
	ordered_players = sorted(b_name_lobby,key=lambda l:l[3], reverse=False)
	print(ordered_players)
	teams = snake_draft(ordered_players, num)
	#print(teams)
	return teams