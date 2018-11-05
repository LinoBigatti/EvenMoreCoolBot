import discord
import time
import json

x = 1

bot = discord.Client()

config_raw = open("config.json", "r")
config = json.load(config_raw)

TOKEN = config["token"]

@bot.event
async def on_ready():
	print('Coolbot++ - a bot by L!no')
	print('Logged in as')
	print(bot.user.name)
	print(bot.user.id)
	print('------')

def main():
	bot.run(TOKEN)

main()
