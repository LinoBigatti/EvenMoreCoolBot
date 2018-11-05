import discord
import time
import json

x = 1

bot = discord.Client()

config_raw = open("config.json", "r")
config = json.load(config_raw)

TOKEN = config["token"]

bot.run(TOKEN)

@bot.event
async def on_ready():
	print('Coolbot++ - a bot by L!no')
	print('Logged in as')
	print(client.user.name)
	print(client.user.id)
	print('------')

while(1):
	while x != 3:
		x += 1
		print(x)
		time.sleep(1)
	while x != 1:
		x -= 1
		print(x)
		time.sleep(1)
