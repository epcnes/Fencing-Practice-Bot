from discord.ext import tasks, commands
from announcing import automate

class OnReady_Message(commands.Cog):
   def __init__(self, client):
      self.client = client
      self.send_onready_message.start()

   def cog_unload(self):
      self.send_onready_message.close()
      return

   # task
   @tasks.loop(count = 1)  # do it only one time
   async def send_onready_message(self):
      channel = self.client.get_channel(int(767871452665741392))
      automate()

   @send_onready_message.before_loop  # wait for the client before starting the task
   async def before_send(self):
      await self.client.wait_until_ready()

      return

   @send_onready_message.after_loop  # destroy the task once it's done
   async def after_send(self):
      self.send_onready_message.close()

      return
   @send_onready_message.after_loop  # destroy the task once it's done
   async def after_send(self):
      self.send_onready_message.close()

      return