from os import symlink
import discord
from discord.ext import commands
from core.classes import Cog_Extension
import random
import uuid
import requests
import shutil
import json

with open('setting.json', mode = 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)

class Emoticon(Cog_Extension):
    @commands.group()
    async def pic(self, ctx):
        pass 
    @pic.command()
    async def upload(self, ctx,pic_name):
        try:
            url = ctx.message.attachments[0].url
        except IndexError:
            await ctx.send("No attachments")
        else:
            with open('setting.json', mode = 'r', encoding='utf8') as jfile:
                jdata = json.load(jfile)
            time = int(jdata['pic_name_file'][0])
            re_name = False 
            for i in range(time):
                if pic_name == jdata['pic_name_file'][i]:
                    re_name = True
            if re_name:
                await ctx.send("Already has the same name picture")
            else:
                jdata['pic_name_file'][0] = str(time + 1)
                jdata['pic_name_file'][time + 1] = pic_name
                with open('setting.json', mode = 'w', encoding='utf8') as jfile:
                    json.dump(jdata, jfile, indent=4)
                
                await ctx.message.attachments[0].save(f'C:\\Users\\acer\\Documents\\GitHub\\discord_py\\picture\\{pic_name}.jpg')
                await ctx.send("Upload success")
            
def setup(bot):
    bot.add_cog(Emoticon(bot))
