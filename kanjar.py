import discord
from discord.ext import commands, tasks
import os
import time
import re
import devhere
from random import randint
import json
import urllib.request
import pafy


C_token = 'NjkyOTU1OTg2MjgwODQxMzIx.GErMTU.7K7x7Ah03GscqSD2qN0BGW7FTLpyluK2Dm9x1U'
global cnt
cnt =0
playerlist = []
  
client = commands.Bot(command_prefix='`', intents = discord.Intents.all())

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.competing, name="The incel race"))
    print("suru!!")

@client.command(name="join")
async def join(ctx):
    print(ctx.author.voice.channel)
    await ctx.author.voice.channel.connect()

@client.command(name="play")
async def play(ctx,tis=None):
    voice_channel = ctx.author.voice.channel
    voice_client = discord.utils.get(ctx.bot.voice_clients, guild=ctx.guild)
    if voice_client and voice_client.is_connected():
        pass
    else:
        await ctx.author.voice.channel.connect()
    print (tis)
    
    if tis!=None:
        url = await devhere.findmeurl(tis)
        video = pafy.new(url)
        wait = (int((video.duration).split(':')[0])*60*60+int((video.duration).split(':')[1])*60+int((video.duration).split(':')[2]))
        playerlist.append(video)
    print (playerlist)
    try:
        best = playerlist[0].audiostreams[0]
        player = (discord.FFmpegPCMAudio(best.url))
        ctx.voice_client.play(player)
        await ctx.channel.send(embed = discord.Embed(title=playerlist[0].title,url=f"https://www.youtube.com/watch?v={playerlist[0].videoid}").set_image(url=playerlist[0].bigthumb))
        playerlist.pop(0)
    except discord.errors.ClientException:
        print("still playing")
        pass
    

@client.command()
async def skip(ctx):
    await stop(ctx)
    await play(ctx)

@client.command()
async def stop(ctx):
    ctx.voice_client.stop()

@client.command()
async def news(ctx):
    newsart = await devhere.news()
    await ctx.channel.send(newsart)

@client.command()
async def save(ctx,arg1,arg2 = 'default'):
    say = await devhere.savethissong(arg1,arg2)
    await ctx.channel.send(say)

@client.command()
async def listradio(ctx):
    for a in devhere.songdic["savedsongs"]["default"]:
        await ctx.channel.send(a)

@client.command()
async def playserveradio(ctx):
    for a in devhere.songdic["savedsongs"]["default"]:
        await play(ctx, a)

@client.event
async def on_message(message):
    print("ye chla")
    if client.user.mentioned_in(message):
            await message.channel.send("Dubara mention mat kario, gaand mardunga!!")
    word_list = ['rl?', 'valo?', 'chutiya', 'ass', 'titties', 'nipple', 'Ass', 'ASS', 'bhenchod', 'gaand']
    messageContent = message.content
    if len(messageContent) > 0:
        for word in word_list:
            if word in messageContent:
                r = urllib.request.urlopen(
    "https://g.tenor.com/v1/search?q=%s&key=%s&limit=%s" % (word, "HYDM53SGJD2K", 20))
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
                await message.channel.send("https://" + gif_s[randint(1,20)*7 - 7] + ".gif")
    await client.process_commands(message)
    
client.run(C_token)
