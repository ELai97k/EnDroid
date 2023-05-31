import discord
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions, CommandError

class ClearChat(commands.Cog):
    """Cog for clearing chat command."""
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["clear"], pass_context=True, help="Command to clear chats in a text channel.")
    @has_permissions(manage_messages=True)
    async def clearchat(self, ctx, amount=5):
        if ctx.author == self.client.user:
            return
        if ctx.author.bot:
            return

        await ctx.channel.purge(limit=amount+1)
        print(f"Cleared {amount} chats successful!")

        if amount is None:
            await ctx.channel.purge(limit=50+1)
            print(f"Cleared {amount} chats successful!")

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


async def setup(client):
    await client.add_cog(ClearChat(client))

async def teardown(client):
    await client.remove_cog(ClearChat(client))