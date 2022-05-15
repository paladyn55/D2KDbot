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
	return arr_usr_srt