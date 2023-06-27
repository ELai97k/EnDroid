import discord
from discord.ext import commands

class Poll(commands.Cog):
    """Poll function."""
    def __init__(self, client):
        self.client = client

    # poll help
    @commands.command(help="Command for poll help.")
    async def pollhelp(self, ctx):
        if ctx.author == self.client.user:
            return
        if ctx.author.bot:
            return
        
        embed = discord.Embed(
            color = discord.Color.orange(),
            title = "How to use the poll command:",
            description="```!poll title one two three four etc```\nTo input sentences or phrases in the title and/or items, use quotation marks."
        )
        await ctx.send(embed=embed)


    # poll command
    @commands.command(pass_context=True, help="Command to create polls.")
    async def poll(self, ctx, question, *options: str):
        if ctx.author == self.client.user:
            return
        if ctx.author.bot:
            return

        if len(options) <= 1:
            await ctx.send('You need at least more than one option to make a poll!')
            return
        if len(options) > 10:
            await ctx.send('You cannot make a poll for more than 10 things!')
            return

        if len(options) == 2 and options[0] == 'yes' and options[1] == 'no':
            reactions = ['✅', '❌']
        else:
            reactions = ['1⃣', '2⃣', '3⃣', '4⃣', '5⃣', '6⃣', '7⃣', '8⃣', '9⃣', '🔟']

        description = []
        for x, option in enumerate(options):
            description += '\n{} {}'.format(reactions[x], option)
        embed = discord.Embed (
            title = question,
            description = "".join(description),
            color=discord.Color.orange()
        )
        react_message = await ctx.send(embed=embed)
        for reaction in reactions[:len(options)]:
            await react_message.add_reaction(reaction)


async def setup(client):
    await client.add_cog(Poll(client))

async def teardown(client):
    await client.remove_cog(Poll(client))