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
            "Splatoon 3",
            "Nintendo Switch Sports",
            "Animal Crossing New Horizons",
            "Taiko no Tatsujin: Drum 'n' Fun",
            "The Stanley Parable",
            "The Stanley Parable Ultra Deluxe",
            "The Stanley Parable 2",
            "The Stanley Parable 3: Offline Tuesday",
            "The Stanley Parable 4: Attack On Co-workers",
            "Hearthstone",
            "Forza Horizon 1",
            "Forza Horizon 2",
            "Forza Horizon 3",
            "Forza Horizon 4",
            "Forza Horizon 5",
            "Sine Mora",
            "Sine Mora EX",
            "The Journey Down Chapter 1",
            "The Journey Down Chapter 2",
            "The Journey Down Chapter 3",
            "Flipping Death",
            "Hollow Knight",
            "Shovel Knight",
            "Persona 3",
            "Persona 3 FES",
            "Persona 3 Portable",
            "Persona 4",
            "Persona 4 Golden",
            "Persona 5",
            "Persona 5 Royal",
            "Worms 4 Mayhem",
            "Worms Ultimate Mayhem",
            "MapleStory",
            "Club Penguin",
            "Club Penguin Rewritten"
        ]

        await self.client.change_presence (
            activity=discord.Activity (
            type=discord.ActivityType.playing, name=f'{random.choice(status)}'))


def setup(client):
    client.add_cog(Bot_Statuses(client))