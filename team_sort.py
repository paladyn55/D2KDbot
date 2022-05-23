def invert_array(array):
  inverted = []
  for i in range(len(array)):
    inverted.append(array.pop())
  return inverted
def csv_arr(csv_o):
  arr = []
  for row in csv_o:
    arr.append(row)
  return arr
	
def sort_list(arr_usrs):
	print('1')
	import getPlayerStats
	import csv
	f = open("names.csv",mode='r',encoding='utf-8')
	csv_o = csv.reader(f)
	usr_arr = csv_arr(csv_o)
	lobby_b_names = []
	for usr in usr_arr:
		print(usr)
	for usr in lobby_b_names:
		usr.append(getPlayerStats.stat_get(usr[1], usr[2]))
		print('2')
	print(lobby_b_names)
	return lobby_b_names

def snake_draft(ordered_players, people_per_team):
	print('3')
	number_teams = len(ordered_players)//people_per_team
	teams = []
	for _ in range(number_teams):
		teams.append([])
  
	while len(ordered_players) > 0:
		for team in teams:
			team.append(ordered_players.pop(0))
		teams = invert_array(teams)
	print('4')
	print(teams)
	return teams

#people = []
#snake_draft(people, 3)