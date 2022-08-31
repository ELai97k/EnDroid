import discord
from discord.ext import commands

class g_bar(commands.Cog):
    def __init__(self, client):
        self.client = client

    # Gay Bar welcome embed
    @commands.Cog.listener()
    async def on_member_join(self, member):
        if member.guild.name == "Gay Bar 3.0":
            embed = discord.Embed (
                title=f'Hello {member.name}, and welcome to **{member.guild.name}**!',
                description='Have a look at the rules at <#855777347730407434> and server info at <#855775497955180545>.',
                color=0x198C19
            )
            embed.set_footer(text='Thank you for joining us! We hope you enjoy your stay.')
            await self.client.get_channel(762317365970468877).send(embed=embed)


    # Gay Bar goodbye embed
    @commands.Cog.listener()
    async def on_member_remove(self, member):
        if member.guild.name == "Gay Bar 3.0":
            embed = discord.Embed (
                title=f'{member} has left the server!',
                description="Sorry to see you go!",
                color=0x1e377f
            )
        await self.client.get_channel(762317365970468877).send(embed=embed)


def setup(client):
    client.add_cog(g_bar(client))