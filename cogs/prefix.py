import discord
import json
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions, CommandError

class Prefix(commands.Cog):
    """Cog for the bot's prefixes."""
    def __init__(self, client):
        self.client = client

    # add default prefix and guild id to json file when bot joins server
    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        with open("prefixes.json", "r") as f:
            prefixes = json.load(f)

        # default prefix
        prefixes[str(guild.id)] = "!"

        with open("prefixes.json", "w") as f:
            json.dump(prefixes, f, indent=4)

    # remove prefix and guild id from json file when bot leaves server
    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
        with open("prefixes.json", "r") as f:
            prefixes = json.load(f)

        prefixes.pop(str(guild.id))

        with open("prefixes.json", "w") as f:
            json.dump(prefixes, f, indent=4)


    # change prefix command
    @commands.command(aliases=["setprefix"], help="Command for changing the bot's prefix.")
    @has_permissions(administrator=True)
    async def changeprefix(self, ctx, prefix):
        if ctx.author == self.client.user:
            return
        if ctx.author.bot:
            return

        with open("prefixes.json", "r") as f:
            prefixes = json.load(f)

        prefixes[str(ctx.guild.id)] = prefix

        with open("prefixes.json", "w") as f:
            json.dump(prefixes, f, indent=4)

        embed = discord.Embed (
            title = "The bot's default prefix has been changed",
            color=0xc7ecf7
        )
        embed.add_field(
            name = "Default prefix",
            value = "!",
            inline=False
        )
        embed.add_field(
            name = "New prefix",
            value = f"{prefix}",
            inline=False
        )
        await ctx.send(embed=embed)
        await ctx.guild.me.edit(nick=f"[{prefix}] Endroid")

    @changeprefix.error
    async def changeprefix_error(self, ctx, error):
        if isinstance(error, MissingPermissions):
            await ctx.send("You do not have permission to use this command!")

        if isinstance(error, CommandError):
            embed = discord.Embed (
                title = "Command Error",
                description = "Could not complete your request! Pls type properly, idiot!",
                color = discord.Color.dark_red()
            )
            await ctx.send(embed=embed)
            print(f"{self.client.user} Error 404: Command Error")


    # server prefix command
    @commands.command(aliases=["currentprefix"], help="Command to fetch server prefix.")
    async def serverprefix(self, ctx):
        if ctx.author == self.client.user:
            return
        if ctx.author.bot:
            return

        with open("prefixes.json", "r") as f:
            prefixes = json.load(f)

        prefix = prefixes[str(ctx.guild.id)]

        await ctx.send(f"My server prefix is `{prefix}`")


    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.client.user:
            return
        if message.author.bot:
            return

        if message.content.lower().startswith("whats the prefix") or message.content.lower().startswith("what's the prefix") or message.content.lower().startswith("what is the prefix") or message.content.lower().startswith("whats the current prefix") or message.content.lower().startswith("what's the current prefix") or message.content.lower().startswith("what is the current prefix"):
            with open("prefixes.json", "r") as f:
                prefixes = json.load(f)

            prefix = prefixes[str(message.guild.id)]

            await message.channel.send(f"My current prefix is `{prefix}`")


def setup(client):
    client.add_cog(Prefix(client))

def teardown(client):
    client.remove_cog(Prefix(client))