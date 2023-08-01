import discord
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions

class Status(commands.Cog):
    """Custom bot statuses."""
    def __init__(self, client):
        self.client = client

    @commands.command(help="Set custom bot status.")
    @has_permissions(administrator=True, manage_roles=True)
    async def change_status(self, ctx, type, newstatus=None):
        if ctx.author == self.client.user:
            return
        if ctx.author.bot:
            return
        
        types = {
            "playing":discord.ActivityType.playing,
            "watching":discord.ActivityType.watching,
            "listening":discord.ActivityType.listening,
            "default":await self.client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="Sunshine Day"))
        }
        if type.lower() == "default":
            await self.client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="Sunshine Day"))
            await ctx.send("Changed to default status!")
        try:
            await self.client.change_presence(activity=discord.Activity(type=types[type.lower()], name=newstatus))
            await ctx.send("Changed status!")

        except KeyError:
            # invalid status type
            await ctx.send("Invalid status! Unable to display status.")
            return

    @change_status.error
    async def change_status_error(self, ctx, error):
        if isinstance(error, MissingPermissions):
            await ctx.send("You do not have permission to use this command!")


async def setup(client):
    await client.add_cog(Status(client))

async def teardown(client):
    await client.remove_cog(Status(client))