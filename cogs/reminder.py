import discord
from discord.ext import commands
import asyncio

class Remind(commands.Cog):
    """Reminder command (input message first, then the time)"""
    def __init__(self, client):
        self.client = client

    # remind / reminder command
    @commands.command(pass_context=True, aliases=["reminder"])
    async def remind(self, ctx, reminder=None, *times):
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

            command_prefix = "?"
            r_command = "remind"
            reminder = ctx.message.content.lower().replace(f"{command_prefix}", "").replace(f"{r_command}", "").replace(f"{time}", "").strip()
            
            if reminder is None:
                await ctx.send("Please tell me what to remind you.")
            if seconds == 0 or seconds > 2592000:
                await ctx.send("Please input a reminder before you input the time in:\n`m` (minutes)\n`h` (hours)\n`d` (days).")
            else:
                await ctx.send(f"Okay {user.mention}, I will remind you about `{reminder}` in `{counter}`.")
                await asyncio.sleep(seconds)
                await ctx.send(f"Hey {user.mention}, you asked me to remind you about `{reminder}` `{counter}` ago.")
                return
    
    # remind me command
    @commands.command(pass_context=True)
    async def remindme(self, ctx, *times, reminder=None):
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

            command_prefix = "?"
            r_command = "remind"
            reminder = ctx.message.content.lower().replace(f"{command_prefix}", "").replace(f"{r_command}", "").replace(f"{time}", "").strip()
            
            if reminder is None:
                await ctx.send("Please tell me what to remind you.")
            if seconds == 0 or seconds > 2592000:
                await ctx.send("Please input the time in:\n`m` (minutes)\n`h` (hours)\nor `d` (days), then input your reminder.")
            else:
                await ctx.send(f"Okay {user.mention}, I will remind you about `{reminder}` in `{counter}`.")
                await asyncio.sleep(seconds)
                await ctx.send(f"Hey {user.mention}, you asked me to remind you about `{reminder}` `{counter}` ago.")
                return


def setup(client):
    client.add_cog(Remind(client))