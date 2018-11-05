import discord
from discord.ext import commands
import asyncio

bot = commands.Bot(command_prefix='U'
)
@bot.event
async def on_ready():
  print ('Logged in as')
  print (bot.user.name)
  print (bot.user.id)
  print ('------') 
  
@bot.command()
async def ping():
    await bot.say(':ping_pong:')
    await bot.say('Hey! You pinged me!!')
    
@bot.command()
async def adrule():
    await bot.say(' Advertisement Rules:Follow the advertisement rules when advertising, anything against the advertising rules will be deleted. Follow the rules or you will be warned, or may have your advertisement role provoked. Rules: 1. Advertisements must have a description or it will be deleted. 2. Do not leave after posting an advertisement or it will be deleted. 3. NO DM ADVERTISING. 4. Put your advert in the right category that fits your server. 5. You may only advertise 4 adverts in a 24 hour day period. More rules will be added to future situations. More Information:                    DM Advertising is strictly prohibited in Unique Discord Servers. If you see someone DM Advertising and the person is in our server please contact moderation immediately. Again, just because some applicable rules are not up there, that does not mean you can take advantage of that. Our moderators will reflect an action against you for a pretty good reason.')
    await bot.say('If you need more support tag one of are staff.')
    
@bot.command()
async def info():
	await bot.say('This bot was made by UDS. If anyone claims to have make this bot it is a lie. The bot is still under development and more commands will be added soon!')
