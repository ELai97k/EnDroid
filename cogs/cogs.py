import discord
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions, CommandError

class Cogs(commands.Cog):
    """Commands for loading, unloading, and reloading cogs."""
    def __init__(self, client):
        self.client = client

    # load cogs
    @commands.command(help="Command for loading cogs.")
    @has_permissions(manage_roles=True)
    async def load(self, ctx, extension):
        if ctx.author == self.client.user:
            return
        if ctx.author.bot:
            return

        embed = discord.Embed (
            title = "Operation Successful!",
            description = f"Cog name `{extension}` has been loaded successfully and your changes were saved.",
            color=0x198C19
        )
        await ctx.channel.typing()
        await ctx.send(embed=embed)
        await self.client.load_extension(f'cogs.{extension}')
        print(f'Loading {extension}')

    @load.error
    async def load_error(self, ctx, error):
        if isinstance(error, MissingPermissions):
            await ctx.send("You do not have permission to use this command!")

        if isinstance(error, CommandError):
            embed = discord.Embed (
                title = "Command Error",
                description = "Pls load something, like a cog. But not your idiot brain!\n```Could not complete your request!```",
                color = discord.Color.dark_red()
            )
            await ctx.send(embed=embed)
            print(f"{self.client.user} Error 404: Command Error")


    # unload cogs
    @commands.command(help="Command for unloading cogs.")
    @has_permissions(manage_roles=True)
    async def unload(self, ctx, extension):
        if ctx.author == self.client.user:
            return
        if ctx.author.bot:
            return

        embed = discord.Embed (
            title = "Operation Successful!",
            description = f"Cog name `{extension}` has been unloaded successfully and your changes were saved.",
            color=0x198C19
        )
        await ctx.channel.typing()
        await ctx.send(embed=embed)
        await self.client.unload_extension(f'cogs.{extension}')
        print(f'Unloading {extension}')

    @unload.error
    async def unload_error(self, ctx, error):
        if isinstance(error, MissingPermissions):
            await ctx.send("You do not have permission to use this command!")

        if isinstance(error, CommandError):
            embed = discord.Embed (
                title = "Command Error",
                description = "Pls unload your dumb brain, thanks!\n```Could not complete your request!```",
                color = discord.Color.dark_red()
            )
            await ctx.send(embed=embed)
            print(f"{self.client.user} Error 404: Command Error")


    # reload cogs
    @commands.command(help="Command for reloading cogs.")
    @has_permissions(manage_roles=True)
    async def reload(self, ctx, extension):
        if ctx.author == self.client.user:
            return
        if ctx.author.bot:
            return

        embed = discord.Embed (
            title = "Operation Successful!",
            description = f"Cog name `{extension}` has been reloaded successfully and your changes were saved.",
            color=0x198C19
        )
        await ctx.channel.typing()
        await ctx.send(embed=embed)
        await self.client.reload_extension(f'cogs.{extension}')
        print(f'Reloading {extension}')

    @reload.error
    async def reload_error(self, ctx, error):
        if isinstance(error, MissingPermissions):
            await ctx.send("You do not have permission to use this command!")

        if isinstance(error, CommandError):
            embed = discord.Embed (
                title = "Command Error",
                description = "Reload what? Your stupidity? No way!\n```Could not complete your request!```",
                color = discord.Color.dark_red()
            )
            await ctx.send(embed=embed)
            print(f"{self.client.user} Error 404: Command Error")


async def setup(client):
    await client.add_cog(Cogs(client))

async def teardown(client):
    await client.remove_cog(Cogs(client))