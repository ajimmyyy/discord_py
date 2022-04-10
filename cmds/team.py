from xmlrpc.client import DateTime
import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json, asyncio, datetime
import random

with open('setting.json', mode = 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)

class Team(Cog_Extension):
    
    start_time:datetime
    counter = 1
    
    @commands.command()
    async def rand_squad(self, ctx):
        if(self.counter == 1):
            online = []
            for member in ctx.guild.members:
                if not member.bot:
                    online.append(member.name)

            team = min(20, int(len(online) / 5)* 5)
            random_online = random.sample(online, k = team )
            for squad in range(int(team / 5)):
                a = random.sample(random_online, k = 5)
                cause = random.choice(jdata['cause'])
                role = random.choice(jdata['role'])
                role_2 = '魔王'
                if role == '魔王':
                    role_2 = '勇者'
                await ctx.send(f'{a[0]} {cause}轉生成為{role}\n而{a[1]},{a[2]},{a[3]},{a[4]}\n組成{role_2}小隊踏上討罰{role}之路。')
                for name in a:
                    random_online.remove(name)
                self.start_time = datetime.datetime.now().strftime("%M")
            self.team_counter = 0
        else:
            await ctx.send('劇情尚未結束')
            

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        async def interval():
            await self.bot.wait_until_ready()
            while not self.bot.is_closed():
                now_time = datetime.datetime.now().strftime("%M")
                if now_time - self.start_time > 5:
                    self.team_counter = 1


def setup(bot):
    bot.add_cog(Team(bot))