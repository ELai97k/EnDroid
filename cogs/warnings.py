from itertools import count
import discord
import json
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions

with open('warns.json', encoding='utf-8') as f:
    try:
        report = json.load(f)
    except ValueError:
        report = {}
        report['users'] = []


class Warnings(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(pass_context=True)
    @commands.has_role("Moderators")
    @commands.has_permissions(manage_roles=True, kick_members=True, ban_members=True)
    async def warn(self, ctx, user:discord.User=None, *, reason=None):
        if ctx.author == self.client.user:
            return
        if ctx.author.bot:
            return
        
        if user is None:
            await ctx.send("Pls specify a user that needs to be warned.")
        if reason is None:
            await ctx.send("Pls provide a reason for warning.")

        try:
            report[ctx.guild.id][user.name][0] += 1
            report[ctx.guild.id][user.name][1].append((ctx.author, reason))
        except ValueError:
            report[ctx.guild.id][user.name] = [1, [(ctx.author, reason)]]
        
        warn_count = report[ctx.guild.id][user.name][0]

        # embed
        embed = discord.Embed (
            title = f"WARNING {warn_count} for {user.name}!",
            description = "You have broken one of the rules of this server. If you receive too many warnings, you will be **kicked or banned.**",
            color = discord.Color.dark_red()
        )
        embed.set_footer(text="If you think this was a mistake, ping Admin or Mods for further discussion.")
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Warnings(client))