import discord
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions
import datetime

import json
with open('reports.json', encoding='utf-8') as f:
  try:
    report = json.load(f)
  except ValueError:
    report = {}
    report['users'] = []


class Triggers(commands.Cog):
    def __init__(self, client):
        self.client = client


    # swear words
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.client.user:
            return
        if message.author.bot:
            return

        bad_list = [
            "dick",
            "cuck",
            "cock",
            "sex",
            "nigga",
            "nigger",
            "negro",
            "penis",
            "vagina",
            "nude",
            "porn",
            "pornhub.com",
            "brazzers.com",
            "faggot",
            "naked",
            "cum ",
            "motherfucker"
        ]
        for bad_word in bad_list:
            with open('reports.json', 'r') as f:
                swear_data = json.load(f)
            swear_data[str(message.author.id)]

            if bad_word in message.content.lower():

                # warning embed
                embed = discord.Embed (
                    title=f"**⚠ WARNING for {message.author.name}!**",
                    description="You have broken one of Da Rules in this server. If you receive too many warnings, you will be either **kicked or banned**.",
                    color=discord.Color.dark_orange()
                )
                embed.set_footer(text="If you think that this was a mistake, pls ping the Admin or Mods for further discussion")
                embed.timestamp = datetime.datetime.utcnow()
                await message.channel.send(embed=embed)
                await message.delete()
                print(f"{message.author} has been given a warning!")

            swear_data[str(message.author.id)]
            with open('reports.json', 'w') as f:
                json.dump(swear_data, f)

    
    # trigger words
    @commands.command()
    async def triggers(self, ctx):
        if ctx.author == self.client.user:
            return
        if ctx.author.bot:
            return
 
        embed = discord.Embed (
            title = "Endroid will delete these censored words:",
            description="||`Dick`\n`Cuck(s)`\n`Cock(s)`\n`Sex`\n`Nigga`\n`Nigger`\n`Negro`\n`Penis`\n`Vagina`\n`Nude`\n`Pronhub.com`\n`Brazzers.com`\n`Faggot`\n`Naked`\n`Cum`\n`Motherfucker`||",
            color=discord.Color.dark_red()
        )
        embed.set_footer(text="You will be given a warning that will trigger Endroid's auto-moderation")
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Triggers(client))