import discord
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions

class Speak(commands.Cog):
    """Control the bot to say anything"""
    def __init__(self, client):
        self.client = client

    # say command
    @commands.command()
    @commands.has_role("Moderators")
    @has_permissions(manage_messages=True)
    async def speak(self, ctx, *, message=None):
        if ctx.author == self.client.user:
            return
        if ctx.author.bot:
            return

        if message == None:
            await ctx.send("What do you want me to say?")

        else:
            # G Bar general channel 762317365970468877
            await self.client.get_channel(762317365970468877).send(f"{message}")
            await ctx.message.delete()

    @speak.error
    async def speak_error(self, ctx, error):
        if isinstance(error, MissingPermissions):
            await ctx.send("You do not have permission to use this command!")

def setup(client):
    client.add_cog(Speak(client))