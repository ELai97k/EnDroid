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
            "Food Theory",
            "Style Theory",
            "Matatabi Movie Labo",
            "マタタビムービーラボ",
            "からめる",
            "YouTube",
            "TikTok",
            "Twitch",
            "Netflix",
            "Disney+",
            "Amazon Prime Video",
            "Apple TV+",
            "The Creator",
            "Barbie",
            "Oppenheimer",
            "Barbenheimer",
            "Bluey",
            "Spy X Family"
        ]
        await self.client.change_presence (
            activity = discord.Activity (
                type = discord.ActivityType.watching, name = {random.choice(statuses)}
            )
        )


async def setup(client):
    await client.add_cog(Statuses_Watching(client))

async def terdown(client):
    await client.remove_cog(Statuses_Watching(client))