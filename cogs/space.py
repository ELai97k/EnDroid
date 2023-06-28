from discord.ext import commands

class Space(commands.Cog):
    """Space cog"""
    def __init__(self, client):
        self.client



async def setup(client):
    await client.add_cog(Space(client))

async def teardown(client):
    await client.remove_cog(Space(client))