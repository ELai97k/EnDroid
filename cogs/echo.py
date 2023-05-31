import discord
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions, CommandError

class Echo(commands.Cog):
    """Control the bot to say anything."""
    def __init__(self, client):
        self.client = client

    # say command for admin only
    @commands.command(help="Make the bot say your message input.")
    @has_permissions(manage_roles=True)
    async def say(self, ctx, *, message=None):
        if ctx.author == self.client.user:
            return
        if ctx.author.bot:
            return

        if message is None:
            await ctx.send("What do you want me to say?")

        else:
            # main server general channel
            await self.client.get_channel(1010841256294875218).send(f"{message}")
            await ctx.message.delete()

    @say.error
    async def say_error(self, ctx, error):
        if isinstance(error, MissingPermissions):
            await ctx.send("You do not have permission to use this command!")

        if isinstance(error, CommandError):
            embed = discord.Embed (
                title = "Command Error",
                description = "Pls try again!\n```Could not complete your request!```",
                color = discord.Color.dark_red()
            )
            await ctx.send(embed=embed)
            print(f"{self.client.user} Error 404: Command Error")


    # speak command for moderators
    @commands.command(help="Make the bot speak your message input.")
    @has_permissions(manage_messages=True)
    async def speak(self, ctx, *, message=None):
        if ctx.author == self.client.user:
            return
        if ctx.author.bot:
            return

        if message is None:
            await ctx.send("What do you want me to say?")

        else:
            # G Bar general channel
            await self.client.get_channel(762317365970468877).send(f"{message}")
            await ctx.message.delete()

    @speak.error
    async def speak_error(self, ctx, error):
        if isinstance(error, MissingPermissions):
            await ctx.send("You do not have permission to use this command!")

        if isinstance(error, CommandError):
            embed = discord.Embed (
                title = "Command Error",
                description = "Pls try again!\n```Could not complete your request!```",
                color = discord.Color.dark_red()
            )
            await ctx.send(embed=embed)
            print(f"{self.client.user} Error 404: Command Error")


async def setup(client):
    await client.add_cog(Echo(client))

async def teardown(client):
    await client.remove_cog(Echo(client))