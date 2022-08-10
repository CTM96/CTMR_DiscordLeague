from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
  return "DEBUG - Processing DiscordLeague server"

def run():
  app.run(host='0.0.0.0', port = 8080)

def loadServer():
  t = Thread(target=run)
  t.start()