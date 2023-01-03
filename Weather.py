TOKEN ='MTA1Nzc1OTUzNDkzMzg4NDk5OQ.GySREm.SPcbNy5y-czIpwJsJxx9eBbJO4uD6-eXLAJx48' 
APIKEY = '76e9913b2a612463565478de07cbca97'

# weather-bot

import discord
from discord.ext import commands
import requests

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
async def weather(ctx, *, city: str):
    # send a message to the channel where the command was invoked
    await ctx.channel.send(f"Getting weather for {city}...")
    print('next')
    api_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={APIKEY}"
    
    response = requests.get(api_url.format(city=city, api_key=APIKEY))
    print(response)
    if response.status_code == 200:
        data = response.json()
        print('line1')
        temperature = data.get('main', {}).get('temp', 0)
        print('line2')
        rain = data['weather'][0]['description']
        print('line3')
        await ctx.channel.send(f"The temperature in {city} is {(temperature-273.15) * (9/5) + 32: .2f}°F with a chance of {rain}.")
    else:
        print('error')
    


bot.run(TOKEN)