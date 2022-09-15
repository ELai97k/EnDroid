import discord
import random
from discord.ext import commands, tasks

class Bot_Statuses(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.random_status_loop.start()

    # bot statuses
    @tasks.loop(seconds=999.0)
    async def random_status_loop(self):
        status = [
            "Stack Overflow",
            "Discord",
            "Biomutant",
            "The Stanley Parable Demonstration",
            "The Stanley Parable: Ultra Deluxe",
            "The Stanley Parable 2",
            "Nintendo Switch Sports",
            "Splatoon 3",
            "Sine Mora",
            "Sine Mora EX",
            "Splitgate",
            "Among Us",
            "The Sims 3",
            "The Sims 4",
            "Minecraft",
            "Fall Guys"
        ]
        await self.client.change_presence (
            activity = discord.Activity (
                type = discord.ActivityType.playing, name = f'{random.choice(status)}'
            )
        )


def setup(client):
    client.add_cog(Bot_Statuses(client))