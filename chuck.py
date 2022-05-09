import discord
from discord.ext import commands, tasks
import re
import random
from requests_html import HTMLSession
import json
import lxml
import asyncio
import urllib.request
import pafy

#from dotenv import load_dotenv

C_token = 'NjkyOTU1OTg2MjgwODQxMzIx.Xn2DjQ.l9FDkwKkPTQfPqCgod9zzA0E18U'
cnt =0
switch = 0
  
client = commands.Bot(command_prefix="`", intents = discord.Intents.all())

#loop = asyncio.get_event_loop()

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="The return of the USSR"))
    print("suru!!")

@client.command(name="join")
async def join(ctx):
    print(ctx.author.voice.channel)
    await ctx.author.voice.channel.connect()


@client.command()
async def play(ctx,tis):
    voice_channel = ctx.author.voice.channel
    try:
        await ctx.author.voice.channel.connect()
    except discord.errors.ClientException:
        pass
    html = urllib.request.urlopen(
        f"https://www.youtube.com/results?search_query={tis}")
    video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())

    url = f'https://www.youtube.com/watch?v={video_ids[0]}'

    video = pafy.new(url)
    best = video.audiostreams[0]
    player = (discord.FFmpegPCMAudio(best.url))
    await ctx.voice_client.play(player)

@client.command()
async def stopukrupdate(ctx):
	global switch
	switch = 0

@client.command()
async def ukrwar(ctx,temp):

	global switch
	switch = 1

#	while(switch):

	try:
		page = HTMLSession().get("https://www.reddit.com/live/18hnzysb1elcs")
	except ValueError:
		pass
	page = lxml.html.fromstring(page.content)
	txt = (page.xpath('.//ol[@class="liveupdate-listing"]/li[1]//text()'))

	if txt[1] == temp:
		pass

	else:
		print(txt[1])
		temp = txt[1]
		for a in txt:
			if a.startswith("/u/"):
				break
			elif a == '\n' or a == '\n\n':
				pass
			else:
				await ctx.channel.send(a)
	return temp



@client.command()
async def startukrupdate(ctx):
	t='ggez'
	while True:
		t=await ukrwar(ctx,t)
		await asyncio.sleep(1800)

@client.event
async def on_message(message):
    if client.user.mentioned_in(message):
            await message.channel.send("Please, let me die in peace")
            await message.channel.send(message.author)

@client.event
async def on_message(message):
	await client.process_commands(message)
	word_list = ['rl', 'valo']
	messageContent = message.content
	if len(messageContent) > 0:
		for word in word_list:
			if word in messageContent:
				r = urllib.request.urlopen(
    "https://g.tenor.com/v1/search?q=%s&key=%s&limit=%s" % (word, "HYDM53SGJD2K", 8))
				temp = json.loads(r.read().decode())
				await message.channel.send(temp['results'][random.randint(0,8)]['media'][0]['mediumgif']['url'])

client.run(C_token)
