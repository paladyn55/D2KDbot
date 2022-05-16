#command list
#register - ties discord username to trackernetwork page /
#start lobby - opens a lobby file which users can join
#clear lobby - clears lobby file
#lobby begin - makes teams with a given number of teams
#statupdate - updates stat values for every member
from discord.ext import commands
import os
import statget
import csv
import team_gen
lobby_inst = False

def usr_add(usr):
	file = open('stattemp.csv', mode='a', encoding='utf-8')
	writer = csv.writer(file, delimiter=',')
	writer.writerow(usr)
	file.close()

def stat_add_one(name, url):
	arr_s = statget.stat_check(url, 10, 40)
	arr_usr = [name, url, arr_s[0], arr_s[1], arr_s[2], arr_s[3]]
	st_n = arr_usr[2] + arr_usr[3] + arr_usr[4] + arr_usr[5]
	arr_usr.append(st_n)

def get_ratings_all():
	statcsv = open("stats.csv", mode='r', encoding = "utf-8")
	arr = csv.reader(statcsv)
	urls = []
	names = []
	for row in arr:
		names.append(row[0])
		urls.append(row[1])
	statcsv.close()
	for url in urls:
		ind = urls.index(url)
		arr_s = statget.stat_check(url, 5, 30)
		arr_usr = [names[ind], url, arr_s[0], arr_s[1], arr_s[2], arr_s[3]]
		st_n = (arr_usr[2] + arr_usr[3] + arr_usr[4] + arr_usr[5])/4
		arr_usr.append(st_n)
		print(arr_usr)
		arr_usr[0].remove("\n")
		usr_add(arr_usr)
	c1 = open("stats.csv", mode='w', encoding='utf-8')
	c2 = open("stattemp.csv", mode='r', encoding="utf-8")
	w = csv.writer(c1, delimiter=',')
	r = csv.reader(c2)
	for row in r:
		w.writerow(row)

def arr_load(file):
	arr = []
	for line in file:
		arr.append(line)
	return arr

def in_check(csv_o, str):
	in_tr = 0
	for row in csv_o:
		if str in row:
			in_tr = 1
	return in_tr
	
#replit
TOKEN = os.environ["TOKEN"]
#VSC
#path = 'C:\\Users\\josep\\Documents\\TOKEN.txt'
#T = open(path, 'r')
#print(T)
prefix = "&"
bot = commands.Bot(prefix)

@bot.event
async def on_ready():
  print("------- Bot is ready -------")

@bot.command()
async def register(ctx, arg):
	names = open("DiscNameT.txt", 'r')
	usr = str(ctx.author) + '\n'
	if usr not in names:
		names.close()
		stat_add_one(usr, arg)
		await ctx.reply("registered")
		print(str(ctx.author) + " registered")
	else:
		await ctx.reply("already registered")
		names.close()

@bot.command()
async def lobby(ctx, arg):
	global lobby_inst
	if str(arg) == "start":
		print(str(ctx.author) + " started a lobby")
		lobby_inst = True
		await ctx.reply("lobby started")
	if str(arg) == "join":
		if lobby_inst == True:
			c = open('stats.csv', 'r')
			cr = csv.reader(c)
			if in_check(cr, str(ctx.author)) == 1:
				l = open("lobby.txt", 'r')
				if str(ctx.author) in l:
					lobby = open('lobby.txt', 'a')
					lobby.write(str(ctx.author) + '\n')
					lobby.close()
					await ctx.reply(str(ctx.author) + ' has joined the lobby')
					print(str(ctx.author) + "joined the lobby")
				else:
					await ctx.reply("user has already joined the lobby")
	if str(arg) == 'end':
		a = open("lobby.txt", "w")
		a.close()
		lobby_inst = False
		await ctx.reply("lobby closed")
	if str(arg) == "teamgen":
		team_num = 1
		for team in team_gen.team_create():
			await ctx.reply(f"team {str(team_num)}:\n{team[0][0]}\n{team[1][0]}\n{team[2][0]}")
			team_num += 1
#---------------------
#bot.run(TOKEN)
#get_ratings_all()
#statgetlong.longupdate()