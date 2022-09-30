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
            "Youtube",
            "Matatabi Movie Labo",
            "マタタビムービーラボ",
            "Spring of Birth",
            "Midsummer Knight's Dream",
            "Falling Down",
            "Winter of Rebirth",
            "Netflix",
            "Oddballs",
            "Wendell and Wild",
            "Tekken: Bloodline",
            "The Shaman King 2021",
            "Nobody's Looking",
            "Ninguém Tá Olhando",
            "Spy x Family season 2",
            "Mob Psycho 100 season 3",
            "My Hero Academia season 6",
            "The Rings of Power",
            "The Grand Tour: A Scandi Flick"
        ]
        await self.client.change_presence (
            activity = discord.Activity (
                type = discord.ActivityType.watching, name = f'{random.choice(status)}'
            )
        )


def setup(client):
    client.add_cog(BotStatuses(client))