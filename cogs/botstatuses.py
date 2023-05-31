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
        playing_statuses = [
            "myself",
            "Visual Studio Code",
            "The Stanley Parable Ultra Deluxe",
            "Stardew Valley",
            "The Sims 3",
            "The Sims 4",
            "Splitgate",
            "Minecraft",
            "Minecraft Dungeons",
            "Biomutant",
            "Animal Crossing New Horizons",
            "Splatoon 3",
            "Persona 3",
            "Persona 3 FES",
            "Persona 3 Portable",
            "Persona 4",
            "Persona 4 Golden",
            "Persona 5",
            "Persona 5 Royal",
            "Discord",
            "GitHub",
            "Ren'Py",
            "YouTube",
            "Spotify"
        ]
        await self.client.change_presence (
            activity = discord.Activity (
                type = discord.ActivityType.playing, name = f'{random.choice(playing_statuses)}'
            )
        )


@tasks.loop(seconds=999.0)
async def random_status_loop(self):
    watching_statuses = [
        "you",
        "this server",
        "YouTube",
        "Game Theory",
        "Film Theory",
        "Matatabi Movie Labo",
        "Netflix",
        "Disney+",
        "Everything Everywhere All At Once",
        "American Born Chinese",
        "Attack On Titan",
        "My Hero Academia",
        "Mob Psycho 100",
        "Shaman King",
        "Spider-Man: Across the Spider-Verse",
        "The Super Mario Bros. Movie",
        "Wendell & Wild",
        "Turning Red",
        "Encanto",
        "The Mitchells vs. the Machines"
    ]
    await self.client.change_presence (
        activity = discord.Activity (
            type = discord.ActivityType.watching, name = f'{random.choice(watching_statuses)}'
        )
    )


async def setup(client):
    await client.add_cog(BotStatuses(client))

async def teardown(client):
    await client.remove_cog(BotStatuses(client))