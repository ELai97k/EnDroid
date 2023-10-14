import discord
import random
from discord.ext import commands, tasks

class Statuses_Playing(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.random_status_loop.start()

    @tasks.loop(seconds=999.0)
    async def random_status_loop(self):
        statuses = [
            "The Stanley Parable Ultra Deluxe",
            "Stardew Valley",
            "Beat Saber",
            "Job Simulator",
            "chess.com",
            "Minecraft",
            "Team Fortress 2",
            "Animal Crossing New Horizons",
            "Splatoon 3",
            "Mario Kart 8 Deluxe",
            "Persona 3",
            "Persona 3 FES",
            "Persona 3 Portable",
            "Persona 4",
            "Persona 4 Golden",
            "Persona 5",
            "Persona 5 Royal",
            "Forza Horizon",
            "Forza Horizon 2",
            "Forza Horizon 3",
            "Forza Horizon 4",
            "Forza Horizon 5",
            "Discord",
            "GitHub",
            "YouTube",
            "Spotify"
        ]
        await self.client.change_presence (
            activity = discord.Activity (
                type = discord.ActivityType.playing, name = {random.choice(statuses)}
            )
        )


async def setup(client):
    await client.add_cog(Statuses_Playing(client))

async def teardown(client):
    await client.remove_cog(Statuses_Playing(client))