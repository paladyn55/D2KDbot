#rly long function which should create a list which you can use to manually update csvs
import statget
def arr_load(file):
	arr = []
	for line in file:
		arr.append(line)
	return arr
	
def longupdate():
	n = arr_load(open('DiscNameT.txt', 'r', encoding='utf-8'))
	u = arr_load(open('D2TpageT.txt', 'r', encoding='utf-8'))
	for url in u:
		ind = u.index(url)
		arr_s = statget.stat_check_(url)
		arr_usr = [n[ind], url, arr_s[0], arr_s[1], arr_s[2], arr_s[3]]
		st_n = (arr_usr[2] + arr_usr[3] + arr_usr[4] + arr_usr[5])/4
		arr_usr.append(st_n)
		print(arr_usr)
		arr_usr[0].remove("\n")
		print(arr_usr)
		
