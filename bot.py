import discord
from discord.ext import tasks
import time
import threading
from exts.twitch import *
import sys


class BotClient(discord.Client):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.msg = "@everyone v0ltpat is currently live on:\nhttps://www.twitch.tv/v0ltpat"
        self.msged = False
        self.check.start()

    # Run Twitch Check
    @tasks.loop(seconds=10)
    async def check(self):
        # Check If Pat Is Online
        if not is_online("v0ltpat"):
            # Sends MSG To Channel
            if self.msged:
                print("[Internal] v0ltpat is online")
                channel = self.get_channel(872972403368677437)
                await channel.send(self.msg)
                self.msged = True
                print("[Internal] Sent Announcement")
        else:
            self.msged = False

    @check.before_loop
    async def before_my_task(self):
        await self.wait_until_ready()  # wait until the bot logs in

    # Run Discord Client
    def run_client(self):
        self.run(sys.argv[1])

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
        elif m.content == "ping":
            await m.channel.send("pong!")
        elif m.content == "sources":



bot = BotClient()
bot.run(sys.argv[1])
