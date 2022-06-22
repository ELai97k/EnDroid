import discord
from discord.ext import commands
import pytz
from datetime import datetime

class Time(commands.Cog):
    def __init__(self, client):
        self.client = client

    # GMT timezone
    @commands.command()
    async def time_gmt(self, ctx):
        if ctx.author == self.client.user:
            return
        
        timestamp = datetime.now()
        gmt = pytz.timezone('Asia/Singapore')
        gmt_embed = discord.Embed (
            title = "Current date and time in GMT +08:00",
            color=0xc7ecf7
        )
        gmt_embed.add_field(name="Date", value=timestamp.astimezone(gmt).strftime("%a %d %b %Y"), inline=False)
        gmt_embed.add_field(name="Time", value=timestamp.astimezone(gmt).strftime("%I:%M %p"), inline=False)
        await ctx.send(embed=gmt_embed)


def setup(client):
    client.add_cog(Time(client))