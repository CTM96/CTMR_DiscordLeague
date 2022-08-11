import os
from replit import db
import discord
from service.serverService import loadServer
from service.playerService import init
from service.playerService import quitJob
from service.menuService import menuMainPage
from service.menuService import menuScoutInfo
from service.menuService import backToMainMenu
from service.menuService import closeMenu

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
    if message.content.startswith("$init "):
      if author.id not in CURRENT_MODS:
        CURRENT_MODS.append(author.id)
        await init(message)
        CURRENT_MODS.remove(author.id)
    elif message.content == "$quitjob":
      if author.id not in CURRENT_MODS:
        CURRENT_MODS.append(author.id)
        await quitJob(message)
        CURRENT_MODS.remove(author.id)
    elif message.content == "$menu":
      if author.id not in CURRENT_MODS:
        CURRENT_MODS.append(author.id)
        await menuMainPage(message)
        CURRENT_MODS.remove(author.id)
    elif message.content == "$get":
      if author.id not in CURRENT_MODS:
        CURRENT_MODS.append(author.id)
        #DO
        CURRENT_MODS.remove(author.id)
  
  
  if str(author.id) == "377551216869244929":
    if message.content == "$debugdbclear":
      db.clear()

footers = ["Main Menu", "Scouting Area"]

@CLIENT.event
async def on_reaction_add(reaction, user):
  if len(reaction.message.embeds) > 0:
    if reaction.message.embeds[0].footer.text in footers:
      author = reaction.message.embeds[0].author
      if author.name == user.name:
        if author.id not in CURRENT_MODS:
          CURRENT_MODS.append(author.id)
          await handleReactions(reaction, user)
          CURRENT_MODS.remove(author.id)

async def handleReactions(reaction, user):
  if reaction.emoji == "👶":
    await menuScoutInfo(reaction.message, reaction.message.embeds[0], user)
  elif reaction.emoji == "🔙":
    await backToMainMenu(reaction.message, reaction.message.embeds[0], user)
  elif reaction.emoji == "❌":
    await closeMenu(reaction.message, reaction.message.embeds[0], user)

loadServer()
CLIENT.run(os.environ["DISCORD_TOKEN"])