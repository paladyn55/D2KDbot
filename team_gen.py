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
def team_create():
	lobby = arr_load(open("lobby.txt", 'r', encoding='utf-8'))
	if len(lobby)%3 != 0:
		print("uneven number of players for teams of 3")
	else:
		c = open('statsT.csv', 'r', encoding='utf-8')
		cr = csv.reader(c)
		usr_arr_t = csv_arr(cr)
		arr_usrs = []
		for usr in lobby:
			for row in usr_arr_t:
				usr = usr.strip('\n')
				if usr in row:
					arr_usrs.append(row)
		arr_usr_srt = sorted(arr_usrs,key=lambda l:l[6], reverse=True)
		team_c1 = []
		team_c2 = []
		team_c3 = []
		ind = 0
		len_ = int((len(arr_usr_srt))/3)
		arr_teams = []
		for i in range(len_):
			team_c1.append(arr_usr_srt[ind])
			ind += 1
		for i in range(len_):
			team_c2.append(arr_usr_srt[ind])
			ind += 1
		for i in range(len_):
			team_c3.append(arr_usr_srt[ind])
			ind += 1
		for i in team_c1:
			ind = team_c1.index(i)
			arr = [i, team_c2[ind], team_c3[ind]]
			arr_teams.append(arr)
		return arr_teams