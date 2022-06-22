import discord
from discord.ext import commands

class Say(commands.Cog):
    """Control the bot to say anything"""
    def __init__(self, client):
        self.client = client

    # say command
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def speak(self, ctx, *, message=None):
        if ctx.author == self.client.user:
            return

        if message == None:
            await ctx.send("What do you want me to say?")
            await ctx.message.delete()

        else: # general channel ID = 762317365970468877
            await self.client.get_channel(768537268452851754).send(f"{message}")
            await ctx.message.delete()


def setup(client):
    client.add_cog(Say(client))