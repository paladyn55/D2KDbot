#command list
#register - ties discord username to bungie username
#start lobby - opens a lobby file which users can join
#clear lobby - clears lobby file
#lobby begin - makes teams with a given number of teams

from discord.ext import commands
import os
import csv
import team_gen

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
	
TOKEN = os.environ['TOKEN']
prefix = "&"
bot = commands.Bot(prefix)

@bot.event
async def on_ready():
  print("------- Bot is ready -------")

@bot.command()
async def register(ctx, arg):
	f = open('names.csv',mode='r',encoding='utf-8')
	csv_o = csv.reader(f)
	usr_arr = csv_arr(csv_o)
	check = 0
	for line in usr_arr:
		print(line)
		if line[0] == str(ctx.author):
			check = 1
	if check == 0:
		f.close
		f = open('names.csv',mode='a',encoding='utf-8')
		cw = csv.writer(f)
		usr = str(ctx.author)
		b_name, b_num = arg.split('#')
		usr_t = [usr, b_name, b_num]
		cw.writerow(usr_t)
		await ctx.reply('registered')
	else:
		await ctx.reply("already registered")

lobby_arr = ["<paladyn>#8056", "Singham, Son of Iron Lord Mikey#7874", "DLH3LIX#6618", "Generic#0866", "iDarknesslll#7448", "ReapersStrike#0108"]
lobby_inst = False

@bot.command()
async def lobby(ctx, arg):
	global lobby_inst
	global lobby_arr
#---------------------------------------------------------------------
	if arg == "start":
		print(str(ctx.author) + " started a lobby")
		lobby_inst = True
		await ctx.reply("lobby started")
#---------------------------------------------------------------------
	if arg == "join":
		if lobby_inst == True:
			check = 0
			for usr in lobby_arr:
				if usr == str(ctx.author):
					check = 1
			if check == 0:
				lobby_arr.append(str(ctx.author))
				await ctx.reply(str(ctx.author) + ' has joined the lobby')
				print(str(ctx.author) + "joined the lobby")
				print(f"lobby: {lobby_arr}")
			else:
				await ctx.reply("user has already joined the lobby")
		else:
			await ctx.reply("no")
#---------------------------------------------------------------------
	if arg == "leave":
		if str(ctx.author) in lobby_arr:
			lobby_arr.remove(str(ctx.author))
			await ctx.reply(f"{str(ctx.author)} removed from lobby")
		else:
			await ctx.reply("user not in lobby")
#---------------------------------------------------------------------
	if arg == "check":
		print(lobby_arr)
		for usr in lobby_arr:
			await (ctx.author).send(usr)
#---------------------------------------------------------------------
	if arg == 'end':
		lobby_inst = False
		lobby_arr = []
		await ctx.reply("lobby closed")
@bot.command()
async def lobbyadd(ctx, arg):
	global lobby_inst
	global lobby_arr
	if lobby_inst == True:
		if arg == 'Alice':
			lobby_arr.append('Alice ❤#9033')
			await ctx.reply("Alice ❤#9033 added")
		if arg == 'Zewps':
			lobby_arr.append('Alice ❤#9033')
			await ctx.reply("Alice ❤#9033 added")
		else:	
			lobby_arr.append(arg)
			await ctx.reply(f"{arg} added")
		print(lobby_arr)
@bot.command()
async def teamgen(ctx, arg):
	global lobby_inst
	global lobby_arr
	if lobby_inst == True:
		num = 1
		teams = team_gen.teamgen(lobby_arr, int(arg))
		for team in teams:
			names = []
			for usr in team:
				names.append(usr[0])
			await ctx.reply(f"team {num}: {names}")
			num += 1
		print(teams)
#---------------------

bot.run(TOKEN)