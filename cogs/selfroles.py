import discord
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions

class SelfRoles (commands.Cog):
    """Self roles."""
    def __init__(self, client):
        self.client = client

    # embed commands
    @commands.command(aliases = ["self_roles"], help="Get Verified embed command.")
    @has_permissions(administrator=True)
    async def selfroles(self, ctx):
        if ctx.author == self.client.user:
            return
        if ctx.author.bot:
            return

        embed = discord.Embed (
            title = "Self Roles (optional)",
            description = "React to this message with the corresponding emoji and the role associated with it.\n\n📢 <@&1032579279885705257>\n🧡 <@&1078567772524650556>",
            color=0xc7ecf7
        )
        
        await self.client.get_channel(958915454401912863).send(embed=embed)
        await ctx.message.delete()

    @selfroles.error
    async def selfroles_error(self, ctx, error):
        if isinstance(error, MissingPermissions):
            await ctx.send("You do not have permission to use this command!")
            await ctx.message.delete()


async def setup(client):
    await client.add_cog(SelfRoles(client))

async def teardown(client):
    await client.remove_cog(SelfRoles(client))