import discord
from discord.ext import commands

class Say(commands.Cog):
    """Control the bot to say anything"""
    def __init__(self, client):
        self.client = client

    # say command
    @commands.command()
    @commands.has_role("Moderators")
    async def say(self, ctx, *, message=None):
        if ctx.author == self.client.user:
            return

        if message == None:
            await ctx.send("What do you want me to say?")

        else:
            await self.client.get_channel(911112792646508627).send(f"{message}")
            await ctx.message.delete()


def setup(client):
    client.add_cog(Say(client))