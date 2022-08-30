import discord
from discord.ext import commands

class Stanley(commands.Cog):
    """Fun misc commands based on The Stanley Parable"""
    def __init__(self, client):
        self.client = client

    # eight command
    @commands.command()
    async def eight(self, ctx):
        if ctx.author == self.client.user:
            return
        if ctx.author.bot:
            return

        embed = discord.Embed (
            title = "8888888888888888",
            description = "8888888888888888888888888888",
            color=0xfe3088
        )
        embed.add_field(name="Eight", value="<:eight_8:976069765506424932>")
        embed.set_footer(text="EIGHT")
        await ctx.send(embed=embed)
        print("eight")


    # Stanley command
    @commands.command(aliases=["employee427", "stanleyparable"])
    async def stanley(self, ctx):
        if ctx.author == self.client.user:
            return
        if ctx.author.bot:
            return

        embed = discord.Embed (
            title = "The Stanley Parable",
            description = "This is the story of a man named Stanley. Stanley worked for a company in a big building where he was Employee Number 427. Employee Number 427's job was simple, he sat at his desk in Room 427 and he pushed buttons on a keyboard. Orders came to him through a monitor on his desk, telling him what buttons to push, how long to push them, and in what order. This is what Employee 427 did every day, of every month, of every year. And although others might have considered it soul-rending, Stanley relished every moment that the orders came in, as though he had been made exactly for this job. And Stanley was happy.",
            color=0xe4d21d
        )
        embed.set_footer(text = "Original Story by The Narrator\nWritten by Davey Wreden")
        await ctx.send(embed=embed)
        print("The Stanley Parable")


    # bucket command
    @commands.command()
    async def bucket(self, ctx):
        if ctx.author == self.client.user:
            return
        if ctx.author.bot:
            return
        await ctx.send(":bucket:")


def setup(client):
    client.add_cog(Stanley(client))