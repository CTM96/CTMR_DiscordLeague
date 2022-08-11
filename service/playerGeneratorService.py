import random
from constant.playerConstants import PRENAMES
from constant.playerConstants import LASTNAMES
from constant.playerConstants import AGES
from constant.playerConstants import POSITIONS
from etc.classes import Player

MAX_AGE = 35

# GENERATOR MODE 1 = INIT
# GENERATOR MODE 2 = TRANSFERMARKED
# GENERATOR MODE 3 = SCOUTING

async def generatePlayer(mode: int, nextNumber: int, position: str) -> Player:
  if mode == 1:
    number = str(nextNumber)
    position = str(position)
    name = str(random.choice(PRENAMES)) + str(random.choice(LASTNAMES))
    age = str(random.choice(AGES))
    rating = str(50)
    potential = str(60)
    value = str(await calculateValue(rating))
    return Player(number, position, name, age, rating, potential, value)
  elif mode == 2:
    number = str(nextNumber)
    position = str(position)
    name = str(random.choice(PRENAMES)) + str(random.choice(LASTNAMES))
    age = str(random.choice(AGES))
    rating = str(await calculateRating(int(age)))
    potential = str(await calculatePotential(int(age), int(rating)))
    value = str(await calculateValue(rating))
    return Player(number, position, name, age, rating, potential, value)
  elif mode == 3:
    number = str(nextNumber)
    position = str(random.choice(POSITIONS))
    name = str(random.choice(PRENAMES)) + str(random.choice(LASTNAMES))
    age = str(16)
    rating = str(await calculateRating(int(age)))
    potential = str(await calculatePotential(int(age), int(rating)))
    value = str(await calculateValue(rating))
    return Player(number, position, name, age, rating, potential, value)

async def calculateValue(rating: str) -> int:
  rating = int(rating)
  if rating <= 45:
    return 1000
  elif rating <= 50:
    return 1000
  elif rating <= 55:
    return random.randint(1000,2000)
  elif rating <= 60:
    return random.randint(2000,2500)
  elif rating <= 65:
    return random.randint(2500,3000)
  elif rating <= 70:
    return random.randint(3000,5000)
  elif rating <= 75:
    return random.randint(5000,7000)
  elif rating <= 80:
    return random.randint(7000,8000)
  elif rating <= 85:
    return random.randint(8000,8500)
  elif rating <= 90:
    return random.randint(8500,9000)
  elif rating <= 95:
    return random.randint(9000,9500)
  elif rating <= 100:
    return random.randint(9500,10000)

async def calculateRating(age: int) -> int:
  if age <= 18:
    return random.randint(40,60)
  elif age <= 20:
    return random.randint(45,70)
  elif age <= 22:
    return random.randint(50,80)
  elif age <= 24:
    return random.randint(55,90)
  elif age <= 26:
    return random.randint(60,99)
  elif age <= 28:
    return random.randint(55,95)
  elif age <= 30:
    return random.randint(50,90)
  elif age <= 32:
    return random.randint(45,85)
  elif age <= 34:
    return random.randint(40,80)

async def calculatePotential(age: int, rating: int) -> int:
  remainingYears = MAX_AGE - int(age)
  potential = 0
  if remainingYears <= 2:
    potential = random.randint(rating,rating + 5)
  elif remainingYears <= 4:
    potential = random.randint(rating,rating + 10)
  elif remainingYears <= 6:
    potential = random.randint(rating,rating + 15)
  elif remainingYears <= 8:
    potential = random.randint(rating,rating + 20)
  elif remainingYears <= 10:
    potential = random.randint(rating,rating + 25)
  elif remainingYears <= 12:
    potential = random.randint(rating,rating + 30)
  elif remainingYears <= 14:
    potential = random.randint(rating,rating + 35)
  elif remainingYears <= 16:
    potential = random.randint(rating,rating + 40)
  elif remainingYears <= 19:
    potential = random.randint(rating,rating + 50)
  if potential > 99:
    potential = 99
  return int(potential)