import discord
import json
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions

class Warnings(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(pass_context=True)
    @commands.has_role("Moderators")
    @commands.has_permissions(manage_roles=True, kick_members=True, ban_members=True)
    async def warn(self, ctx, user:discord.User, *reason:str):
        with open('warns.json', encoding='utf-8') as f:
            try:
                report = json.load(f)
            except ValueError:
                report = {}
                report['users'] = []

        if ctx.author == self.client.user:
            return
        if ctx.author.bot:
            return
        
        if not reason:
            await ctx.send("Pls provide a reason for warning.")
            return
        
        embed = discord.Embed (
            title = f"WARNING for {user.name}",
            description = "You have broken one of the rules of this server. If you receive too many warnings, you will be **kicked or banned**.",
            color = discord.Color.dark_red()
        )
        embed.set_footer(text="If you think this was a mistake, pls ping the Admin or Mods for further discussion.")

        for current_user in report['users']:
            if current_user['name'] == user.name:
                current_user['reasons'].append(reason)
                break
            else:
                report['users'].append({
                    'name': user.name,
                    'reasons': [reason, ]
                })
        
        with open('warns.json', 'w+') as f:
            json.dump(report, f)
        await ctx.send(embed=embed)
        print(f"{user.name} has been given a warning!")


def setup(client):
    client.add_cog(Warnings(client))