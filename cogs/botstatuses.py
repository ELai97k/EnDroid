import discord
import asyncio
from discord.ext import commands

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
            type = discord.ActivityType.watching, name = "VLC Media Player"
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
            type = discord.ActivityType.playing, name = "Nintendo Switch"
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
            type = discord.ActivityType.listening, name = "El Condor Pasa"
            )
        )
        await asyncio.sleep(999)
        await self.client.change_presence (
            activity = discord.Activity (
            type = discord.ActivityType.playing, name = "PCSX2 1.6.0"
            )
        )
        await asyncio.sleep(999)
        await self.client.change_presence (
            activity = discord.Activity (
            type = discord.ActivityType.playing, name = "Xenia Canary"
            )
        )
        await asyncio.sleep(999)
        await self.client.change_presence (
            activity = discord.Activity (
            type = discord.ActivityType.playing, name = "PPSSPP"
            )
        )
        await asyncio.sleep(999)
        await self.client.change_presence (
            activity = discord.Activity (
            type = discord.ActivityType.playing, name = "Drastic"
            )
        )
        await asyncio.sleep(999)
        await self.client.change_presence (
            activity = discord.Activity (
            type = discord.ActivityType.watching, name = "Bohemian Rhapsody"
            )
        )
        await asyncio.sleep(999)
        await self.client.change_presence (
            activity = discord.Activity (
            type = discord.ActivityType.listening, name = "Bohemian Rhapsody"
            )
        )
        await asyncio.sleep(999)
        await self.client.change_presence (
            activity = discord.Activity (
            type = discord.ActivityType.playing, name = "ProPresenter"
            )
        )
        await asyncio.sleep(999)
        await self.client.change_presence (
            activity = discord.Activity (
            type = discord.ActivityType.playing, name = "VLC Media Player"
            )
        )
        await asyncio.sleep(999)
        await self.client.change_presence (
            activity = discord.Activity (
            type = discord.ActivityType.listening, name = "VLC Media Player"
            )
        )


async def setup(client):
    await client.add_cog(BotStatuses(client))

async def teardown(client):
    await client.remove_cog(BotStatuses(client))