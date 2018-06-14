import discord
import random
import asyncio
import json
from discord.ext import commands
import aiohttp



insult = ["If laughter is the best medicine, your face must be curing the world.", 
"You're so ugly, you scared the crap out of the toilet.",
'Your family tree must be a cactus because everybody on it is a prick.',
"No I'm not insulting you, I'm describing you.",
"It's better to let someone think you are an Idiot than to open your mouth and prove it.",
"If I had a face like yours, I'd sue my parents.",
"Your birth certificate is an apology letter from the condom factory.",
'I guess you prove that even god makes mistakes sometimes.',
"The only way you'll ever get laid is if you crawl up a chicken's ass and wait.",
"You're so fake, Barbie is jealous.",
"I’m jealous of people that don’t know you!",
"My psychiatrist told me I was crazy and I said I want a second opinion. He said okay, you're ugly too.",
"You're so ugly, when your mom dropped you off at school she got a fine for littering.",
"If I wanted to kill myself I'd climb your ego and jump to your IQ.",
"You must have been born on a highway because that's where most accidents happen.",
"Brains aren't everything. In your case they're nothing.",
"I don't know what makes you so stupid, but it really works.",
'I can explain it to you, but I can’t understand it for you.',
"Roses are red violets are blue, God made me pretty, what happened to you?",
'Behind every fat woman there is a beautiful woman. No seriously, your in the way.',
'Calling you an idiot would be an insult to all the stupid people.',
"You, sir, are an oxygen thief!",
"Some babies were dropped on their heads but you were clearly thrown at a wall.",
"Don't like my sarcasm, well I don't like your stupid.",
"Why don't you go play in traffic.",
"Please shut your mouth when you’re talking to me.",
"I'd slap you, but that would be animal abuse.",
"They say opposites attract. I hope you meet someone who is good-looking, intelligent, and cultured.",
"Stop trying to be a smart ass, you're just an ass.",
'The last time I saw something like you, I flushed it.',
"'m busy now. Can I ignore you some other time?",
"You have Diarrhea of the mouth; constipation of the ideas.",
"If ugly were a crime, you'd get a life sentence.",
"Your mind is on vacation but your mouth is working overtime.",
'I can lose weight, but you’ll always be ugly.',
"Why don't you slip into something more comfortable... like a coma.",
"Shock me, say something intelligent.",
"If your gonna be two faced, honey at least make one of them pretty.",
"Keep rolling your eyes, perhaps you'll find a brain back there.",
"You are not as bad as people say, you are much, much worse.",
"I don't know what your problem is, but I'll bet it's hard to pronounce.",
"You get ten times more girls than me? ten times zero is zero...",
"There is no vaccine against stupidity.",
"You're the reason the gene pool needs a lifeguard.",
"Sure, I've seen people like you before - but I had to pay an admission.",
"How old are you? - Wait I shouldn't ask, you can't count that high.",
"Have you been shopping lately? They're selling lives, you should go get one.",
"You're like Monday mornings, nobody likes you.",
"Of course I talk like an idiot, how else would you understand me?",
"All day I thought of you... I was at the zoo.",
"To make you laugh on Saturday, I need to you joke on Wednesday.",
"You're so fat, you could sell shade.",
"I'd like to see things from your point of view but I can't seem to get my head that far up my ass.",
"Don't you need a license to be that ugly?",
"Your house is so dirty you have to wipe your feet before you go outside.",
"If you really spoke your mind, you'd be speechless.",
"Stupidity is not a crime so you are free to go.",
"If I told you that I have a piece of dirt in my eye, would you move?",
"You're so dumb that you got hit by a parked car.",
"You're so fat, you leave footprints in concrete.",
"Wipe your mouth, there's still a tiny bit of bullshit around your lips.",
"Are you always this stupid or is today a special occasion?",
]



ball = ["As I see it, yes", "It is certain", "It is decidedly so", "Most likely", "Outlook good",
                     "Signs point to yes", "Without a doubt", "Yes", "Yes – definitely", "You may rely on it", "Reply hazy, try again",
                     "Ask again later", "Better not tell you now", "Cannot predict now", "Concentrate and ask again",
"Don't count on it", "My reply is no", "My sources say no", "Outlook not so good", "Very doubtful"]




