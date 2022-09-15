import discord
import asyncio
from discord.ext import commands

class Shut(commands.Cog):
    def __init__(self, client):
        self.client = client

    # shut bot
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.client.user:
            return
        if message.author.bot:
            return

        if "shut up bot" in message.content.lower() or "shut up daydreamer" in message.content.lower() or "daydreamer shut up" in message.content.lower() or "bot shut up" in message.content.lower():
            await message.channel.send("Okay :(")
            self.client.unload_extension("cogs.auto_responses")
            print("Auto Responses has been turned off")
            await asyncio.sleep(999)
            self.client.load_extension("cogs.auto_responses")
            print("Auto Responses has been turned on")


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
        self.client.unload_extension("cogs.auto_responses")
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
        self.client.load_extension("cogs.auto_responses")
        print("Auto responses has been turned on")


def setup(client):
    client.add_cog(Shut(client))