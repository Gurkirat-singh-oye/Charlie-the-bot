from email import message
import discord
from discord.ext import commands, tasks
import os
import re
import devhere
from random import randint
import json
import urllib.request
import pafy


C_token = 'NjkyOTU1OTg2MjgwODQxMzIx.GErMTU.7K7x7Ah03GscqSD2qN0BGW7FTLpyluK2Dm9x1U'
global cnt
cnt =0
  
client = commands.Bot(command_prefix='`', intents = discord.Intents.all())

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.competing, name="incel race"))
    print("suru!!")

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
    print (url)
    video = pafy.new(url)
    best = video.audiostreams[0]
    player = (discord.FFmpegPCMAudio(best.url))
    ctx.voice_client.play(player)

@client.command()
async def news(ctx):
    newsart = await devhere.news()
    await ctx.channel.send(newsart)

@client.event
async def on_message(message):
    print("ye chla")
    if client.user.mentioned_in(message):
            await message.channel.send("Dubara mention mat kario, gaand mardunga!!")
            await message.channel.send(message.author)
    word_list = ['rl?', 'valo?', 'chutiya', 'ass', 'titties', 'nipple', 'Ass', 'ASS', 'bhenchod', 'gaand']
    messageContent = message.content
    if len(messageContent) > 0:
        for word in word_list:
            if word in messageContent:
                r = urllib.request.urlopen(
    "https://g.tenor.com/v1/search?q=%s&key=%s&limit=%s" % (word, "HYDM53SGJD2K", 10))
                #print (r)
                r=r.read().decode()
                #print(r)
                ##temp = json.loads(r.read().decode())
##                print (len(temp))
##                print (len(temp['results'][0]))
##                print (len(temp['results'][0]['media'][0]))
##                print (temp['results'][0]['media'][0]['mediumgif']['url'])
                gif_s = re.findall(r"https://(\S{61}).gif", r)
                print(len(gif_s))
                await message.channel.send("https://" + gif_s[randint(1,10)*7 - 7] + ".gif")
    await client.process_commands(message)
    
client.run(C_token)
