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
            "Xbox PC Game Pass",
            "Forza Horizon 5",
            "Persona 5 Royal",
            "Persona 4 Golden",
            "Persona 3 Portable",
            "The Last of Us Part 1",
            "SteamVR",
            "Beat Saber",
            "Job Simulator: The 2050 Archives",
            "Vacation Simulator",
            "Vacation Simulator: Back To Job",
            "Adobe Photoshop 2022",
            "Adobe Illustrator 2022",
            "Adobe After Effects 2022",
            "Adobe Premiere Pro 2022",
            "Adobe Animate 2022",
            "YouTube",
            "GitHub",
            "Spotify",
            "SoundCloud",
            "Discord",
            "Ren'Py",
            "Hagar's Ordeal",
            "I need new statuses!!"
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