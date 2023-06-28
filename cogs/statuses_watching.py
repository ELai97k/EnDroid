import discord
import random
from discord.ext import commands, tasks

class Statuses_Watching(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.random_status_loop.start()

    @tasks.loop(seconds=999.0)
    async def random_status_loop(self):
        statuses = [
            "you",
            "you bloom in the light of the moon",
            "this server",
            "Game Theory",
            "Film Theory",
            "Matatabi Movie Labo",
            "YouTube",
            "Netflix",
            "Disney+",
            "Amazon Prime Video",
            "Everything Everywhere All At Once",
            "Spider-Man: Across the Spider-Verse",
            "The Super Mario Bros. Movie",
            "Transformers: Rise of the Beasts",
            "The Grand Tour: A Scamdi Flick",
            "The Grand Tour: Eurocrash",
            "American Born Chinese",
            "Attack On Titan",
            "My Hero Academia"
        ]
        await self.client.change_presence (
            activity = discord.Activity (
                type = discord.ActivityType.watching, name = f'{random.choice(statuses)}'
            )
        )


async def setup(client):
    await client.add_cog(Statuses_Watching(client))

async def terdown(client):
    await client.remove_cog(Statuses_Watching(client))