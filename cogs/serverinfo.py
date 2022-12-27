import discord
from discord.ext import commands

class ServerInfo(commands.Cog):
    """Cog for server info."""
    def __init__(self, client):
        self.client = client

    @commands.command(help="Command for server information.")
    async def serverinfo(self, ctx):
        if ctx.author == self.client.user:
            return
        if ctx.author.bot:
            return
        
        embed = discord.Embed (
            title = f"{ctx.guild.name} Info",
            color = 0xc7ecf7
        )
        embed.add_field(name='🆔 Server ID:', value=f"{ctx.guild.id}", inline=True)
        embed.add_field(name='📆 Created On:', value=ctx.guild.created_at.strftime("%a, %d %b, %Y"), inline=False)
        embed.add_field(name='👑 Owner:', value=f"{ctx.guild.owner.mention}", inline=False)
        embed.add_field(name='👥 Members:', value=f'{ctx.guild.member_count} Members', inline=False)
        embed.add_field(name='💬 Channels:', value=f'{len(ctx.guild.text_channels)} Text channels\n{len(ctx.guild.voice_channels)} Voice channels', inline=False)

        await ctx.send(embed=embed)


async def setup(client):
    await client.add_cog(ServerInfo(client))

async def teardown(client):
    await client.remove_cog(ServerInfo(client))