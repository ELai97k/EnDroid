import discord
from discord.ext import commands
import asyncio

class Remindme(commands.Cog):
    """Reminder command 2 (input the time first, then your reminder text)"""
    def __iniy__(self, client):
        self.client = client



def setup(client):
    client.add_cog(Remindme(client))