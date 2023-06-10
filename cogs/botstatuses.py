import discord
import asyncio
from discord.ext import commands, tasks

class BotStatuses(commands.Cog):
    def __init__(self, client):
        self.client = client
        
    @commands.Cog.listener()
    async def on_ready(self):
        # bot login
        print(f"{self.client.user} logged in successfully!")

        await self.client.change_presence (
            activity = discord.Activity (
            type = discord.ActivityType.playing, name = "!help"
            )
        )
        await asyncio.sleep(999)
        await self.client.change_presence (
            activity = discord.Activity (
            type = discord.ActivityType.playing, name = "Visual Studio Code"
            )
        )
        await asyncio.sleep(999)
        await self.client.change_presence (
            activity = discord.Activity (
            type = discord.ActivityType.playing, name = "myself"
            )
        )
        await asyncio.sleep(999)
        await self.client.change_presence (
            activity = discord.Activity (
            type = discord.ActivityType.playing, name = "discord.py"
            )
        )
        await asyncio.sleep(999)
        await self.client.change_presence (
            activity = discord.Activity (
            type = discord.ActivityType.playing, name = "!help"
            )
        )
        await asyncio.sleep(999)
        await self.client.change_presence (
            activity = discord.Activity (
            type = discord.ActivityType.playing, name = "Visual Studio Code"
            )
        )
        await asyncio.sleep(999)
        await self.client.change_presence (
            activity = discord.Activity (
            type = discord.ActivityType.playing, name = "myself"
            )
        )
        await asyncio.sleep(999)
        await self.client.change_presence (
            activity = discord.Activity (
            type = discord.ActivityType.playing, name = "discord.py"
            )
        )


async def setup(client):
    await client.add_cog(BotStatuses(client))

async def teardown(client):
    await client.remove_cog(BotStatuses(client))