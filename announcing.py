import asyncio
from datetime import datetime
import discord
from discord.ext.commands import Bot
from discord.utils import async_all
from days import tuesdays2021, tuesdays2022, wednesdays2021, wednesdays2022
from header import channelid
import tracemalloc

tracemalloc.start() 

async def fullsend():
     client = discord.Client()
     channel = Bot.fetch_channel(self = client, channel_id = 767871452665741392)
     today = datetime.now()
     day = today.strftime("%Y-%m-%d")
     dayoweek = datetime.today().strftime('%A')

     if day in tuesdays2022 or day in tuesdays2021 or day in wednesdays2021 or day in wednesdays2022:
          announcement = f"@everyone: Today's date is {day} which is a {dayoweek} - that means we have practice today!"
     elif ((dayoweek == 'Tuesday' or dayoweek == 'Wednesday') and (day not in tuesdays2021 or day not in tuesdays2022 or day not in wednesdays2021 or day not in wednesdays2022)):
          announcement = '@everyone: No practice today :)'
     else:
          announcement = "deez nutz"
     
     await channel.send(announcement)