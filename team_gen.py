import csv
def arr_load(file):
	arr = []
	for line in file:
		arr.append(line)
	return arr
def team_create():
    lobby = arr_load(open("lobby.txt", 'r', encoding='utf-8'))
    c = open('statsT.csv', 'r', encoding='utf-8')
    cr = csv.reader(c)
    arr_usrs = []
    print(lobby)
    for usr in lobby:
        print("there should be 6 of these")
        for row in cr:
            usr = usr.strip('\n')
            print(row[0])
            if usr in row:
                arr_usrs.append(row)
    return arr_usrs