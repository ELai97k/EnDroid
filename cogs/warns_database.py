import discord
import sqlite3
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions, CommandError

class Warns_Database(commands.Cog):
    """Cog for warning system."""
    def __init__(self, client):
        self.client = client

    @commands.command(help="Give a warning to a member.")
    @commands.has_role("Moderators")
    @has_permissions(manage_roles=True, kick_members=True, ban_members=True)
    async def warn(self, ctx, user:discord.Member, *, reason:str):
        if ctx.author == self.client.user:
            return
        if ctx.author.bot:
            return

        async def addwarn(ctx, reason, user):
            db = sqlite3.connect('warnings.sqlite')
            cursor = db.cursor()
            cursor.execute(
                """
                INSERT INTO warns (
                    user_id,
                    user_name,
                    reason,
                    guild_id,
                    guild_name
                )
                VALUES (?, ?, ?, ?, ?)
                """, (user.id, user.name, reason, ctx.guild.id, ctx.guild.name)
            )
            db.commit()
        await addwarn(ctx, reason, user)

        # embed
        embed = discord.Embed (
            title=f"**⚠ WARNING for {user}**",
            description=f"This user `{user}` has been given a warning! It has been recorded and added to their userdata successfully.",
            color=discord.Color.dark_red()
        )
        await ctx.send(embed=embed)
        print(f"{user} has been given a warning!")

        db = sqlite3.connect('warnings.sqlite')
        cursor = db.cursor()
        cursor.execute("SELECT * FROM warns WHERE user_id = ? AND guild_id = ?", (user.id, ctx.guild.id))
        data = cursor.fetchall()
        if len(data) >= 3:
            await user.kick(reason=f"`{user}` has reached 3 warnings.")
            await ctx.send(f"`{user}` has reached 3 warnings and is promptly kicked from this server.")
            print(f"{user} has reached 3 warnings and is kicked from this server.")

        if len(data) == 4:
            await user.ban(reason=f"`{user}` has reached 4 warnings.")
            await ctx.send(f"`{user}` has reached 4 warnings and is banned from this server, goodbye.")
            print(f"{user} has reached 4 warnings and is banned from this server.")

    # warn error
    @warn.error
    async def warn_error(self, ctx, error):
        if isinstance(error, MissingPermissions):
            await ctx.send("You do not have permission to use this command!")

        if isinstance(error, CommandError):
            embed = discord.Embed (
                title = "Command Error",
                description = "Pls specify a member and reason for warning!\n```Could not complete your request!```",
                color = discord.Color.dark_red()
            )
            await ctx.send(embed=embed)
            print(f"{self.client.user} Error 404: Command Error")


    # warnings
    @commands.command(help="Shows amount of warnings for a member.")
    @commands.has_role("Moderators")
    async def warnings(self, ctx, *, user:discord.Member):
        if ctx.author == self.client.user:
            return
        if ctx.author.bot:
            return

        db = sqlite3.connect('warnings.sqlite')
        cursor = db.cursor()
        cursor.execute("SELECT reason FROM warns WHERE user_id = ? AND guild_id = ?", (user.id, ctx.guild.id))
        data = cursor.fetchall()

        # if user has a warning
        if data:
            embed = discord.Embed (
                title = f"Warning Report for `{user}`",
                description = f"**Warnings:** {len(data)}",
                color = discord.Color.blurple()
            )
            await ctx.send(embed=embed)
            await ctx.send(f"`{user}` has {len(data)} warnings.")
        # if user has no warnings
        else:
            embed = discord.Embed (
                title = f"Warning Report for `{user}`",
                description = f"**Warnings:** {len(data)}",
                color = discord.Color.blurple()
            )
            await ctx.send(embed=embed)
            await ctx.send(f"`{user}` has {len(data)} warnings.")

    # warnings error
    @warnings.error
    async def warnings_error(self, ctx, error):
        if isinstance(error, MissingPermissions):
            await ctx.send("You do not have permission to use this command!")

        if isinstance(error, CommandError):
            embed = discord.Embed (
                title = "Command Error",
                description = "Pls specify a member for me to view their warning report!\n```Could not complete your request!```",
                color = discord.Color.dark_red()
            )
            await ctx.send(embed=embed)
            print(f"{self.client.user} Error 404: Command Error")


    # remove warn command
    @commands.command(help="Remove all warnings from a member.")
    @commands.has_role("Moderators")
    @has_permissions(manage_roles=True, kick_members=True, ban_members=True)
    async def removewarns(self, ctx, *, user:discord.Member):
        if ctx.author == self.client.user:
            return
        if ctx.author.bot:
            return

        db = sqlite3.connect('warnings.sqlite')
        cursor = db.cursor()
        cursor.execute("SELECT reason FROM warns WHERE user_id = ? AND guild_id = ?", (user.id, ctx.guild.id))
        data = cursor.fetchone()
        if data:
            cursor.execute("DELETE FROM warns WHERE user_id = ? AND guild_id = ?", (user.id, ctx.guild.id))
            await ctx.send(f"Warnings removed from `{user}`.")
        else:
            await ctx.send(f"`{user}` has {len(data)} warnings.")
        db.commit()

    # remove warn error
    @removewarns.error
    async def removewarns_error(self, ctx, error):
        if isinstance(error, MissingPermissions):
            await ctx.send("You do not have permission to use this command!")

        if isinstance(error, CommandError):
            embed = discord.Embed (
                title = "Command Error",
                description = "Pls try again!\n```Could not complete your request!```",
                color = discord.Color.dark_red()
            )
            await ctx.send(embed=embed)
            print(f"{self.client.user} Error 404: Command Error")


def setup(client):
    client.add_cog(Warns_Database(client))

def teardown(client):
    client.remove_cog(Warns_Database(client))