import discord
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions
import datetime

import json
with open('warns.json', encoding='utf-8') as f:
  try:
    warns = json.load(f)
  except ValueError:
    warns = {}
    warns['users'] = []
    
async def update_data(users, user):
    if not f'{user.name}' in users:
        users[f'{user.name}'] = {}
        users[f'{user.name}']['warns'] = 0

async def add_warns(users, user, warns):
    users[f'{user.name}']['warns'] += warns


class Warnings(commands.Cog):
    """Warnings for members and warn command"""
    def __init__(self, client):
        self.client = client

    @commands.command(pass_context=True)
    @commands.has_role("Moderators")
    @has_permissions(manage_roles=True, kick_members=True, ban_members=True)
    async def warn(self, ctx, user: discord.Member):
        if ctx.author == self.client.user:
            return
        if ctx.author.bot:
            return

        with open('warns.json', 'r') as f:
            users = json.load(f)
        
        await update_data(users, user)
        await add_warns(users, user, 1)

        with open('warns.json', 'w') as f:
            json.dump(users, f, sort_keys=True, ensure_ascii=False, indent=4)

        embed = discord.Embed (
            title = f"**⚠ WARNING for {user.name}!**",
            description = "You have broken one of Da Rules and your warning has been added to the user database. If you receive too many warnings, you will be either **kicked or banned**.",
            color = discord.Color.dark_red()
        )
        embed.set_footer(text="If you think this was a mistake, ping Admin or Mods for further discussion.")
        embed.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=embed)
        print(f"{user.name} has been given a warning!")


    @commands.command(pass_context=True)
    @commands.has_role("Moderators")
    @has_permissions(manage_roles=True)
    async def remove_warn(self, ctx, user: discord.Member, amount: int=None):
        if ctx.author == self.client.user:
            return
        if ctx.author.bot:
            return

        with open('warns.json', 'r') as f:
            users = json.load(f)

        amount = amount or 1

        await update_data(users, user)
        await add_warns(users, user, -amount)

        if users[f'{user.name}']['warns'] <= 0:
            with open('warns.json', 'w') as f:
                del users[f'{user.name}']['warns']
                del users[f'{user.name}']
                f.write(json.dumps(users, indent=4))
            return

        else:
            with open('warns.json', 'w') as f:
                json.dump(users, f, sort_keys=True, ensure_ascii=False, indent=4)
            await ctx.send(f'Removed {amount} warnings for {user.name}.')
            return


    @commands.command(pass_context=True)
    @commands.has_role("Moderators")
    @has_permissions(manage_roles=True)
    async def warnings(self, ctx, user: discord.Member=None):
        user = user or ctx.author
        if ctx.author == self.client.user:
            return
        if ctx.author.bot:
            return

        try:
            with open('warns.json', 'r') as f:
                users = json.load(f)

            warns = users[f'{user.name}']['warns']

            await ctx.send(f'{user.name} has {warns} warnings.')
        
        except:
            await ctx.send(f"{user.name} doesn't have any warnings.")


def setup(client):
    client.add_cog(Warnings(client))