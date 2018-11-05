import discord
from discord.ext.commands import Bot
import time
import json

x = 0xffffff

bot = Bot("c!")

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

@bot.command(pass_context=True)
async def start(ctx, Role : discord.Role):
	await bot.edit_role(ctx.message.server, Role, colour=discord.Colour(x))
	await bot.say("Success!")

def main():
	bot.run(TOKEN)

main()
