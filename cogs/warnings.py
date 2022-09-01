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


class Warnings(commands.Cog):
    """Warnings for members and warn command"""
    def __init__(self, client):
        self.client = client

    # warn command
    @commands.command(pass_context = True)
    @commands.has_role("Moderators")
    @has_permissions(manage_roles=True, kick_members=True, ban_members=True)
    async def warn(self, ctx, user:discord.User, *reason:str):
        if ctx.author == self.client.user:
            return
        if ctx.author.bot:
            return

        if not reason:
            await ctx.send("Please provide a reason for warning.")
            return

        reason = ' '.join(reason)
        for current_user in report['users']:
            if current_user['name'] == user.name:
                current_user['reasons'].append(reason)
                break
        else:
            report['users'].append({
                'name': user.name,
                'reasons': [reason, ]
            })
        with open('reports.json','w+') as f:
            json.dump(report,f)
        
        # embed
        embed = discord.Embed (
            title=f"**⚠ WARNING for {user.name}!**",
            description="You have broken one of Da Rules and your warning has been added to the user database. If you accumulate too many warnings, you will be either **kicked or banned**.",
            color=discord.Color.dark_red()
        )
        embed.set_footer(text="If you think that this was a mistake, pls DM or ping the Admin or Mods for further discussion")
        embed.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=embed)
        print(f"{user.name} has been given a warning!")

    @warn.error
    async def warn_error(self, ctx, error):
        if isinstance(error, MissingPermissions):
            await ctx.send("You do not have permission to use this command!")


    # warnings command
    @commands.command(pass_context = True)
    @commands.has_role("Moderators")
    async def warnings(self, ctx, user:discord.User):
        if ctx.author == self.client.user:
            return
        if ctx.author.bot:
            return

        for current_user in report['users']:
            if user.name == current_user['name']:

                # embed
                embed = discord.Embed (
                    title = f"Warning Report for {user.name}",
                    description = f"{user.name} has been reported {len(current_user['reasons'])} times.",
                    color=discord.Color.dark_red()
                )
                embed.add_field (
                    name = "Reasons",
                    value = f"{','.join(current_user['reasons'])}"
                )
                await ctx.send(embed=embed)
                break
        else:
            await ctx.trigger_typing()
            await ctx.send(f"{user.name} has never been reported.")

# NOTE to self
# pls relaod this cog everytime a user gets a warning
# or when editing the reports.json file

def setup(client):
    client.add_cog(Warnings(client))