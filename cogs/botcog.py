import discord
import asyncio
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions

class Botcog(commands.Cog):
    """Bot cog."""
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
        await self.client.logout()

    @logout.error
    async def logout_error(self, ctx, error):
        if isinstance(error, MissingPermissions):
            await ctx.send("You do not have permission to use this command!")


def setup(client):
    client.add_cog(Botcog(client))

def teardown(client):
    client.remove_cog(Botcog(client))