class fun:
    def __init__(self, bot):
        self.bot = bot
        


    @commands.command()
    async def insult(self, ctx, user : discord.Member):
        """Insult the user"""
        msg = ' '
        if user == None:
            await ctx.send(ctx.message.author.mention + msg + random.choice(insult))
        elif user.id == self.bot.user.id:
            await ctx.send("Well you tried to Insult such an awesome bot, so here is credit." )
            await ctx.send(ctx.message.author.mention + msg + random.choice(insult))
        elif user.id == 374608196943347712:
            await ctx.send("Wow, I guess you are biggest stupid in server, comeon who dares to insult Creator.")
            await ctx.send(ctx.message.author.mention + msg + random.choice(insult))
        else:
            await ctx.send(user.mention + msg + random.choice(insult))
        



    @commands.command()
    async def hug(self, ctx, *,member : discord.Member = None):
        if member is None:
            await ctx.send(ctx.message.author.mention + " has been hugged! 💘 ")
        else:
            if member.id == ctx.message.author.id:
                await ctx.send (ctx.message.author.mention + " hugged themselve because they are a loner 🤦 ")
            else:
                await ctx.send(member.mention + " was hugged by " + ctx.message.author.mention + " 💝 ")




    @commands.command(pass_context=True)
    async def coinflip(self, ctx):
        '''Select Random'''
        choice = random.randint(1,2)
        if choice == 1:
            await ctx.send("Tails")
        else:
            await ctx.send("Heads")

    



    @commands.command(description='Lets see, what bot prefers')
    async def choose(self, ctx, *choices : str):
        """Chooses between multiple choices."""
        await ctx.send(random.choice(choices))


    @commands.command()
    async def kill(self, ctx, *, member: discord.Member = None):
        if member is None:
            embed=discord.Embed(title="No one to kill!", description="You havent mentioned anyone to kill!", color=0xff0000)
            embed.set_thumbnail(url="http://i.imgur.com/6YToyEF.png")
            embed.set_footer(text = "I thought you are not enough stupid")
            await ctx.send(embed=embed)
        elif member.id == ctx.message.author.id:
            embed=discord.Embed(title="Call this number", description="1-800-784-2433", color=0xff0000)
            embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/thumb/f/fa/NHS-Logo.svg/1200px-NHS-Logo.svg.png")
            embed.set_image(url="http://4.bp.blogspot.com/-FL6mKTZOk94/UBb_9EuAYNI/AAAAAAAAOco/JWsTlyInMeQ/s400/Jean+Reno.gif")
            embed.set_footer(text="~~You are good~~")
            await ctx.send(embed=embed)
        else:
            embed=discord.Embed(title="Killed!", description="{} Was killed by {} OOF ".format(member.mention, ctx.message.author.name),color=0x00ff00)
            embed.set_image(url="https://media.giphy.com/media/kOA5F569qO4RG/giphy.gif")
            embed.set_footer(text= "RIP")
            await ctx.send(embed=embed)



    @commands.command(name="8", aliases=["8ball"])
    async def eightball(self, ctx, *, question : str):
        "When u dont know what is good"
        if question.endswith("?") and question != "?":
            await ctx.send("`" + random.choice(ball) + "`")
        else:
            await ctx.send("`That dosen't looks like a question`")
    

    @commands.command()
    async def gay(self, ctx, user :  discord.Member = None):
        '''Find out Gay Character'''
        if user != None and user.id == 374608196943347712:
            await ctx.send("I guess, " + ctx.message.author.mention + " is " +  str(100) + " % gay." )
        elif user != None:
            await ctx.send(user.mention + " You are " + str(random.randint(1,101)) + "% gay." )
        else:
            await ctx.send(ctx.message.author.mention + " You are " + str(random.randint(1,101)) + "% gay.")




    
    
    @commands.command(pass_context=True, no_pm=True)
    async def stupid(self, ctx, user : discord.Member = None):
        """Check Whether Mentioned user is stupid"""
        if user != None:
            if ctx.message.author.id == 374608196943347712:
                await ctx.send(f'Oh, Creator! You\'re the intelligent person I\'ve ever seen! You definitely are right! {user.mention} is really stupid!')
            elif user.id == self.bot.user.id:
                await ctx.send('I am smart enough to understand you tried to troll me... Believe me, the stupid here is you, not me!')
            elif user.id == 374608196943347712:
                await ctx.send(ctx.message.author.mention + " Ofc, you are stupid, if you are saying stupid to Creator of this bot.")
            else:
                await (f'Hmm perhaps, I\'m not sure if {user.mention} is stupid, but I\'m sure YOU are!')
        else:
            await ctx.send(ctx.message.author.mention + "No Doubt, you are ofc Stupid, if you didn't mentioned anyone.")
    @commands.command()
    async def face(self, ctx):
        faces=["¯\_(ツ)_/¯", "̿̿ ̿̿ ̿̿ ̿'̿'\̵͇̿̿\З= ( ▀ ͜͞ʖ▀) =Ε/̵͇̿̿/’̿’̿ ̿ ̿̿ ̿̿ ̿̿", "( ͡°( ͡° ͜ʖ( ͡° ͜ʖ ͡°)ʖ ͡°) ͡°)", "ʕ•ᴥ•ʔ", "(▀̿Ĺ̯▀̿ ̿)", "(ง ͠° ͟ل͜ ͡°)ง", "༼ つ ◕_◕ ༽つ", "ಠ_ಠ", "(づ｡◕‿‿◕｡)づ", "̿'̿'\̵͇̿̿\З=( ͠° ͟ʖ ͡°)=Ε/̵͇̿̿/'̿̿ ̿ ̿ ̿ ̿ ̿", "(ﾉ◕ヮ◕)ﾉ*:･ﾟ✧ ✧ﾟ･: *ヽ(◕ヮ◕ヽ)", "┬┴┬┴┤ ͜ʖ ͡°) ├┬┴┬┴", "( ͡°╭͜ʖ╮͡° )", "(͡ ͡° ͜ つ ͡͡°)", "(• ε •)", "(ง'̀-'́)ง", "(ಥ﹏ಥ)", "(ノಠ益ಠ)ノ彡┻━┻", "[̲̅$̲̅(̲̅ ͡° ͜ʖ ͡°̲̅)̲̅$̲̅]", "(ﾉ◕ヮ◕)ﾉ*:･ﾟ✧", "(☞ﾟ∀ﾟ)☞", "| (• ◡•)| (❍ᴥ❍ʋ)", "(◕‿◕✿)", "(ᵔᴥᵔ)", "(¬‿¬)", "(☞ﾟヮﾟ)☞ ☜(ﾟヮﾟ☜)", "(づ￣ ³￣)づ", "ლ(ಠ益ಠლ)", "ಠ╭╮ಠ", "̿ ̿ ̿'̿'\̵͇̿̿\з=(•_•)=ε/̵͇̿̿/'̿'̿ ̿", "(;´༎ຶД༎ຶ`)", "༼ つ  ͡° ͜ʖ ͡° ༽つ", "(╯°□°）╯︵ ┻━┻"]
        face=random.choice(faces)
        await ctx.send(face)

    @commands.command()
    async def tableflip(self, ctx):
        x = await ctx.send(content="┬─┬ノ( º _ ºノ)")
        await asyncio.sleep(1)
        await x.edit(content='(°-°)\\ ┬─┬')
        await asyncio.sleep(1)
        await x.edit(content='(╯°□°)╯    ]')
        await asyncio.sleep(0.2)
        await x.edit(content='(╯°□°)╯  ︵  ┻━┻')
      
      
    @commands.command()
    async def meme(self, ctx):
        """Pulls a random meme from r/me_irl"""
        async with aiohttp.ClientSession() as session:
            async with session.get("https://api.reddit.com/r/me_irl/random") as r:
		data = await r.json()
                await ctx.send(data[0]["data"]["children"][0]["data"]["url"])
     


def setup(bot):
    bot.add_cog(fun(bot))
                
