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
            "Xbox PC Game Pass",
            "Persona 5 Royal",
            "Persona 4 Golden",
            "Persona 3 Portable",
            "Hi-Fi Rush",
            "Forza Horizon 5"
            "Pico Neo 3",
            "Beat Saber",
            "Discord",
            "YouTube",
            "Spotify",
            "Ren'Py 8"
            "Adobe Photoshop 2022"
        ]
        await self.client.change_presence (
            activity = discord.Activity (
                type = discord.ActivityType.playing, name = f'{random.choice(status)}'
            )
        )


def setup(client):
    client.add_cog(BotStatuses(client))

def teardown(client):
    client.remove_cog(BotStatuses(client))