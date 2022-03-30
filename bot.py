from msilib.schema import File
from ntpath import join
import random
import discord
from discord.ext import commands
import json

with open('setting.json', mode = 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)

bot = commands.Bot(command_prefix='/=')

@bot.event
async def on_ready():
    print(">> Bot is online <<")

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(int(jdata['channel']))
    await channel.send(f'{member} jion!')
    
@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(int(jdata['channel']))
    await channel.send(f'{member} leave!')

@bot.command()
async def ping(ctx):
    await ctx.send(f'{round(bot.latency * 1000)} (ms)')

@bot.command()
async def koyo(ctx):
    random_pic = random.choice(jdata['pic'])
    koyori = discord.File(random_pic)
    await ctx.send(file = koyori)

bot.run(jdata['TOKEN'])
