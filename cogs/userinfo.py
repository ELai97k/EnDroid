import discord
import datetime
from discord.ext import commands

class UserInfo(commands.Cog):
    """Command to fetch user info"""
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def userinfo(self, ctx, *, user: discord.Member = None):
        if ctx.author == self.client.user:
            return
        if ctx.author.bot:
            return
        
        if user is None:
            user = ctx.author

        date_format = "%a, %d %b, %Y"
        status = user.status[0]
        statusnames = {"online" : "Online", "dnd" : "Do Not Disturb", "idle" : "Idle", "offline" : "Invisible/Offline"}
        statusemojis = {"online" : "🟢", "dnd": "🔴", "idle" : "🌙", "offline" : "⚫"}

        embed = discord.Embed (
            title = f"{user.name}'s Info",
            color=0xffd966
        )
        embed.set_author(name=str(user), icon_url=user.avatar_url)
        embed.set_thumbnail(url=user.avatar_url)

        # server join date
        embed.add_field(name="Date joined:", value=user.joined_at.strftime(date_format), inline=False)
        # discord account created date
        embed.add_field(name="Account created:", value=user.created_at.strftime(date_format), inline=False)

        # server join position
        #members = sorted(ctx.guild.members, key=lambda m: m.joined_at)
        #embed.add_field(name="Join position:", value=str(members.index(user)+1), inline=False)

        if len(user.roles) > 1:
            role_string = ' '.join([r.mention for r in user.roles][1:])
            embed.add_field(name="Server roles ({})".format(len(user.roles)-1), value=role_string, inline=False)

        perm_string = ', '.join([str(p[0]).replace("_", " ").title() for p in user.guild_permissions if p[1]])

        embed.add_field(name="Guild permissions:", value=perm_string, inline=False)
        embed.add_field(name="Status:", value=f"{statusemojis[status]} {statusnames[status]}", inline=False)

        embed.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(UserInfo(client))