from ntpath import join
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='/=')

@bot.event
async def on_ready():
    print(">> Bot is online <<")

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(907248185943146506)
    await channel.send(f'{member} jion!')
    

@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(907248185943146506)
    await channel.send(f'{member} leave!')

@bot.command()
async def ping(ctx):
    await ctx.send(f'{round(bot.latency * 1000)} (ms)')

bot.run("OTU4MzcyNTMwMzUwMDg0MTA2.YkMX-A.BUcZtY11TQdXUeZa7eMlyg9rV7s")
