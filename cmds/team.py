import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json, asyncio, datetime

with open('setting.json', mode = 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)

class Team(Cog_Extension):
    @commands.command()
    async def rand_squad(self, ctx):

        online = []
        for member in ctx.guild.members:
             if str(member.status) == 'online':
                 online.append(member)
        print(ctx.guild.members)

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     async def interval():
    #         await self.bot.wait_until_ready()
    #         self.channel = self.bot.get_channel(907248185943146506)
    #         while not self.bot.is_closed():
    #             now_time = datetime.datetime.now().strftime("%d")
    #             if now_time == 1:
    #                 pass


def setup(bot):
    bot.add_cog(Team(bot))