import discord
import asyncio
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions, CommandError

class Botcog(commands.Cog):
    """Bot cog for logging out."""
    def __init__(self, client):
        self.client = client

    # log out
    @commands.command(help="Command for bot log out.")
    @has_permissions(administrator=True)
    async def logout(self, ctx):
        if ctx.author == self.client.user:
            return
        if ctx.author.bot:
            return
        
        await ctx.channel.trigger_typing()
        await ctx.send(f"```{self.client.user} logging out...\nReminder: Log me back in manually through the terminal.```")
        
        print(f"{self.client.user} logging out...")
        print("Reminder: Log me back in manually.")

        await asyncio.sleep(3)
        await self.client.change_presence(status=discord.Status.offline)
        await asyncio.sleep(3)
        await self.client.close()

    @logout.error
    async def logout_error(self, ctx, error):
        if isinstance(error, MissingPermissions):
            await ctx.send("You do not have permission to use this command!")

        if isinstance(error, CommandError):
            embed = discord.Embed (
                title = "Command Error",
                description = "Could not complete your request! Pls type properly, idiot!",
                color = discord.Color.dark_red()
            )
            await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Botcog(client))

def teardown(client):
    client.remove_cog(Botcog(client))