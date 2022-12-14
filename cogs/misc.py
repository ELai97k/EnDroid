import discord
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

        await ctx.send("This is a test command.")
        print("This is a test command and it works.")


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
        if ctx.authot == self.client.user:
            return
        if ctx.author.bot:
            return
        
        await ctx.send("Here's my GitHub page:\nhttps://github.com/ELai97k/EnDroid")


    # user profile pics
    @commands.command(pass_context=True, aliases=["profile", "userprofile", "userpfp"], help="Command to show user's profile picture (pfp)")
    async def pfp(self, ctx, *, user:discord.Member=None):
        if ctx.author == self.client.user:
            return
        if ctx.author.bot:
            return

        if user is None:
            user = ctx.author

        embed = discord.Embed(color=discord.Color.blurple())
        embed.set_image(url=user.avatar_url)
        await ctx.send(embed=embed)


    # welcome embed
    @commands.Cog.listener()
    async def on_member_join(self, member):
        if member.guild.id == 762317365970468874:
            embed = discord.Embed (
                title=f'Hello {member.name}, and welcome to **{member.guild.name}**!',
                description='Have a look at the rules at <#855777347730407434> and server info at <#855775497955180545>.',
                color=0x198C19
            )
            embed.set_footer(text='Thank you for joining us! We hope you enjoy your stay.')
            await self.client.get_channel(762317365970468877).send(embed=embed)

    # goodbye embed
    @commands.Cog.listener()
    async def on_member_remove(self, member):
        if member.guild.id == 762317365970468874:
            embed = discord.Embed (
                title=f'{member} has left the server!',
                description="Sorry to see you go.",
                color=0x1e377f
            )
        await self.client.get_channel(762317365970468877).send(embed=embed)


def setup(client):
    client.add_cog(Misc(client))

def teardown(client):
    client.remove_cog(Misc(client))