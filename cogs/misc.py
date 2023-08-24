import discord
import pytz
from datetime import datetime
from discord.ext import commands

class Misc(commands.Cog):
    """Cog for basic and misc commands."""
    def __init__(self, client):
        self.client = client

    # test command
    @commands.command(help="This is a test command.")
    async def test(self, ctx):
        if ctx.author == self.client.user:
            return
        if ctx.author.bot:
            return

        await ctx.send("aaaaaaaaaaaaaaaaa")


    # ping command
    @commands.command(help="Command that shows the bot's latency.")
    async def ping(self, ctx):
        if ctx.author == self.client.user:
            return
        if ctx.author.bot:
            return

        await ctx.send(f"🏓pong! Latency is {round (self.client.latency * 1000)} ms.")


    # test embed
    @commands.command(help="Command for a test embed.")
    async def embed(self, ctx):
        if ctx.author == self.client.user:
            return
        if ctx.author.bot:
            return

        embed = discord.Embed (
            title = "Hello world",
            description = "This is a test embed",
            color=0xc7ecf7
        )
        await ctx.send(embed=embed)


    # github page
    @commands.command(help="Shows the bot's GitHub page.")
    async def github(self, ctx):
        if ctx.author == self.client.user:
            return
        if ctx.author.bot:
            return
        
        await ctx.send("Here's my GitHub page:\nhttps://github.com/ELai97k/EnDroid")


    # user profile pics
    @commands.command(pass_context=True, aliases=["profile", "userprofile", "userpfp", "avatar"], help="Command to show user's profile picture (pfp)")
    async def pfp(self, ctx, *, user:discord.Member=None):
        if ctx.author == self.client.user:
            return
        if ctx.author.bot:
            return

        if user is None:
            user = ctx.author

        embed = discord.Embed(color=discord.Color.blurple())
        try:
            embed.set_image(url=user.avatar.url)
        except:
            embed.set_image(url=str(user.display_avatar.url))
        await ctx.send(embed=embed)


    # GMT+8 timezone
    @commands.command(aliases=["gmt+8", "gmt_8"], help="Fetch timezone in Malaysia/Singapore (GMT +8)")
    async def gmt8(self, ctx):
        if ctx.author == self.client.user:
            return
        if ctx.author.bot:
            return

        timestamp = datetime.now()
        gmt8 = pytz.timezone('Asia/Singapore')
        embed = discord.Embed (
            title = "Current date and time in GMT+8",
            color=0xc7ecf7
        )
        embed.add_field(name="Date", value=timestamp.astimezone(gmt8).strftime("%a, %d %b, %Y"), inline=False)
        embed.add_field(name="Time", value=timestamp.astimezone(gmt8).strftime("%I:%M %p"), inline=False)
        await ctx.send(embed=embed)


    # laws of robotics
    @commands.command(aliases=["lawsofrobotics", "robotics", "isaacasimov", "isaac_asimov"], help="Isaac Asimov's Three Laws of Robotics")
    async def laws_robotics(self, ctx):
        if ctx.author == self.client.user:
            return
        if ctx.author.bot:
            return

        embed = discord.Embed (
            title="The Three Laws of Robotics",
            color=0xc7ecf7
        )
        # First Law
        embed.add_field(name="First Law", value="A robot may not injure a human being or, through inaction, allow a human being to come to harm.", inline=False)
        # Second Law
        embed.add_field(name="Second Law", value="A robot must obey the orders given it by human beings except where such orders would conflict with the **First Law**.", inline=False)
        # Third Law
        embed.add_field(name="Third Law", value="A robot must protect its own existence as long as such protection does not conflict with the **First** or **Second Law**.", inline=False)

        # embed footer
        embed.set_footer(text="The Three Laws of Robotics was created by Isaac Asimov in 1942.")
        await ctx.send(embed=embed)


    @commands.command(name="version", aliases=["ver"], help="Bot's discord.py version")
    async def _version(self, ctx):
        if ctx.author == self.client.user:
            return
        if ctx.author.bot:
            return
        
        await ctx.send(f"My discord.py version is {discord.__version__}")
        print(f"discord.py v{discord.__version__}")


async def setup(client):
    await client.add_cog(Misc(client))

async def teardown(client):
    await client.remove_cog(Misc(client))