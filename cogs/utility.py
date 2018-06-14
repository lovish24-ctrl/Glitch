import discord
import mtranslate
from discord.ext import commands
import aiohttp




class utility:
	def __init__(self, bot):
		self.bot = bot



	@commands.command()
	@commands.has_permissions(manage_guild = True)
	async def addemoji(self, ctx, name, id):
		'''add new emojis by id'''
		url = f"https://cdn.discordapp.com/emojis/{id}"
		async with self.bot.session.get(url) as resp:
			image = await resp.read()
		done = await ctx.guild.create_custom_emoji(name = name, image = image)
		await ctx.send("Emoji {} created!".format(done))

	@commands.command()
	@commands.has_permissions(manage_guild = True)
	async def createemoji(self, ctx, name, url):
		'''add new emojis by url'''
		async with self.bot.session.get(url) as resp:
			image = await resp.read()
		done = await ctx.guild.create_custom_emoji(name = name, image = image)
		await ctx.send("Emoji {} created!".format(done))
		
	@commands.command()
	async def avatar(self, ctx, user: discord.Member = None):
		"""Gets a avatar"""
		if user == None:
			user = ctx.author
		await ctx.send(user.avatar_url)
		
		
		
	@commands.command()
	@commands.has_permissions(manage_guild = True)
	async def changeprefix(self, ctx, prefix):
		'''Change prefix of your bot in guild'''
		await self.bot.db.config.update_one({"gid" : ctx.guild.id}, {"$set" : {"prefix" : prefix}})
		ctx.send(f"New Prefix of {ctx.guild.name} is {prefix}, You can also change it again by doing {prefix}changeprefix <newprefix>.")





def setup(bot):
    bot.add_cog(utility(bot))



    
    

