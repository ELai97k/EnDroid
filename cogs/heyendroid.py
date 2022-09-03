import discord
from discord.ext import commands

class HeyPrompts(commands.Cog):
    """'hey endroid' prompts and responses"""
    def __init__(self, client):
        self.client = client

    # embed
    @commands.command()
    async def heyprompts(self, ctx):
        if ctx.author == self.client.user:
            return
        if ctx.author.bot:
            return

        embed = discord.Embed (
            title = "List of available options when typing 'hey endroid'",
            color=0xc7ecf7
        )
        # how are you
        embed.add_field(name="Ask how is Endroid", 
        value="**Prompts:** 'how are you', 'how are you doing'",
        inline=False)

        # features
        embed.add_field(name="Ask about Endroid's functions / features", 
        value="**Prompts:** 'what can you do', 'what are your features', 'what are your functions'",
        inline=False)

        # tell me about yourself
        embed.add_field(name="Ask Endroid to introduce himself", 
        value="**Prompts:** 'tell me about yourself', 'who are you', 'what are you'",
        inline=False)

        # what are you doing right now
        embed.add_field(name="Ask Endroid what he's doing", 
        value="**Prompts:** 'what are you doing right now', 'what are you doing now', 'what are you doing', 'what you doing', 'whatcha doin', 'whatcha doing', 'what'cha doin', 'what'cha doing', 'what are you doing currently', 'what are you currently doing'",
        inline=False)

        # talk to me
        embed.add_field(name="Make Endroid talk to you", 
        value="**Prompts:** 'talk to me', 'talk to me pls', 'pls talk to me', 'can you talk to me', 'can you pls talk to me', 'can ypu talk to me pls'",
        inline=False)
        
        # time
        embed.add_field(name="Ask Endroid about the time. (In GMT+8)",
        value="**Prompts:** 'whats the time', 'whats the time now', 'what's the time', 'what's the time now', 'what is the time', 'what is the time now', 'what time is it'",
        inline=False)

        # Isaac Asimov Robot Laws
        embed.add_field(name="Ask Endroid about the Laws of Robotics",
        value="**Prompts:** 'tell me about robot laws', 'tell me about the robot laws', 'what are the robot laws', 'what are the laws of robotics', ''",
        inline=False)

        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(HeyPrompts(client))