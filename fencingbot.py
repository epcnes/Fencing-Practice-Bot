from datetime import datetime
import discord
from header import token
from announcing import fullsend
from daysitsbeen import days_it_be
from cogs import OnReady_Message

#main program#

client = discord.Client()
days_its_been = days_it_be

#log in#
@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))

now = datetime.now()
time = now.strftime("%H:%M:%S")
dayoweek = now.strftime("%d")

#test functions by message event#
@client.event
async def on_message(message):
     if message.author == client.user:
          return
     if message.content.startswith('$!produce'):
          await produce()

#hopefully automate soon#

@on_ready()
async def produce():
     today = now.strftime("%m-%d-%Y")
     if today in days_its_been:
          print ("task already done today")
     else:
          await fullsend()
          # days_its_been.append(today)
          table = open("daysitsbeen.py", "w")
          table.write(f"days_it_be = {days_its_been}")
          table.close()

OnReady_Message(client)

import tracemalloc
tracemalloc.start()            

print ("I'm working on it...")
client.run(token)