from os import symlink
import discord
from discord.ext import commands
from core.classes import Cog_Extension
import random
import uuid
import requests
from PIL import Image #install
import os 
import pathlib
import cv2 #install
import time
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
                if  ctx.message.attachments[0].size > 250000:
                    await ctx.send("Please upload picture under 250kb")
                else:
                    await ctx.message.attachments[0].save(f'{position}\\picture\\{pic_name}.jpg')
                    
                    img = cv2.imread(f'{position}\\picture\\{pic_name}.jpg')
                    image = cv2.resize(img, dsize=(48,48), interpolation=cv2.INTER_CUBIC)
                    cv2.imwrite(f'{position}\\picture\\{pic_name}.jpg', image)
                    
                    await ctx.send("Upload success")
    
    @pic.command()
    async def use(self, ctx,pic_name):
        position = pathlib.Path().parent.absolute()
        dirs = os.listdir(f'{position}\\picture')
        for name in dirs:
            if pic_name == name[:-4]:
                pic = discord.File(f'{position}\\picture\\{name}')
                await ctx.channel.purge(limit = 1)
                await ctx.send(file = pic)
            else:
                await ctx.send(f'Can not find the picture name {pic_name}')
                time.sleep(3)
                await ctx.channel.purge(limit = 2)

def setup(bot):
    bot.add_cog(Emoticon(bot))
