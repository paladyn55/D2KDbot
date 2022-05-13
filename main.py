#command list
#register - ties discord username to trackernetwork page /
#start lobby - opens a lobby file which users can join
#clear lobby - clears lobby file
#lobby begin - makes teams with a given number of teams
#statupdate - updates stat values for every member
from discord.ext import commands
import discord
import random as ran
import os
import statgetse
import requests
from requests import get
import csv
lobby_inst = False

def usr_add(usr):
    file = open('stats.csv', mode='w', encoding='utf-8')
    writer = csv.writer(file, delimiter=',')
    writer.writerow(usr)
    file.close()

def stat_add_one(name, url):
	n = open("DiscName.txt", 'a')
	n.write(name)
	n.close()
	u = open("D2Tpage.txt", 'a')
	url = url + '\n'
	u.write(url)
	u.close
	arr_s = statgetse.stat_check(url)
	arr_usr = [name, url, arr_s[0], arr_s[1], arr_s[2], arr_s[3]]
	st_n = arr_usr[2] + arr_usr[3] + arr_usr[4] + arr_usr[5]
	arr_usr.append(st_n)

def get_ratings_all():
		n = arr_load(open('DiscName.txt', 'r', encoding='utf-8'))
		u = arr_load(open('D2Tpage.txt', 'r', encoding='utf-8'))
		for url in u:
				ind = u.index(url)
				arr_s = statgetse.stat_check(url)
				arr_usr = [n[ind], url, arr_s[0], arr_s[1], arr_s[2], arr_s[3]]
				st_n = arr_usr[2] + arr_usr[3] + arr_usr[4] + arr_usr[5]
				arr_usr.append(st_n)
				print(arr_usr)
				arr_usr[0].remove("\n")
				usr_add(arr_usr)

def arr_load(file):
    arr = []
    for line in file:
        arr.append(line)
    return arr

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
    print("Bot is ready!")

@bot.command()
async def register(ctx, arg):
		names = open("DiscName.txt", 'r')
		usr = str(ctx.author) + '\n'
		if usr not in names:
				names.close()
				stat_add_one(usr, arg) # PLZ SORT THIS FUNCTION OUT, just do get_ratings but without the for loop
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
        names = arr_load('DiscName.txt')
        usr = str(ctx.author) + '\n'
        if lobby_inst == True and usr in names:
            lobby = open('lobby.txt', 'a')
            lobby.write(usr)
            lobby.close()
            await ctx.reply(str(ctx.author) + ' has joined the lobby')
    if str(arg) == 'end':
        a = open("lobby.txt", "w")
        a.close()
        lobby_inst = False
        await ctx.reply("lobby closed")

@bot.command()
async def statupdate(ctx):
    print('doing the big boi command')
    get_ratings_all()
#---------------------
#bot.run(TOKEN)