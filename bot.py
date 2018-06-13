import discord 
from discord.ext import commands
import time
import os




bot = commands.Bot(command_prefix='e.', description="An easy to use discord bot")
bot.load_extension("cogs.fun")
bot.load_extension("cogs.utility")
bot.load_extension("cogs.mod")



@bot.event
async def on_ready():
	print('Logged in as'+ bot.user.name)
	print(bot.user.id)
	print('------')




bot.run(os.environ.get("TOKEN"))
