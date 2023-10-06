import discord
import asyncio
from discord.ext import commands
from discord.ext.commands import CommandError

class Reminder(commands.Cog):
    """Get the bot to set reminders and be pinged when it's due."""
    def __init__(self, client):
        self.client = client

    # remind / reminder command
    @commands.command(help="Reminder command (input time first then reminder text)", aliases = ["reminder", "remindme"])
    async def remind(self, ctx, time, *, reminder):
        if ctx.author == self.client.user:
            return
        if ctx.author.bot:
            return

        user = ctx.author

        seconds = 0

        if time.lower().endswith("d"):
            seconds += int(time[:-1]) * 60 * 60 * 24
            counter = f"{seconds // 60 // 60 // 24} days"

        if time.lower().endswith("h"):
            seconds += int(time[:-1]) * 60 * 60
            counter = f"{seconds // 60 // 60} hours"

        elif time.lower().endswith("m"):
            seconds += int(time[:-1]) * 60
            counter = f"{seconds // 60} minutes"

        elif time.lower().endswith("s"):
            seconds += int(time[:-1])
            counter = f"{seconds} seconds"

        if seconds == 0:
            embed = discord.Embed (
                title = "Cannot process reminder",
                description = "Please input duration of time first followed by a reminder text.",
                color=0xc7ecf7
            )
            embed.add_field(name="Days", value="`d`")
            embed.add_field(name="Hours", value="`h`")
            embed.add_field(name="Minutes", value="`m`")
            embed.add_field(name="Minimum duration", value="```1 minute```")
            embed.add_field(name="Maximum duration", value="```104 days```")

        elif seconds < 60:
            embed = discord.Embed(color=0xc7ecf7)
            embed.add_field(name="Warning", value="You have specified a duration that is too short!\n```Minimum duration is 1 minute.```")

        elif seconds > 8985600:
            embed = discord.Embed(color=0xc7ecf7)
            embed.add_field(name="Warning", value="You have specified a duration that is too long!\n```Maximum duration is 104 days.```")

        else:
            await ctx.send(f"Alright {user.mention}, I will remind you about `{reminder}` in `{counter}`.")
            print(f"{user} {reminder} {counter}")
            await asyncio.sleep(seconds)
            await ctx.send(f"Hi {user.mention}, you asked me to remind you about `{reminder} {counter}` ago.")
            print(user, reminder, counter)
            return
        await ctx.send(embed=embed)
        print(f"Unable to process reminder for {user}")

    @remind.error
    async def remind_error(self, ctx, error):
        user = ctx.author
        if isinstance(error, CommandError):
            embed = discord.Embed (
                title = "Command Error",
                description = "Pls enter a proper time and reminder!\n```I'm unable to process your input!```",
                color = discord.Color.dark_red()
            )
            await ctx.send(embed=embed)
            print(f"{self.client.user} Error 404: Command Error")
            print(f"Unable to process reminder for {user}")


async def setup(client):
    await client.add_cog(Reminder(client))

async def teardown(client):
    await client.remove_cog(Reminder(client))