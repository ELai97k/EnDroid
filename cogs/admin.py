import discord
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions

class Admin(commands.Cog):
    """Kick and ban commands for admin and mods."""
    def __init__(self, client):
        self.client = client

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
            await member.kick(reason=reason)
            await ctx.send(embed=embed)
            print(f"{member.name} has been kicked from the server.")
            print(f"Reason: {reason}")

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
            await member.ban(reason=reason)
            await ctx.send(embed=embed)
            print(f"{member.name} has been banned from the server.")
            print(f"Reason: {reason}")

    @ban.error
    async def ban_error(self, ctx, error):
        if isinstance(error, MissingPermissions):
            await ctx.send("You do not have permission to use this command!")


def setup(client):
    client.add_cog(Admin(client))