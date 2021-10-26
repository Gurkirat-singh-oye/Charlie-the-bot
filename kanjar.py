import discord
from discord.ext import commands, tasks
import os
import re


import urllib.request
import pafy

from dotenv import load_dotenv

C_token = 'NjkyOTU1OTg2MjgwODQxMzIx.Xn2DjQ.p6Hp5wClXNVOg6kBGd-a9mz0-KM'

  
client = commands.Bot(command_prefix='`', intents = discord.Intents.all())


@client.command(name="join")

async def join(ctx):
    print(ctx.author.voice.channel)
    await ctx.author.voice.channel.connect()

@client.command(name="play")
async def play(ctx,tis):
    voice_channel = ctx.author.voice.channel
    await ctx.author.voice.channel.connect()
    print (tis)
    html = urllib.request.urlopen(
        f"https://www.youtube.com/results?search_query={tis}")
    video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())

    url = f'https://www.youtube.com/watch?v={video_ids[0]}'

    video = pafy.new(url)
    best = video.audiostreams[0]
##    print(type(best))
    player = (discord.FFmpegPCMAudio(best.url))
    ctx.voice_client.play(player)
##    global p
##    p=vlc.MediaPlayer(best.url)
##    p.play()
    
client.run(C_token)
