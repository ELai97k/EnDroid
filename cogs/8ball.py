import random
from discord.ext import commands

class EightBall(commands.Cog):
    """8ball function."""
    def __init__(self, client):
        self.client = client

    # 8ball command (prefix + ask)
    @commands.command(help="Ask the bot anything with the 8ball function.")
    async def ask(self, ctx, *, message=None):
        if ctx.author == self.client.user:
            return
        if ctx.author.bot:
            return

        eight_ball = [
            "Yes.",
            "No.",
            "Maybe.",
            "I don't know.",
            "You may rely on it.",
            "Cannot tell you now.",
            "Cannot predict now.",
            "Better not tell you now.",
            "Outlook good.",
            "Outlook not so good.",
            "It is decidedly so.",
            "Most likely.",
            "Very unlikely.",
            "My reply is no.",
            "My reply is yes.",
            "Very doubtful.",
            "Don't count on it!",
            "Can't say for sure.",
            "My sources say no.",
            "My sources say yes.",
            "Without a doubt.",
            "Ask again later.",
            "Try again later.",
            "Reply hazy, try again later.",
            "As I see it, yes."
        ]
        
        if message is None:
            await ctx.channel.typing()
            await ctx.send("Pls ask me a yes-or-no question first.")

        else:
            await ctx.channel.typing()
            await ctx.send(f'{random.choice(eight_ball)}')


async def setup(client):
    await client.add_cog(EightBall(client))

async def teardown(client):
    await client.remove_cog(EightBall(client))