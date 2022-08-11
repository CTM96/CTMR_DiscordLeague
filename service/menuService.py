from replit import db
import discord

#MAIN MENU
  #TEAM
  #TRANSFERMARKED
  #SCOUTINFO
  #TABLEINFO
  #TRADEINFO
  #INFO
async def menuMainPage(message):
  userId = str(message.author.id)
  serverId = str(message.guild.id)
  userKey = userId + "_" + serverId
  if userKey not in db.keys():
    await message.channel.send("There is no club to manage. Use $init <TEAMNAME> to create a club.")
    return
  teamStats = db[userKey][0]
  split = teamStats.split("|")
  teamName = split[0]
  money = split[1]
  trophies = split[2]
  players = len(db[userKey]) - 1
  text = "\n\nClub: **" + str(teamName) + "**\n\n" + "Money: **" + str(money) + "€**" + "\n\n" + "Trophies: **" + str(trophies) + "**\n\n" + "Players: **" + str(players) + "**\n\n"
  embed = discord.Embed(description=text, color=0xd1d372)
  embed.set_author(name=message.author.name, icon_url=message.author.avatar_url)
  embed.set_footer(text="Main Menu")
  embed_box = await message.channel.send(embed=embed)
  await embed_box.add_reaction("⚽")
  await embed_box.add_reaction("👜")
  await embed_box.add_reaction("👶")
  await embed_box.add_reaction("📑")
  await embed_box.add_reaction("🤝")
  await embed_box.add_reaction("❓")
  await embed_box.add_reaction("❌")

async def backToMainMenu(message, embed, user):
  userId = str(user.id)
  serverId = str(message.guild.id)
  userKey = userId + "_" + serverId
  if userKey not in db.keys():
    await message.channel.send("There is no club to manage. Use $init <TEAMNAME> to create a club.")
    return
  teamStats = db[userKey][0]
  split = teamStats.split("|")
  teamName = split[0]
  money = split[1]
  trophies = split[2]
  players = len(db[userKey]) - 1
  text = "\n\nClub: **" + str(teamName) + "**\n\n" + "Money: **" + str(money) + "€**" + "\n\n" + "Trophies: **" + str(trophies) + "**\n\n" + "Players: **" + str(players) + "**\n\n"
  embed = discord.Embed(description=text, color=0xd1d372)
  embed.set_author(name=user.name, icon_url=user.avatar_url)
  embed.set_footer(text="Scouting Area")
  await message.edit(embed = embed)
  await message.clear_reactions()
  await message.add_reaction("⚽")
  await message.add_reaction("👜")
  await message.add_reaction("👶")
  await message.add_reaction("📑")
  await message.add_reaction("🤝")
  await message.add_reaction("❓")
  await message.add_reaction("❌")

async def menuScoutInfo(message, embed, user):
  text = "**Welcome to your local playground.**"
  embed = discord.Embed(description=text, color=0xd1d372)
  embed.set_author(name=user.name, icon_url=user.avatar_url)
  embed.set_footer(text="Scouting Area")
  await message.edit(embed = embed)
  await message.clear_reactions()
  await message.add_reaction("🔙")
  await message.add_reaction("❌")

async def closeMenu(message, embed, user):
  await message.delete()