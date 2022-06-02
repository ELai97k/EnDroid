import discord
from discord.ext import commands

class Main_Cog(commands.Cog):
    """This is a main cog for bot's login and status and sending welcome and goodbye message embeds for new members"""
    def __init__(self, client):
        self.client = client

    # bot login
    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{self.client.user} logged in successfully!")

    


def setup(client):
    client.add_cog(Main_Cog(client))