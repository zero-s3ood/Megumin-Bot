import discord
import random
import math
import sys
import pytz
import datetime
import requests
import bs4
from datetime import datetime
from discord.ext import commands

client = commands.Bot(command_prefix='.')

from datetime import datetime
from pytz import timezone    


@client.event
async def on_ready():
    print('Bot is ready.')


@client.command()
async def ping(ctx):
    """Returns server ping"""
    await ctx.send(f'Pong! {round(client.latency*1000)}ms')

@client.command()
async def wtime(ctx):
    """World Clock for Chat Memebers"""
    vancouver = timezone('America/Vancouver')
    van = datetime.now(vancouver)
    await ctx.send("The time in Vancouver is " + van.strftime('%H:%M'))
    edmonton = timezone('America/Edmonton')
    ed = datetime.now(edmonton)
    await ctx.send("The time in Fort McMurray is " + ed.strftime('%H:%M'))
    newyork = timezone('America/New_York')
    ny = datetime.now(newyork)
    await ctx.send("The time in New York is " + ny.strftime('%H:%M'))
    Riyadh = timezone('Asia/Riyadh')
    ry = datetime.now(Riyadh)
    await ctx.send("The time in Doha is " + ry.strftime('%H:%M'))
    Lisbon = timezone('Europe/Lisbon')
    ls = datetime.now(Lisbon)
    await ctx.send("The time in Lisbon is " + ls.strftime('%H:%M'))


@client.command()
async def rolla(ctx, arg=0, arg2=0):
    """Rolls 2 dice, returns the max type (optional add a modifier after command)"""
    a=random.randrange(1,20,1)
    b=random.randrange(1,20,1)
    c=max(a,b)+arg
    await ctx.send('(Advantage) You rolled two dice and got: ' +str(a) +' ' +str(b))
    await ctx.send('With Modifiers the highest is:' +str(c) +' The Enemy/Challenge has a rating of: ' +str(arg2))
    if (c<arg2):
        await ctx.send('You fail the roll.')
    else:
        await ctx.send('You pass and do ' +str(c-arg2) + ' damage')
        
@client.command()
async def rolld(ctx, arg=0, arg2=0):
    """Rolls 2 dice, returns the min type (optional add a modifier after command)"""
    a=random.randrange(1,20,1)
    b=random.randrange(1,20,1)
    c=min(a,b)+arg
    await ctx.send('(Disadvantage) You rolled two dice and got: ' +str(a) +' ' +str(b))
    await ctx.send('With Modifiers the score is:' +str(c) +' The Enemy/Challenge has a rating of: ' +str(arg2))
    if (c<arg2):
        await ctx.send('You fail the roll.')
    else:
        await ctx.send('You pass and do ' +str(c-arg2) + ' damage')

@client.command()
async def shadi(ctx):
    """Answers Shadi"""
    await ctx.send('Crimson-black blaze, king of myriad worlds,')
    await ctx.send('though I promulgate the laws of nature, I am the alias of destruction incarnate in accordance with the principles of all creation.')
    await ctx.send('Let the hammer of eternity descend unto me!')
    await ctx.send('Ex--')
    await ctx.send('plosion')
    await ctx.send('https://giphy.com/gifs/explosion-oe33xf3B50fsc ')
    await ctx.send('(Thud)')

@client.command()
async def ak(ctx):
    """Answers Abdulrahman"""
    await ctx.send('I believe in aliens too Senpai:heart:')
    await ctx.send('https://giphy.com/gifs/foxhomeent-alien-aliens-james-cameron-l3V0ma60jQqGCoJyM ')

@client.command()
async def mahmoud(ctx):
    """Answers Mahmoud"""
    await ctx.send('Hey Mahmoud, I can be whomever you want....even emilia :heart:')
    await ctx.send('https://tenor.com/view/emilia-re-zero-anime-smile-gif-12793368 ')
    await ctx.send("We're the same voice actress")

@client.command()
async def saoud(ctx):
    """Answers Saoud"""
    await ctx.send('あなたは退化したクソ :hushed:')

@client.command()
async def ray(ctx):
    """Answers Ray"""
    await ctx.send('Here Ray, how about you find good internet before you talk to me. :stuck_out_tongue_closed_eyes:')
    await ctx.send('https://www.broadbandspeedchecker.co.uk/isp-directory/Portugal/Lisbon.html ')

@client.command()
async def fuckyou(ctx):
    """Don't Piss me off"""
    msg = 'Hey{0.author.mention}, here is the picture you told me to look up last night, I"m sorry it took so long :heart:.'.format(ctx.message)
    await ctx.send(msg)
    await ctx.send("https://giphy.com/gifs/pizza-loli-deeznuts-PVhpy9qyMvZu0 ")
    await ctx.send("I'm pulling your discord email from your profile, the 1GB folder of trentacle hentai is on its way :heart:")
    msg2= "Hey{0.author.mention} don't fuck with me".format(ctx.message)
    await ctx.send(msg2)

@client.command()
async def kareem(ctx):
    """Answers Kareem"""
    msg = 'Krispy Kareem '.format(ctx.message)
    await ctx.send("Krispy Kareem, why are you talkig to me when you should be ...")
    await ctx.send("...")
    await ctx.send("......")
    await ctx.send("..........")
    await ctx.send("...")
    await ctx.send("......")
    await ctx.send("..........")
    await ctx.send(" PLAYING DOOOOOOTTTTTAAAA")

@client.command()
async def amir(ctx):
    """Answers Amir"""
    await ctx.send("Let's face it Amir this is what you imagine when I say moneyshot")
    await ctx.send("https://giphy.com/gifs/money-mattress-mgByAN6FfHTnq ")
    
    
@client.command()
async def roll(ctx, arg=0, arg2=0):
    """Rolls 1 dice type the modifier after command"""
    a=random.randrange(1,20,1)+arg
    await ctx.send('You rolled the dice and got: ' +str(a) +' The Enemy/Challenge has a rating of: ' +str(arg2))
    if (a<arg2):
        await ctx.send('You fail the roll.')
    else:
        await ctx.send('You pass and do ' +str(a-arg2) + ' damage')

@client.command()
async def clear(ctx, amount=10):
    """Clears 10 messages from chat (Optional, specify more/less"""
    await ctx.channel.purge(limit=amount)
       
client.run('NzAzODkxNzcxOTA5NzM0NDEw.XqVa3Q.pwSlgJLrufamzlyZkJagY9JGaBs')
    
