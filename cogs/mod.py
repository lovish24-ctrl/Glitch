import discord
from discord.ext import commands
import asyncio

 
 
class mod:
    def __init__(self, bot):
        self.bot = bot
 


    @commands.command()
    @commands.has_permissions(kick_members = True)
    async def mute(self, ctx, user : discord.User, time = None):
        if time != None:
            time = int(time)
            t = time * 60
            await ctx.channel.set_permissions(user, send_messages=False)
            ctx.send(f"Done, {user.mention} is now muted and will be unmuted after str{time}minutes!")
            await asyncio.sleep(t)
            await ctx.channel.set_permissions(user, send_messages=True)
        else:
            await ctx.channel.set_permissions(user, send_messages=False)
            ctx.send(f"Done, {user.mention} is now permanently muted.")
    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def unmute(self, ctx, user: discord.Member):
        '''Unmute someone'''
        await ctx.channel.set_permissions(user, send_messages=True)   
        ctx.send(f"Done, {user.mention} is unmuted") 

            
 
 
 
    @commands.command()
    @commands.has_permissions(administrator = True)
    async def dm(self, ctx, user: discord.Member, *, message):
        """DM someone xD"""
        await user.send(str(message))
        await ctx.message.delete()            
        await ctx.send("It was at time. :white_check_mark: ")

        



    @commands.command()
    @commands.has_permissions(kick_members = True)
    async def warn(self, ctx, user: discord.Member, *, reason):
        """Sends that warning."""
        embed = discord.Embed(color=0xf52338, title=f"WARNING: by {ctx.message.author.name} from **{ctx.author.guild.name}**.", description=f" Reason ==> {reason}")
        await user.send(embed=embed)
        await ctx.message.delete

    @commands.command()
    @commands.has_permissions(kick_members = True)
    async def kick(self, ctx, user : discord.Member, *, reason = None):
        '''OFC kick anyone'''
        if reason != None:
            await ctx.send(f"Done, {user} is kicked, reason = {reason} ")
            embed=discord.Embed(title=f"Kicked From **{ctx.author.guild.name}**", color=0xf52338)
            embed.set_author(name=f"You have been kicked from **{ctx.author.guild.name}** by **{ctx.message.author.name}**, Reason ==> **{reason}**!")
            await user.send(embed=embed)
            await ctx.guild.kick(user, reason = reason)
            
        else:
            await ctx.send(f"Done, {user} is kicked, reason = Unspecified ")
            embed=discord.Embed(title=f"Kicked From **{ctx.author.guild.name}**", color=0xf52338)
            embed.set_author(name=f"You have been kicked from **{ctx.author.guild.name}** by **{ctx.message.author.name}**, Reason ==> **Not Specified**!")
            await user.send(embed=embed)
            await ctx.guild.kick(user, reason = reason)
            
        

    @commands.command()
    @commands.has_permissions(ban_members = True)
    async def ban(self, ctx, user : discord.User, *, reason = None):
        if reason != None:
            await ctx.send(f"Done, {user} is banned, reason = {reason} ")
            embed=discord.Embed(title=f"Banned From **{ctx.author.guild.name}**", color=0xf52338)
            embed.set_author(name=f"You have been Banned from **{ctx.author.guild.name}** by **{ctx.message.author.name}**, Reason ==> **{reason}**!")
            await user.send(embed=embed)
            await ctx.guild.ban(user, reason = reason)
        else:
            await ctx.send(f"Done, {user} is banned, reason = {reason} ")
            embed=discord.Embed(title=f"Banned From **{ctx.author.guild.name}**", color=0xf52338)
            embed.set_author(name=f"You have been Banned from **{ctx.author.guild.name}** by **{ctx.message.author.name}**, Reason ==> **Not Specified**!")
            await user.send(embed=embed)
            await ctx.guild.ban(user, reason = reason)
    

    @commands.command()
    @commands.has_permissions(manage_messages = True)
    async def clear(self, ctx, x):
        """Deletes msgs."""
        x = int(x)
        await ctx.channel.purge(limit=x+1)
        msg = await ctx.send(f"Deleted `{x}` messages", delete_after = 5 )






    

























def setup(bot):
    bot.add_cog(mod(bot))
                
