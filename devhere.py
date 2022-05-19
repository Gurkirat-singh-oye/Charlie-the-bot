from lib2to3.pgen2.pgen import ParserGenerator
import requests as rq
import random
from requests_html import HTMLSession
import lxml
import re

async def news():
    tmp = rq.get('https://www.thehindu.com/')
    links = (re.findall( "href=[\"\'](https://www.thehindu.com/news/.*?ece)[\"\']", tmp.text))
    return (random.choice(links))
