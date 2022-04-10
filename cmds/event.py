import discord
from discord.ext import commands
from core.classes import Cog_Extension
import random
import json

with open('setting.json', mode = 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)

class Event(Cog_Extension):
    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = self.bot.get_channel(int(jdata['channel']))
        await channel.send(f'{member} jion!')
        
    @commands.Cog.listener()
    async def on_member_remove(self, member):
        channel = self.bot.get_channel(int(jdata['channel']))
        await channel.send(f'{member} leave!')
    
    @commands.Cog.listener()
    async def on_message(self, msg):
        if msg.content == '大眼睛':
            random_msg = random.choice(jdata['big_eyes'])
            await msg.channel.send(random_msg)
        if msg.content == 'koyori':
            await msg.channel.send('hi')
            
def setup(bot):
    bot.add_cog(Event(bot))