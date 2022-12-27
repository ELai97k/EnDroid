import discord
import random
from discord.ext import commands, tasks

class BotStatuses(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.random_status_loop.start()

    # bot statuses (will change from time to time)
    @tasks.loop(seconds=999.0)
    async def random_status_loop(self):
        status = [
            "myself",
            "on Raspberry Pi 3",
            "Forza Horizon 5",
            "Persona 5 Royal",
            "Xbox PC Game Pass",
            "Ren'Py 8",
            "Visual Studio Code",
            "YouTube",
            "GitHub",
            "Spotify",
            "SoundCloud",
            "Discord",
            "Minecraft",
            "Hearthstone",
            "Hagar's Ordeal",
            "The Sims 3",
            "Among Us Hide n Seek",
        ]
        await self.client.change_presence (
            activity = discord.Activity (
                type = discord.ActivityType.watching, name = f'{random.choice(status)}'
            )
        )


def setup(client):
    client.add_cog(BotStatuses(client))

def teardown(client):
    client.remove_cog(BotStatuses(client))