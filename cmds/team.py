from multiprocessing.connection import wait
from time import time
import time
from xmlrpc.client import DateTime
import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json, asyncio, datetime
import random

with open('setting.json', mode = 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)


class Team(Cog_Extension):
    wait_time = 5
    start_time = int(datetime.datetime.now().strftime("%M")) - wait_time - 1
    counter = 2

    @commands.command()
    async def rand_squad_wait_time(self, ctx, msg):
        wait_time = int(msg)
        await ctx.send(f'Waiting time set as {wait_time} min')

    @commands.command()
    async def rand_squad(self, ctx):
        now_time = datetime.datetime.now().strftime("%M")
        if int(now_time) - int(self.start_time) > self.wait_time:
            self.counter = 1
        else:
            self.counter = 0
        if(self.counter == 1):
            online = []
            for member in ctx.guild.members:
                if not member.bot:
                    online.append(member)

            team = min(20, int(len(online) / 5)* 5)
            random_online = random.sample(online, k = team )

            for squad in range(int(team / 5)):
                a = random.sample(random_online, k = 5)
                cause = random.choice(jdata['cause'])
                role_team = random.choice(jdata['role'])
                role = role_team[0]
                role_2 = role_team[1]
                await ctx.send(f'{a[0].name} {cause}轉生成為{role}\n而{a[1].name},{a[2].name},{a[3].name},{a[4].name}\n組成{role_2}小隊踏上討罰{role}之路。')
                for name in a:
                    random_online.remove(name)
                self.start_time = datetime.datetime.now().strftime("%M")
            self.team_counter = 0
        else:
            await ctx.send('劇情尚未結束')
    
    @commands.group()
    async def atk(self, ctx):
        pass
    @atk.command()
    async def sword(self, ctx):
        await ctx.send("你的劍擦過對方的盔甲，你的劍產生些微裂痕")
    @atk.command()
    async def bow(self, ctx):
        await ctx.send("你的箭筆直的飛向友軍，對方見你的低能行為，對你的戒心下降(抗性降低10%)")
    @atk.command()
    async def mag(self, ctx):
        await ctx.send("小火球打在對方的盔甲上，但對方似乎有魔法抗姓")
    @atk.command()
    async def chicken(self, ctx):
        await ctx.send("Chicken attack!\nWatch your back before it fades to black\nThey might look harmless but they’ll kick your non-chicken ass\nGo chicken go!\nGo chicken go!\nNow go, now fly\nYou own the sky")
        time.sleep(2)
        await ctx.send("什麼事都沒發生")

    
def setup(bot):
    bot.add_cog(Team(bot))