from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions

class Echo(commands.Cog):
    """Control the bot to say anything."""
    def __init__(self, client):
        self.client = client

    # say command for admin only
    @commands.command(help="Make the bot say your message input.")
    @has_permissions(administrator=True)
    async def say(self, ctx, *, message=None):
        if ctx.author == self.client.user:
            return
        if ctx.author.bot:
            return

        if message is None:
            await ctx.send("What do you want me to say?")

        else:
            # main server general channel 1010841256294875218
            await self.client.get_channel(1010841256294875218).send(f"{message}")
            await ctx.message.delete()

    @say.error
    async def say_error(self, ctx, error):
        if isinstance(error, MissingPermissions):
            await ctx.send("You do not have permission to use this command!")


    # speak command for moderators
    @commands.command(help="Make the bot speak your message input.")
    @commands.has_role("Moderators")
    @has_permissions(manage_messages=True)
    async def speak(self, ctx, *, message=None):
        if ctx.author == self.client.user:
            return
        if ctx.author.bot:
            return

        if message is None:
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
    client.add_cog(Echo(client))

def teardown(client):
    client.remove_cog(Echo(client))