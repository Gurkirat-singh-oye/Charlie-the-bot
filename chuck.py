import discord
from discord.ext import commands, tasks
#import os
import re
import requests
import json
import urllib.request
import pafy

from dotenv import load_dotenv

C_token = 'NjkyOTU1OTg2MjgwODQxMzIx.Xn2DjQ.l9FDkwKkPTQfPqCgod9zzA0E18U'
global cnt
cnt =0
  
client = commands.Bot(command_prefix='`', intents = discord.Intents.all())

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Blade Runner 2049!!"))
    print("suru!!")

@client.command(name="join")
async def join(ctx):
    print(ctx.author.voice.channel)
    await ctx.author.voice.channel.connect()

@client.event
async def on_message(message):
    if client.user.mentioned_in(message):
            await message.channel.send("please dont mention again!!")
            await message.channel.send(message.author)

@client.event
async def on_message(message):
    word_list = ['rl?', 'valo?', 'gta']
    messageContent = message.content
    if len(messageContent) > 0:
        for word in word_list:
            if word in messageContent:
                r = urllib.request.urlopen(
    "https://g.tenor.com/v1/search?q=%s&key=%s&limit=%s" % (word, "HYDM53SGJD2K", 1))
                temp = json.loads(r.read().decode())
                print (temp['results'][0]['media'][0]['mediumgif']['url'])
                message.channel.send(f'Did someone say {word}')
                await message.channel.send(temp['results'][0]['media'][0]['mediumgif']['url'])

#@client.command(name="play")
#async def play(ctx,tis):
#    voice_channel = ctx.author.voice.channel
#    await ctx.author.voice.channel.connect()
 #   print (tis)
  #  html = urllib.request.urlopen(
   #     f"https://www.youtube.com/results?search_query={tis}")
    #video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())

#    url = f'https://www.youtube.com/watch?v={video_ids[0]}'

#    video = pafy.new(url)
 #   best = video.audiostreams[0]
  #  player = (discord.FFmpegPCMAudio(best.url))
#    ctx.voice_client.play(player)
    
client.run(C_token)
