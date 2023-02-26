import discord
import os
import json
import sqlite3
from discord.ext import commands
from discord.ext.commands import CommandNotFound

intents = discord.Intents.default().all()
intents.members=True

# setting up prefixes.json in json file
def get_prefix(client, message):
    with open("prefixes.json", "r") as f:
        prefixes = json.load(f)
    return prefixes[str(message.guild.id)]

# custom help command
class CustomHelpCommand(commands.HelpCommand):
    # cogs and commands
    async def send_bot_help(self, mapping):
        embed = discord.Embed(title=f"{client.user.name}'s Cogs & Commands", color=0xc7ecf7)
        description = self.context.bot.description
        if description:
            embed.description = description

        for cog, commands in mapping.items():
            if cog is not None:
                name = cog.qualified_name
                filtered = await self.filter_commands(commands, sort=True)

                if filtered:
                    value = '\u2002 '.join('`' + c.name + '`' for c in commands if not c.hidden)

                    if cog and cog.description:
                        value = '{0}\n{1}'.format(cog.description, value)

                    embed.add_field(name=name, value=value, inline=True)
                    embed.set_footer(text="Use [prefix]help [cog] or [prefix]help [command] for more info.")

        await self.get_destination().send(embed=embed)

    # cog info
    async def send_cog_help(self, cog):
        embed = discord.Embed (
            title = f"{cog.qualified_name} Commands",
            description = f"{cog.description}\n```{[command.name for command in cog.get_commands()]}```",
            color=0xc7ecf7
        )
        embed.set_footer(text="Use [prefix]help [command] for more info on a command.")
        await self.get_destination().send(embed=embed)

    # command info
    async def send_command_help(self, command):
        embed = discord.Embed (
            color=0xc7ecf7
        )
        embed.add_field (
            name=f"{command.name}",
            value=command.help,
            inline=False
        )
        await self.get_destination().send(embed=embed)

client = commands.Bot(command_prefix=get_prefix, 
help_command=CustomHelpCommand(), 
case_insensitive=True, 
intents=intents)

# cogs
for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        client.load_extension(f'cogs.{filename [:-3]}')

# on ready event
@client.event
async def on_ready():
    # bot login
    print(f"{client.user} logged in successfully!")

    # bot default status
    await client.change_presence (
        activity = discord.Activity (
        type = discord.ActivityType.playing, name = "Visual Studio Code"
        )
    )

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        embed = discord.Embed (
            title = "Command Not Found!",
            description = "No such command found in my cogs! Use `!help` for list of commands.",
            color = discord.Color.dark_red()
        )
        await ctx.send(embed=embed)

    # sqlite3 db warnings
    db = sqlite3.connect('warnings.sqlite')
    cursor = db.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS warns (
            user_id INTERGER,
            user_name TEXT
            reason TEXT,
            guild_id INTERGER,
            guild_name TEXT
        )
        """
    )

client.run(os.getenv('TOKEN'))