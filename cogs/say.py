import discord
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions

class Say(commands.Cog):
    """Control the bot to say anything"""
    def __init__(self, client):
        self.client = client

    # say command
    @commands.command()
    @has_permissions(administrator=True)
    async def say(self, ctx, *, message=None):
        if ctx.author == self.client.user:
            return
        if ctx.author.bot:
            return

        if message == None:
            await ctx.send("What do you want me to say?")

        else:
            await self.client.get_channel(911112792646508627).send(f"{message}")
            await ctx.message.delete()

    @say.error
    async def say_error(self, ctx, error):
        if isinstance(error, MissingPermissions):
            await ctx.send("You do not have permission to use this command!")

def setup(client):
    client.add_cog(Say(client))