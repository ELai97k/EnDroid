import discord
import random
from discord.ext import commands, tasks

class Bot_Statuses(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.random_status_loop.start()

    # bot statuses (will change from time to time)
    @tasks.loop(seconds=999.0)
    async def random_status_loop(self):
        status = [
            "Youtube",
            "からめる",
            "マタタビムービーラボ",
            "Netflix",
            "Spy x Family season 2",
            "Mob Psycho 100 season 3",
            "Oddballs",
            "Wendell and Wild",
            "Tekken: Bloodline",
            "The Shaman King",
            "The Rings of Power",
            "The Grand Tour: A Scandi Flick"
        ]
        await self.client.change_presence (
            activity = discord.Activity (
                type = discord.ActivityType.watching, name = f'{random.choice(status)}'
            )
        )


def setup(client):
    client.add_cog(Bot_Statuses(client))