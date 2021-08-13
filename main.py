import discord
import time
import threading
from exts.twitch import *
import sys

# Client
client = discord.Client()

print("Booting bot ... ")

# Run Twitch Check
def run_check():
    while True:
        # Check If Pat Is Online
        if is_online("v0ltpat"):
            # Sends MSG To Channel
            channel = client.get_channel(875567716411539517)
            channel.send("@everyone\nv0ltpat is currently live:\nhttps://www.twitch.tv/v0ltpat")
        print("[Internal] Checked")
        time.sleep(10)

# Run Discord Client
def run_client():
    client.run(sys.argv[1])

# Bot Ready Function
@client.event
async def on_ready():
    print(f"[Internal] Bot logged in as : '{client.user}'")

# Message Function
@client.event
async def on_message(m):
    print(f"[Internal] Message in channel : '{m.channel.name}', content : '{m.content}'")
    if m.author == client.user:
        return
    if m.content == "$live":
        if is_online("v0ltpat"):
            await m.channel.send('''
            v0ltpat is currently live on:
            https://www.twitch.tv/v0ltpat
            ''')

        else:
            await m.channel.send("v0ltpat is not currently live right now:\nhttps://www.twitch.tv/v0ltpat")

# Running Threads
check = threading.Thread(target=run_check)
dcman = threading.Thread(target=run_client())

dcman.start()
check.start()

