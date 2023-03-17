import discord
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions, CommandError

class ClearChat(commands.Cog):
    """Cog for clearing chat command."""
    def __init__(self, client):
        self.client = client

    @commands.command(pass_context=True, help="Command to clear chats in a text channel.")
    @has_permissions(manage_messages=True)
    async def clearchat(self, ctx, amount=None):
        if ctx.author == self.client.user:
            return
        if ctx.author.bot:
            return

        if amount is None:
            await ctx.channel.purge(limit=50)
            print("Clear chat successful!")
        else:
            try:
                int(amount)
            except:
                await ctx.send("Please enter a valid integer as amount.")
            else:
                await ctx.channel.purge(linit=amount)
                print("Clear chat successful!")

    @clearchat.error
    async def clearchat_error(self, ctx, error):
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


def setup(client):
    client.add_cog(ClearChat(client))

def teardown(client):
    client.remove_cog(ClearChat(client))