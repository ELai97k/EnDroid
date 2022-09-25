import discord
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions
from datetime import datetime

import json
with open('reports.json', encoding='utf-8') as f:
  try:
    report = json.load(f)
  except ValueError:
    report = {}
    report['users'] = []


class Admin(commands.Cog):
    """Kick and ban commands for admin and mods."""
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
            json.dump(report, f)
        
        # embed
        embed = discord.Embed (
            title=f"**⚠ WARNING for {user.name}!**",
            description="You have broken one of Da Rules and your warning has been recorded. If you receive too many warnings, you will be either **kicked or banned**.",
            color=discord.Color.dark_red()
        )
        embed.set_footer(text="If you think this was a mistake, DM or ping Admin or Mods for further discussion.")
        embed.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=embed)
        print(f"{user.name} has been given a warning!")


    # kick command
    @commands.command(pass_context=True, help="Kick a member out of the server.")
    @commands.has_role("Moderators")
    @has_permissions(manage_roles=True, kick_members=True)
    async def kick(self, ctx, member:discord.Member, *, reason=None):
        if member.guild_permissions.manage_roles:
            embed = discord.Embed (
                title = "Command Error!",
                description = "Admin or Moderators cannot be kicked!",
                color = discord.Color.dark_red()
            )
            await ctx.send(embed=embed)

        else:
            embed = discord.Embed (
                title = "Operation Successful!",
                description = f"{member.name} has been kicked from this server.",
                color=0x198C19
            )
            embed.add_field (
                name = "Reason:",
                value = f"{reason}",
                inline=False
            )
            await member.kick(reason=reason)
            await ctx.send(embed=embed)
            print(f"{member.name} has been kicked from the server.")

    @kick.error
    async def kick_error(self, ctx, error):
        if isinstance(error, MissingPermissions):
            await ctx.send("You do not have permission to use this command!")


    # ban command
    @commands.command(pass_context=True, help="Ban a member from the server.")
    @commands.has_role("Moderators")
    @has_permissions(manage_roles=True, ban_members=True)
    async def ban(self, ctx, member:discord.Member, *, reason=None):
        if member.guild_permissions.manage_roles:
            embed = discord.Embed (
                title = "Command Error!",
                description = "Admin or Moderators cannot be banned!",
                color = discord.Color.dark_red()
            )
            await ctx.send(embed=embed)

        else:
            embed = discord.Embed (
                title = "Operation Successful!",
                description = f"{member.name} has been banned from this server.",
                color=0x198C19
            )
            embed.add_field (
                name = "Reason:",
                value = f"{reason}",
                inline=False
            )
            await member.ban(reason=reason)
            await ctx.send(embed=embed)
            print(f"{member.name} has been banned from the server.")

    @ban.error
    async def ban_error(self, ctx, error):
        if isinstance(error, MissingPermissions):
            await ctx.send("You do not have permission to use this command!")


def setup(client):
    client.add_cog(Admin(client))