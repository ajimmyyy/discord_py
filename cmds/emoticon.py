from os import symlink
import discord
from discord.ext import commands
from core.classes import Cog_Extension
import random
import uuid
import requests
import os
import pathlib
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
            re_name = False 
            position = pathlib.Path().parent.absolute()
            dirs = os.listdir(f"{position}\\picture")
            for name in dirs:
                if pic_name == name[:-4]:
                    re_name = True
            if re_name:
                await ctx.send("Already has the same name picture")
            else:
                await ctx.message.attachments[0].save(f'{p}\\picture\\{pic_name}.jpg')
                await ctx.send("Upload success")
            
def setup(bot):
    bot.add_cog(Emoticon(bot))
