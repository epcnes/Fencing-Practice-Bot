from asyncio.tasks import Task
from datetime import datetime
import discord
from discord import channel
from days import tuesdays2021, tuesdays2022, wednesdays2021, wednesdays2022
from discord.ext.commands import Bot
from discord.ext import tasks

def automate():
     today = datetime.now()

     day = today.strftime("%Y-%m-%d")
     dayoweek = today.strftime('%d')

     bot = Bot("$!")
     channel = bot.get_channel(767871452665741392)

     global message

     if day in tuesdays2022 or day in tuesdays2021:
          message = "@everyone: Today's date is {day} which is a Tuesday - that means we have practice today!"
     elif day in wednesdays2021 or day in wednesdays2022:
          message = "@everyone: Today's date is {day} which is a Wednesday - that means we have practice today!"
     elif ((dayoweek == 'Tuesday' or dayoweek == 'Wednesday') and (day not in tuesdays2021 or day not in tuesdays2022 or day not in wednesdays2021 or day not in wednesdays2022)):
          message = '@everyone: No practice today :)'
     else:
          message = "deez nutz"

     # print (message)

# def signal():
#      @tasks.datetime
#      async def fullsend():
#           await channel.TextChannel.send(message)