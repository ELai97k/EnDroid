import discord
from discord.ext import commands

class MainCog(commands.Cog):
    """Main cog for sending welcome and goodbye message embeds."""
    def __init__(self, client):
        self.client = client

    # welcome embed
    @commands.Cog.listener()
    async def on_member_join(self, member):
        if member.guild.id == 911112792646508624: # Elai's server
            embed = discord.Embed (
                title = f'Hello {member.name}, and welcome to **{member.guild.name}**!',
                description = 'Pls read the rules at <#911130413756461126> and react to that message to unlock the rest of the server.',
                color=0x198C19
            )
            embed.set_footer(text='Thank you for joining us! We hope you enjoy your stay.')
            await self.client.get_channel(918831456187461652).send(embed=embed)

            # auto role on join
            role = discord.utils.get(member.guild.roles, name="Unverified")
            await member.add_roles(role)
            print(f'{member} has joined the server!')

    # goodbye embed
    @commands.Cog.listener()
    async def on_member_remove(self, member):
        if member.guild.id == 911112792646508624: # Elai's server
            embed = discord.Embed (
                title = f'{member} has left the server!',
                description = "Sorry to see you go.",
                color=0x1e377f
            )
            await self.client.get_channel(918831456187461652).send(embed=embed)
            print(f'{member} has left the server!')

            # remove role on leave
            role = discord.utils.get(member.guild.roles, name="Verified")
            await member.remove_roles(role)


def setup(client):
    client.add_cog(MainCog(client))

def teardown(client):
    client.remove_cog(MainCog(client))