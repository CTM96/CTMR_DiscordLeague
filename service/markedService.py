from service.playerGeneratorService import generatePlayer
from constant.playerConstants import POSITIONS
from replit import db
from etc.classes import Player

async def generateMarked() -> list:
  marked = []
  counter = 1
  for x in POSITIONS:
    marked.append(await generatePlayer(2, counter, x))
    counter = counter + 1
    marked.append(await generatePlayer(2, counter, x))
    counter = counter + 1
  return marked

async def getStringFromPlayer(player: Player) -> str:
  number = str(player.number)
  position = str(player.position)
  name = str(player.name)
  age = str(player.age)
  rating = str(player.rating)
  potential = str(player.potential)
  value = str(player.value)
  return number + "|" + position + "|" + name + "|" + age + "|" + rating + "|" + potential + "|" + value

async def getPlayerFromString(string: str) -> Player:
  split = string.split("|")
  return Player(split[0], split[1], split[2], split[3], split[4], split[5], split[6])

async def saveMarked(marked: list, message):
  serverId = str(message.guild.id)
  markedKey = serverId + "_" + "MARKED"
  stringMarked = []
  for x in marked:
    stringMarked.append(await getStringFromPlayer(x))
  db[markedKey] = stringMarked

async def getMarked(message) -> list:
  serverId = str(message.guild.id)
  markedKey = serverId + "_" + "MARKED"
  if markedKey not in db.keys():
    await message.channel.send("ERROR - SOMETING WENT WRONG. THERE IS NO MARKED FOR THIS SERVER")
    return
  playerMarked = []
  for x in db[markedKey]:
    playerMarked.append(await getPlayerFromString(x))
  return playerMarked