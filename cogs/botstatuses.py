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
            type = discord.ActivityType.listening, name = "The Sound of Silence"
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
            type = discord.ActivityType.listening, name = "This Wandering Day"
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
            type = discord.ActivityType.listening, name = "Where The Shadows Lie"
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
        await asyncio.sleep(999)
        await self.client.change_presence (
            activity = discord.Activity (
            type = discord.ActivityType.playing, name = "SPAAACCCCCE!"
            )
        )
        await asyncio.sleep(999)
        await self.client.change_presence (
            activity = discord.Activity (
            type = discord.ActivityType.watching, name = "The Lord of the Rings: The Rings of Power"
            )
        )
        await asyncio.sleep(999)
        await self.client.change_presence (
            activity = discord.Activity (
            type = discord.ActivityType.playing, name = "on Raspberry Pi 3"
            )
        )
        await asyncio.sleep(999)
        await self.client.change_presence (
            activity = discord.Activity (
            type = discord.ActivityType.watching, name = "SPAAACCCCCE!"
            )
        )


async def setup(client):
    await client.add_cog(BotStatuses(client))

async def teardown(client):
    await client.remove_cog(BotStatuses(client))