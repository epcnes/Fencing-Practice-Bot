import asyncio
from datetime import datetime
import discord
from discord.ext.commands import Bot
from discord.utils import async_all
from days import tuesdays2021, tuesdays2022, wednesdays2021, wednesdays2022
from header import channelid
import tracemalloc

tracemalloc.start() 

def automate():
     today = datetime.now()
     day = today.strftime("%Y-%m-%d")
     dayoweek = datetime.today().strftime('%A')

     global announcement #global variable

     #what to say on what days
     if day in tuesdays2022 or day in tuesdays2021 or day in wednesdays2021 or day in wednesdays2022:
          announcement = "@everyone: Today's date is {day} which is a {dayoweek} - that means we have practice today!"
     elif ((dayoweek == 'Tuesday' or dayoweek == 'Wednesday') and (day not in tuesdays2021 or day not in tuesdays2022 or day not in wednesdays2021 or day not in wednesdays2022)):
          announcement = '@everyone: No practice today :)'
     else:
          announcement = "deez nutz"

     #makes things run well and lets me get no error messages
     client = discord.Client()
     def lop():
          loop = client.wait_until_ready()
          fullsend(announcement)
          loop.close
     global channel
     channel = Bot.fetch_channel(self = client, channel_id = 767871452665741392)

     #fullsend function thing     
     print (announcement)

async def fullsend():
     async def ugh():
          automate()
     ugh()
     await channel.send(announcement)