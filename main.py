#command list
#register - ties discord username to trackernetwork page /
#start lobby - opens a lobby file which users can join
#clear lobby - clears lobby file
#lobby begin - makes teams with a given number of teams
#statupdate - updates stat values for every member
from discord.ext import commands
import os
import api_get
import csv
import team_gen
import getPlayerStats
lobby_inst = False

def usr_add(usr):
	file = open('stattemp.csv', mode='a', encoding='utf-8')
	writer = csv.writer(file, delimiter=',')
	writer.writerow(usr)
	file.close()

# make register function

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
	usrs = open("players.txt", 'r')
	list_player = []
	for i in usrs:
		list_player.append(i)
	check = 0
	for i in list_player:
		if i[0] == str(ctx.author):
			check = 1
	
	if check == 1:
		usrs.close()
		#register function
		await ctx.reply("registered")
		print(str(ctx.author) + " registered")
	else:
		await ctx.reply("already registered")
		usrs.close()

@bot.command()
async def lobby(ctx, arg):
	global lobby_inst

	input = arg.split(" ")

	if str(input[0]) == "start":
		print(str(ctx.author) + " started a lobby")
		lobby_inst = True
		await ctx.reply("lobby started")
	if str(input[0]) == "join":
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
	if str(input[0]) == 'end':
		a = open("lobby.txt", "w")
		a.close()
		lobby_inst = False
		await ctx.reply("lobby closed")
	if str(input[0]) == "teamgen":
		team_num = 1
		for team in team_gen.team_create(input[1]):
			await ctx.reply(f"team {str(team_num)}:\n{team[0][0]}\n{team[1][0]}\n{team[2][0]}")
			team_num += 1
#---------------------
#bot.run(TOKEN)
#VSC
#get_ratings_all(1)
#replit:
#get_ratings_all(2)
#api_get.stat_get("4611686018478013482", "2")
#getPlayerStats.stat_get()
c = open('new.csv', 'r', encoding='utf-8')
csv_o = csv.reader(c)
usr_arr = csv_arr(csv_o)
for usr in usr_arr:
	getPlayerStats.stat_get(usr[1], usr[2])