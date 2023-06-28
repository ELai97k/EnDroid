import discord
import asyncio
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions

class Botcog(commands.Cog):
    """Bot cog."""
    def __init__(self, client):
        self.client = client

    # welcome embed
    @commands.Cog.listener()
    async def on_member_join(self, member):
        if member.guild.id == 762317365970468874:
            embed = discord.Embed (
                title=f'Hello {member.name}, and welcome to **{member.guild.name}**!',
                description='Have a look at the rules at <#855777347730407434> and server info at <#855775497955180545>.',
                color=0x198C19
            )
            embed.set_footer(text='Thank you for joining us! We hope you enjoy your stay.')
            await self.client.get_channel(762317365970468877).send(embed=embed)

    # goodbye embed
    @commands.Cog.listener()
    async def on_member_remove(self, member):
        if member.guild.id == 762317365970468874:
            embed = discord.Embed (
                title=f'{member} has left the server!',
                description="Sorry to see you go.",
                color=0x1e377f
            )
        await self.client.get_channel(762317365970468877).send(embed=embed)


    # log out
    @commands.command(help="Command for bot log out.")
    @has_permissions(administrator=True)
    async def logout(self, ctx):
        if ctx.author == self.client.user:
            return
        if ctx.author.bot:
            return
        
        await ctx.channel.typing()
        await ctx.send(f"```{self.client.user} logging out...\nReminder: Log me back in manually through the terminal.```")
        
        print(f"{self.client.user} logging out...")
        print("Reminder: Log me back in manually.")

        await asyncio.sleep(3)
        await self.client.change_presence(status=discord.Status.offline)
        await asyncio.sleep(3)
        await self.client.close()

    @logout.error
    async def logout_error(self, ctx, error):
        if isinstance(error, MissingPermissions):
            await ctx.send("You do not have permission to use this command!")


async def setup(client):
    await client.add_cog(Botcog(client))

async def teardown(client):
    await client.remove_cog(Botcog(client))