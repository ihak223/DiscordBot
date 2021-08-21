import discord
from discord.ext import tasks
import time
import threading
from exts.twitch import *
import sys
import random
import json


class BotClient(discord.Client):

    def __init__(self, token, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # sets object attributes
        self.memory = []
        self.token = token
        self.msg = "@everyone v0ltpat is currently live on:\nhttps://www.twitch.tv/v0ltpat"
        self.msged = False
        self.background_tasks.start()

    # background tasks
    @tasks.loop(seconds=10)
    async def background_tasks(self):
        print("[Internal] Looping background tasks")
        # Check If Pat Is Online
        i = 0
        if is_online("v0ltpat"):

            # Sends MSG To Channel
            if not self.msged:
                print("[Internal] v0ltpat is online")
                channel = self.get_channel(872972403368677437)
                await channel.send(self.msg)
                self.msged = True
                print("[Internal] Sent Announcement")
            else:
                print(self.msged)

        else:
            if i <= 3:
                self.msged = False
                i = 0
            else:
                i += 1


    @background_tasks.before_loop
    async def before_tasks(self):
        print("[Internal] Running background tasks")
        await self.wait_until_ready()  # wait until the bot logs in

    # Run Discord Client
    def run_client(self):
        self.run(self.token)

    # Bot Ready Function
    async def on_ready(self):
        print(f"[Internal] Bot logged in as : '{self.user}'")

    # Message Function
    async def on_message(self, m):
        print(f"[Internal] Message in channel : '{m.channel.name}', content : '{m.content}'")
        if m.author == self.user:
            return
        if m.content == "live":
            if is_online("v0ltpat"):

                await m.channel.send('''
                v0ltpat is currently live on:
                https://www.twitch.tv/v0ltpat
                ''')

            else:
                await m.channel.send("v0ltpat is not currently live right now:\nhttps://www.twitch.tv/v0ltpat")
        elif m.content == "sources":
            await m.channel.send("https://github.com/ihak223/DiscordBot")
        elif m.content.split(":")[0] == "cadd":
            central_command = m.content.split(":")[1]
            file = json.loads(open("responses\\responses.json").read())
            string = "{\""+central_command.split(", ")[0].lstrip()+"\": "+"[\""+central_command.split(", ")[1].lstrip()+"\"]"+"}"
            z = {**file, **json.loads(string)}
            open("responses\\responses.json", "w").write(json.dumps(z))
        # elif m.content.split()[0] == "memory":
            # if m.content.split()[1] == "add":

        else:
            try:
                responses = json.loads(open("responses\\responses.json", "r").read())
                print("[Internal] Sent : " + random.choice(responses[m.content.lower()]))
                response = random.choice(responses[m.content.lower()])
                if response[0] == "%":
                    exec(response[1:])
                else:
                    await m.channel.send(response)
            except KeyError:
                print("[Internal] No Command")



bot = BotClient(sys.argv[1])
bot.run_client()
