import discord
from discord.ext import commands
import random

class EightBall(commands.Cog):
    """8ball command"""
    def __init__(self, client):
        self.client = client

    # 8ball command (prefix + ask)
    @commands.command()
    async def ask(self, ctx):
        if ctx.author == self.client.user:
            return
        
        eight_ball = [
            "Yes",
            "No",
            "Maybe",
            "You may rely on it",
            "Cannot tell you now",
            "Cannot predict now.",
            "Better not tell you now",
            "Outlook good.",
            "Outlook not so good.",
            "It is decidedly so.",
            "Most likely.",
            "Most unlikely",
            "My reply is no.",
            "My reply is yes.",
            "Very doubtful.",
            "Don't count on it!",
            "Can't say for sure.",
            "My sources say no.",
            "My sources say yes.",
            "Without a doubt.",
            "Ask again later",
            "Try again later.",
            "Reply hazy, try again later."
        ]
        await ctx.channel.trigger_typing()
        await ctx.send(f'{random.choice(eight_ball)}')
        print("8ball brrr")


def setup(client):
    client.add_cog(EightBall(client))