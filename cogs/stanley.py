import discord
from discord.ext import commands
import asyncio

class Stanley(commands.Cog):
    def __init__(self, client):
        self.client = client

    # eight command
    @commands.command()
    async def eight(self, ctx):
        if ctx.author == self.client.user:
            return

        embed = discord.Embed (
            title = "8888",
            description = "8888888888888888888888888888",
            color=0xfe3088
        )
        embed.add_field(name="Eight", value="<:eight_8:976069765506424932>")
        embed.set_footer(text="EIGHT")
        await ctx.send(embed=embed)
        print("eight")

    # Stanley command
    @commands.command()
    async def stanley(self, ctx):
        if ctx.author == self.client.user:
            return

        embed = discord.Embed (
            title = "The Stanley Parable",
            description = "This is the story of a man named Stanley. Stanley worked for a company in a big building where he was Employee Number 427. Employee Number 427's job was simple, he sat at his desk in Room 427 and he pushed buttons on a keyboard. Orders came to him through a monitor on his desk, telling him what buttons to push, how long to push them, and in what order. This is what Employee 427 did every day, of every month, of every year. And although others might have considered it soul-rending, Stanley relished every moment that the orders came in, as though he had been made exactly for this job. And Stanley was happy.",
            color=0xe4d21d
        )
        embed.set_footer(text = "Original Story by The Narrator")
        await ctx.send(embed=embed)
        print("The Stanley Parable")


    # Employee 427 command
    @commands.command()
    async def employee427(self, ctx):
        if ctx.author == self.client.user:
            return

        embed = discord.Embed (
            title = "The Stanley Parable",
            description = "This is the story of a man named Stanley. Stanley worked for a company in a big building where he was Employee Number 427. Employee Number 427's job was simple, he sat at his desk in Room 427 and he pushed buttons on a keyboard. Orders came to him through a monitor on his desk, telling him what buttons to push, how long to push them, and in what order. This is what Employee 427 did every day, of every month, of every year. And although others might have considered it soul-rending, Stanley relished every moment that the orders came in, as though he had been made exactly for this job. And Stanley was happy.",
            color=0xe4d21d
        )
        embed.set_footer(text = "Original Story by The Narrator")
        await ctx.send(embed=embed)
        print("The Stanley Parable")

    # change bot status
    @commands.command()
    async def stanley_status(self, ctx):
        if ctx.author == self.client.user:
            return

        embed = discord.Embed (
            title = "Operation Successful!",
            description = "Bot status has been updated successfully and your changes were saved!",
            color=0x198C19
        )
        await ctx.send(embed=embed)
        print("Bot status changed successfully!")

        await self.client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="The Stanley Parable Demonstration"))
        await asyncio.sleep(999)
        await self.client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="The Stanley Parable"))
        await asyncio.sleep(999)
        await self.client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="The Stanley Parable Ultra Deluxe"))
        await asyncio.sleep(999)
        await self.client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="The Stanley Parable 2"))
        await asyncio.sleep(999)
        await self.client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="The Stanley Parable 3: Offline Tuesday"))
        await asyncio.sleep(999)
        await self.client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="The Stanley Parable Demonstration"))
        await asyncio.sleep(999)
        await self.client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="The Stanley Parable"))
        await asyncio.sleep(999)
        await self.client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="The Stanley Parable Ultra Deluxe"))
        await asyncio.sleep(999)
        await self.client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="The Stanley Parable 2"))
        await asyncio.sleep(999)
        await self.client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="The Stanley Parable 3: Offline Tuesday"))
        await asyncio.sleep(999)
        await self.client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="The Stanley Parable Demonstration"))
        await asyncio.sleep(999)
        await self.client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="The Stanley Parable"))
        await asyncio.sleep(999)
        await self.client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="The Stanley Parable Ultra Deluxe"))
        await asyncio.sleep(999)
        await self.client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="The Stanley Parable 2"))
        await asyncio.sleep(999)
        await self.client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="The Stanley Parable 3: Offline Tuesday"))


def setup(client):
    client.add_cog(Stanley(client))