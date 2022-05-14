import csv
def team_create():
	lobby = open("lobby.txt", 'r')
	c = open('statsT.csv', 'r')
	cr = csv.reader(c)
	arr_usrs = []
	for usr in lobby:
		print(usr)
	for row in cr:
		print(row)
	for u in lobby:
		for row in cr:
			if row[0] == u:
				arr_usrs.append(row)
	print(arr_usrs)