import asyncio
from datetime import datetime
import discord
from discord.utils import async_all
from days import tuesdays2021, tuesdays2022, wednesdays2021, wednesdays2022
from header import channelid
import tracemalloc

tracemalloc.start() 

def automate():
     today = datetime.now()
     day = today.strftime("%Y-%m-%d")
     dayoweek = datetime.today().strftime('%A')
     
     client = discord.Client()
     client.wait_until_ready()
     channels = client.get_channel(id=767871452665741392)

     global announcement

     if day in tuesdays2022 or day in tuesdays2021 or day in wednesdays2021 or day in wednesdays2022:
          announcement = "@everyone: Today's date is {day} which is a {dayoweek} - that means we have practice today!"
     elif ((dayoweek == 'Tuesday' or dayoweek == 'Wednesday') and (day not in tuesdays2021 or day not in tuesdays2022 or day not in wednesdays2021 or day not in wednesdays2022)):
          announcement = '@everyone: No practice today :)'
     else:
          announcement = "deez nutz"

     # print (dayoweek)
     
     print (announcement)
automate()