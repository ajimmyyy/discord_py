from ast import Str
from sqlite3 import Timestamp
from ssl import OPENSSL_VERSION_NUMBER
import discord
import datetime
from discord.ext import commands
from core.classes import Cog_Extension


class Main(Cog_Extension):

    @commands.command()
    async def em(self, ctx):
        now = datetime.datetime.now()
        embed=discord.Embed(title="about", url="https://www.youtube.com/channel/UCj6McJ0LUnHc8ROGZh3E9EA", description="about the bot", color=0x00c4f5,
        timestamp = now-datetime.timedelta(hours=8))
        embed.set_author(name="ajimmy", url="https://www.youtube.com/channel/UCj6McJ0LUnHc8ROGZh3E9EA")
        embed.set_thumbnail(url="https://c.tenor.com/X8fqZmQF-ocAAAAC/hakui-koyori-koyori.gif")
        
        embed.add_field(name="main", value="/=ping :\nshow your internet ping\n/=sayd (message):\nshow what you say\n/=clean (num) :\n clean message\n", inline=False)
        embed.add_field(name="react", value="/=koyo :\nshow some cute pictures", inline=False)
        embed.add_field(name="event", value="koyori :\nsay hello to you", inline=False)
        embed.add_field(name="task", value="/=set_channel (channel ID) :\nset where massages will send\n/=set_time (hour/minute) :\nalarm clock's time\n", inline=False)
        embed.add_field(name="team", value="/=rand_squad :\nranden grouping\n/=rand_squad_wait_time :\nset mini time need to wait between two rand_squad\n", inline=False)
        embed.add_field(name="emoticon", value="/=pic :\n/= pic upload(picture name you want):\nupload picture\n/= pic use(picture name you want):\nsend picture\n/= pic list:\nlist all the picture", inline=False)
        embed.add_field(name="for programer", value="/=load (name of the project)\n/=unload (name of the project)\n/=reload (name of the project)", inline=False)
        await ctx.send(embed=embed)

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'{round(self.bot.latency * 1000)} (ms)')

    @commands.command()
    async def sayd(self, ctx, *,msg):
        await ctx.message.delete()
        await ctx.send(msg)
    
    @commands.command()
    async def clean(self, ctx, num : int):
        await ctx.channel.purge(limit = num + 1)



def setup(bot):
    bot.add_cog(Main(bot))