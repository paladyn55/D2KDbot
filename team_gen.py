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


def team_create(people_per_team):
	lobby = arr_load(open("lobby.txt", 'r', encoding='utf-8'))
	if len(lobby)%3 != 0:
		print("uneven number of players for teams of 3")
	else:
		
		arr_usrs = []
		for usr in lobby:
			for row in usr_arr_t:
				usr = usr.strip('\n')
				if usr in row:
					arr_usrs.append(row)
		arr_usr_srt = sorted(arr_usrs,key=lambda l:l[6], reverse=True)
		number_teams = len(arr_usr_srt)//people_per_team
		teams = []
		for _ in range(number_teams):
			teams.append([])

		while len(arr_usr_srt) > 0:
			for team in teams:
				team.append(arr_usr_srt.pop(0))
			teams = invert_array(teams)
		return teams
