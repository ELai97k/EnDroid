import discord
import random
from discord.ext import commands, tasks


class Bot_Statuses(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.random_status_loop.start()

    # bot watching statuses
    @tasks.loop(seconds=999.0)
    async def random_status_loop(self):
        status = [
            "Biomutant",
            "The Stanley Parable Demonstration",
            "The Stanley Parable HD Remix",
            "The Stanley Parable 2013",
            "The Stanley Parable: Ultra Deluxe",
            "The Stanley Parable 2",
            "The Stanley Parable 8",
            "Eight Game",
            "Nintendo Switch Sports",
            "Sine Mora",
            "Sine Mora EX",
            "Splitgate",
            "Among Us",
            "Tech Support: Error Unknown"
        ]

        await self.client.change_presence (
            activity=discord.Activity (
            type=discord.ActivityType.playing, name=f'{random.choice(status)}'))


def setup(client):
    client.add_cog(Bot_Statuses(client))