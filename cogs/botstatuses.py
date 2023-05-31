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
            "The Stanley Parable Ultra Deluxe",
            "Stardew Valley",
            "Among Us",
            "Job Simulator",
            "Team Fortress 2",
            "Splitgate",
            "Minecraft",
            "Minecraft Dungeons",
            "Biomutant",
            "Discord",
            "GitHub",
            "Ren'Py"
        ]
        await self.client.change_presence (
            activity = discord.Activity (
                type = discord.ActivityType.playing, name = f'{random.choice(status)}'
            )
        )


async def setup(client):
    await client.add_cog(BotStatuses(client))

async def teardown(client):
    await client.remove_cog(BotStatuses(client))