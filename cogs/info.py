import discord
from discord.ext import commands

class Info(commands.Cog):
    """Alternate help command for the bot."""
    def __init__(self, client):
        self.client = client

    # alternate help command
    @commands.command(help="This is the bot's custom help embed.")
    async def info(self, ctx):
        if ctx.author == self.client.user:
            return
        if ctx.author.bot:
            return

        embed = discord.Embed (
            title = "Bot's List of Commands",
            color=0xc7ecf7
        )
        embed.add_field(name="info", 
        value="Custom help command that you're looking at right now.",
        inline=False)

        embed.add_field(name="help", 
        value="Displays the bot's default help command.",
        inline=False)

        embed.add_field(name="ask", 
        value="8ball command, ask the bot anything.",
        inline=False)

        embed.add_field(name="embed", 
        value="Displays a test embed.",
        inline=False)

        embed.add_field(name="ping", 
        value="This command will show the bot's latency in ms (milliseconds).",
        inline=False)

        embed.add_field(name="poll", 
        value="This command allows you to create and make polls so that everyone can vote.",
        inline=False)

        embed.add_field(name="test", 
        value="This command is a test command.",
        inline=False)

        embed.add_field(name="responses", 
        value="Displays a list of words / phrases / sentences the bot will auto respond to.",
        inline=False)

        embed.add_field(name="remind", 
        value="Get the bot to set a reminder for you and be pinged when it's due.",
        inline=False)

        embed.add_field(name="musichelp", 
        value="Displays list of music bot commands.",
        inline=False)

        embed.add_field(name="heyprompts",
        value="Command for displaying list of options when you type 'hey endroid'.",
        inline=False)

        embed.add_field(name="version / botversion / botver",
        value="Python version for the bot.",
        inline=False)

        embed.add_field(name="userinfo",
        value="Command to fetch user info.",
        inline=False)

        embed.set_footer(text="Bot functions listed here will be subject to future changes")

        await ctx.send(embed=embed)


async def setup(client):
    client.add_cog(Info(client))