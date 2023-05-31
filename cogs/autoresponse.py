import discord
from discord.ext import commands

class Autoresponse(commands.Cog):
    """Cog for the bot's auto-responses."""
    def __init__(self, client):
        self.client = client

    # auto responses off
    @commands.command(pass_context=True, help="Turn off bot's auto-responses.")
    async def autoresponse_off(self, ctx):
        if ctx.author == self.client.user:
            return
        if ctx.author.bot:
            return

        embed = discord.Embed (
            title = "Operation Successful!",
            description = "`Auto-Responses` has been turned **OFF** and your changes were saved.",
            color=0x198C19
        )
        await ctx.send(embed=embed)
        await self.client.unload_extension("cogs.auto_responses")
        print("Auto responses has been turned off")


    # auto responses on
    @commands.command(pass_context=True, help="Turn on bot's auto-responses.")
    async def autoresponse_on(self, ctx):
        if ctx.author == self.client.user:
            return
        if ctx.author.bot:
            return

        embed = discord.Embed (
            title = "Operation Successful!",
            description = "`Auto-Responses` has been turned **ON** and your changes were saved.",
            color=0x198C19
        )
        await ctx.send(embed=embed)
        await self.client.load_extension("cogs.auto_responses")
        print("Auto responses has been turned on")


    # embed showing bot's auto responses
    @commands.command(help="Embed that shows what messages the bot will auto-respond to.")
    async def responses(self, ctx):
        if ctx.author == self.client.user:
            return
        if ctx.author.bot:
            return

        embed = discord.Embed (
            title = "Endroid will automatically respond to the following messages:",
            description = ":(\nI am\nI'm / im\nteleport bread\ndead chat\nwhy isn't this working\njmm\njumm\nhi / hello endroid\nhello / hi / hey bot(s)\nstupid bot\ntell me a joke\nsay something / tell me something\nI have no friends\ninput\nbruh\nF\nshut up bot / bot shut up\nshut up endroid / endroid shut up",
            color=0xc7ecf7
        )
        await ctx.send(embed=embed)


    # hey endroid prompts and responses
    @commands.command(help="Command embed to find out what you can input when you trigger 'hey endroid' in message.")
    async def heyprompts(self, ctx):
        if ctx.author == self.client.user:
            return
        if ctx.author.bot:
            return

        embed = discord.Embed (
            title = "List of available options when typing 'hey endroid'",
            color=0xc7ecf7
        )
        # you're / ur responses
        embed.add_field(name="hey endroid + you're / ur",
        value="```stupid, dumb, dum, a dumbass, useless, not helpful, not helping, a good bot, a clever bot, a cleverbot, a smart bot```",
        inline=False)

        await ctx.send(embed=embed)


async def setup(client):
    await client.add_cog(Autoresponse(client))

async def teardown(client):
    await client.remove_cog(Autoresponse(client))