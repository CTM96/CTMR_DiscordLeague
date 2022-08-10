import os
import discord
from service.serverService import loadServer

CLIENT = discord.Client()
CURRENT_MODS = []

@CLIENT.event
async def on_ready():
  print('DEBUG: RUNNING DiscordLeague')

@CLIENT.event
async def on_message(message):
  author = message.author
  if author.bot:
    return
  else:
    if message.content == "$----------------------------------":
      if author.id not in CURRENT_MODS:
        CURRENT_MODS.append(author.id)
        #DO
        CURRENT_MODS.remove(author.id)
    
    elif message.content == "$----------------------------------":
      if author.id not in CURRENT_MODS:
        CURRENT_MODS.append(author.id)
        #DO
        CURRENT_MODS.remove(author.id)

loadServer()
CLIENT.run(os.environ["DISCORD_TOKEN"])