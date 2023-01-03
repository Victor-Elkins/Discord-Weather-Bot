TOKEN ='MTA1Nzc1OTUzNDkzMzg4NDk5OQ.GySREm.SPcbNy5y-czIpwJsJxx9eBbJO4uD6-eXLAJx48' 


# timezone-bot

import discord
from discord.ext import commands

from datetime import datetime
from pytz import timezone
discord.Permissions = 8
description = '''A bot to be used for getting the time '''
intents = discord.Intents.all()
intents.members = True
bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def timeNow(time_zone: str): 
    fmt = "%Y-%m-%d %H:%M:%S %Z%z"

    # Current time in UTC
    now_utc = datetime.now(timezone('UTC'))
    await time_zone.channel.send (now_utc.strftime(fmt) + " (UTC)")

    # Convert to Europe/London time zone
    now_london = now_utc.astimezone(timezone('Europe/London'))
    await time_zone.channel.send (now_london.strftime(fmt) + " (London)")

    # Convert to Europe/Berlin time zone
    now_berlin = now_utc.astimezone(timezone('Europe/Berlin'))
    await time_zone.channel.send (now_berlin.strftime(fmt) + " (Berlin)")

    # Convert to CET time zone
    now_cet = now_utc.astimezone(timezone('CET'))
    await time_zone.channel.send(now_cet.strftime(fmt) + " (CET)")

    # Convert to Israel time zone
    now_israel = now_utc.astimezone(timezone('Israel'))
    await time_zone.channel.send(now_israel.strftime(fmt) + " (Israel)")

    # Convert to Canada/Eastern time zone
    now_canada_east = now_utc.astimezone(timezone('Canada/Eastern'))
    await time_zone.channel.send(now_canada_east.strftime(fmt) + " (Canada/Eastern)")

    # Convert to US/Central time zone
    now_central = now_utc.astimezone(timezone('US/Central'))
    await time_zone.channel.send(now_central.strftime(fmt) + " (US/Central)")

    # Convert to US/Pacific time zone
    now_pacific = now_utc.astimezone(timezone('US/Pacific'))
    await time_zone.channel.send(now_pacific.strftime(fmt) + " (US/Pacific)")


bot.run(TOKEN)