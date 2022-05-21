import requests as rq
import random
import urllib
import json
import re

jsonctx = open('savedsongs.json','r+')
songdic = json.load(jsonctx)

async def findmeurl(tis):
    html = urllib.request.urlopen(
        f"https://www.youtube.com/results?search_query={tis}")
    video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())

    url = f'https://www.youtube.com/watch?v={video_ids[0]}'
    return url

async def news():
    tmp = rq.get('https://www.thehindu.com/')
    links = (re.findall( "href=[\"\'](https://www.thehindu.com/news/.*?ece)[\"\']", tmp.text))
    return (random.choice(links))

async def savethissong(song, here):
    try:
        songdic['savedsongs'][here].index(song)
        return "This is already there"
    except ValueError:
        pass
    songdic['savedsongs'][here].append(song)
    jsonctx.seek(0)
    (json.dump(songdic,jsonctx))
    jsonctx.truncate()
    return f"this is your list (links and names){songdic['savedsongs'][here]}"
