import discord
from discord.ext import commands
import asyncio

class Remind(commands.Cog):
    """Reminder command"""
    def __init__(self, client):
        self.client = client

    # reminder command
    @commands.command(pass_context=True)
    async def remind(self, ctx, *times, reminder=None):
        user = ctx.author
        if user == self.client.user:
            return

        for time in times:
            seconds = 0
            # minutes
            if time.lower().endswith("m"):
                seconds += int(time[:-1]) * 60
                counter = f"{seconds // 60} minutes"

            # hours
            if time.lower().endswith("h"):
                seconds += int(time[:-1]) * 60 * 60
                counter = f"{seconds // 60 // 60} hours"

            # days
            if time.lower().endswith("d"):
                seconds += int(time[:-1]) * 60 * 60 * 24
                counter = f"{seconds // 60 // 60 // 24} days"

            command_prefix = "?/"
            r_command = "remind"
            reminder = ctx.message.content.lower().replace(f"{command_prefix}", "").replace(f"{r_command}", "").replace(f"{time}", "").strip()
            
            if reminder is None:
                await ctx.send("Please tell me what to remind you.")
            if seconds == 0 or seconds > 2592000:
                await ctx.send("Please specify a proper time:\n`m` for minutes\n`h` for hours\n`d` for days")
            else:
                await ctx.send(f"Okay {user.mention}, I will remind you about `{reminder}` in `{counter}`.")
                await asyncio.sleep(seconds)
                await ctx.send(f"Hey {user.mention}, you asked me to remind you about `{reminder}` `{counter}` ago.")
                return


def setup(client):
    client.add_cog(Remind(client))