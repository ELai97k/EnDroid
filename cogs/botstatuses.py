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
            "Visual Studio Code",
            "on Raspberry Pi 3",
            "Persona 4 Golden",
            "Stardew Valley",
            "Biomutant",
            "Minecraft",
            "Minecraft Dungeons",
            "SteamVR",
            "Beat Saber",
            "Job Simulator: The 2050 Archives",
            "Job Simulator",
            "Vacation Simulator",
            "Vacation Simulator: Back To Job",
            "Adobe Photoshop",
            "Adobe Premiere Pro",
            "Aseprite",
            "YouTube",
            "GitHub",
            "Spotify",
            "SoundCloud",
            "Discord",
            "Godot",
            "Ren'Py",
            "Hagar's Ordeal"
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