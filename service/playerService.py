from replit import db
import random
from etc.classes import Player
from constant.playerConstants import POSITIONS
from service.playerGeneratorService import generatePlayer

#['Liverpool FC|5000|0', '1|GK|Z.Joyce|18|50|60|1000', '2|CB|K.Horne|19|50|60|1000', '3|CB|Z.Fisher|29|50|60|1000', '4|LB|N.Fox|20|50|60|1000', '5|RB|S.Chase|18|50|60|1000', '6|CM|N.Barbour|29|50|60|1000', '7|CM|K.Walters|32|50|60|1000', '8|LM|V.Lyons|30|50|60|1000', '9|RM|V.Zhao|16|50|60|1000', '10|ST|C.Herman|20|50|60|1000', '11|ST|L.Silverman|26|50|60|1000', '12|ST|A.Morton|24|50|60|1000', '13|LB|Z.Norton|30|50|60|1000', '14|CB|P.McPherson|21|50|60|1000', '15|CM|B.Peters|30|50|60|1000', '16|ST|T.Cox|25|50|60|1000']

async def getStringFromPlayer(player: Player) -> str:
  number = str(player.number)
  position = str(player.position)
  name = str(player.name)
  age = str(player.age)
  rating = str(player.rating)
  potential = str(player.potential)
  value = str(player.value)
  return number + "|" + position + "|" + name + "|" + age + "|" + rating + "|" + potential + "|" + value

async def init(message):
  if len(message.content.split(" ")) < 2:
    return
  userId = str(message.author.id)
  serverId = str(message.guild.id)
  userKey = userId + "_" + serverId
  if userKey in db.keys():
    await message.channel.send("You already have a club.")
    return
  teamName = " ".join(message.content.split(" ")[1:])
  money = str(5000)
  trophies = str(0)
  teamInfo = teamName + "|" + money + "|" + trophies
  startingXI = []
  subs = []
  counter = 1
  for x in POSITIONS:
    startingXI.append(await getStringFromPlayer(await generatePlayer(1, counter, x)))
    counter = counter + 1
  for y in range(5):
    subs.append(await getStringFromPlayer(await generatePlayer(1, counter, random.choice(POSITIONS))))
    counter = counter + 1
  finalList = []
  finalList.append(teamInfo)
  finalList.extend(startingXI)
  finalList.extend(subs)
  db[userKey] = finalList
  await message.channel.send("We are proud to introduce the new manager of " + teamName + ". " + "<@"+userId+">" )

async def quitJob(message):
  userId = str(message.author.id)
  serverId = str(message.guild.id)
  userKey = userId + "_" + serverId
  if userKey not in db.keys():
    await message.channel.send("There is no job to quit.")
    return
  del db[userKey]
  await message.channel.send("We wish " + "<@" + userId + "> only the best for the future.")
  return