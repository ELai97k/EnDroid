import discord
from discord.ext import commands

class UserInfo(commands.Cog):
    """Cog for user info."""
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["user"], help="Command to fetch user info.")
    async def userinfo(self, ctx, *, user: discord.Member = None):
        if ctx.author == self.client.user:
            return
        if ctx.author.bot:
            return
        
        if user is None:
            user = ctx.author
        
        # day, date, year
        date_format = "%a, %d %b, %Y"

        # discord status
        status = user.status[0]

        # discord status names
        statusnames = {"online" : "Online", "dnd" : "Do Not Disturb", "idle" : "Idle", "offline" : "Invisible/Offline"}

        # discord status emojis
        statusemojis = {"online" : "🟢", "dnd": "🔴", "idle" : "🌙", "offline" : "⚫"}

        # server roles
        role_string = ' '.join([r.mention for r in user.roles][1:])

        # server / guild permissions
        perm_string = ', '.join([str(p[0]).replace("_", " ").title() for p in user.guild_permissions if p[1]])

        # user info embed
        embed = discord.Embed (
            title = f"{user.name}'s Info",
            color=0xc7ecf7
        )
        embed.set_author(name=str(user), icon_url=user.avatar.url)
        try:
            embed.set_thumbnail(url=user.avatar.url)
        except:
            embed.set_thumbnail(url=str(user.display_avatar.url))

        # server join date
        embed.add_field(name="Date joined:", value=user.joined_at.strftime(date_format), inline=False)
        
        # discord account created date
        embed.add_field(name="Account created:", value=user.created_at.strftime(date_format), inline=False)
        
        # server roles
        embed.add_field(name="Server roles ({})".format(len(user.roles)-1), value=role_string, inline=False)

        # server / guild permissions
        embed.add_field(name="Guild permissions:", value=perm_string, inline=False)

        # member status
        embed.add_field(name="Status:", value=f"{statusemojis[status]} {statusnames[status]}", inline=False)

        await ctx.send(embed=embed)


async def setup(client):
    await client.add_cog(UserInfo(client))

async def teardown(client):
    await client.remove_cog(UserInfo(client))