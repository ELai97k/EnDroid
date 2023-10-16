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
    @has_permissions(administrator=True, manage_roles=True)
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


    # auto responses off
    @commands.command(pass_context=True, help="Turn off bot's auto-responses.")
    async def autoresponse_off(self, ctx):
        if ctx.author == self.client.user:
            return
        if ctx.author.bot:
            return

        embed = discord.Embed (
            title = "Operation Successful!",
            description = "`Auto responses` has been turned **OFF** and your changes were saved.",
            color=0x198C19
        )
        await ctx.send(embed=embed)
        await self.client.unload_extension("cogs.autoresponses")
        print("Auto responses has been turned off")


    # auto responses on
    @commands.command(pass_context=True, help="Turn on bot's auto-responses.")
    async def autoresponse_on(self, ctx):
        if ctx.author == self.client.user:
            return
        if ctx.author.bot:
            return

        embed = discord.Embed (
            title = "Operation Successful!",
            description = "`Auto responses` has been turned **ON** and your changes were saved.",
            color=0x198C19
        )
        await ctx.send(embed=embed)
        await self.client.load_extension("cogs.autoresponses")
        print("Auto responses has been turned on")


    # embed showing bot's auto responses
    @commands.command(help="Embed that shows what messages the bot will auto-respond to.")
    async def responses(self, ctx):
        if ctx.author == self.client.user:
            return
        if ctx.author.bot:
            return

        embed = discord.Embed (
            title = "Endroid will automatically respond to the following messages:",
            description = ":(\nI'm / im\nteleport bread\ndead chat\nwhy isn't this working\njmm\njumm\nhi / hello endroid\nhello / hi / hey bot(s)\nstupid bot\ntell me a joke\nsay something / tell me something\nI have no friends\ninput\nbruh\nF\nshut up bot / bot shut up\nshut up endroid / endroid shut up\nendroid is annoying",
            color=0xc7ecf7
        )
        await ctx.send(embed=embed)


    # hey endroid
    @commands.command(help="Command embed to find out what you can input when you trigger 'hey endroid' in message.")
    async def heyprompts(self, ctx):
        if ctx.author == self.client.user:
            return
        if ctx.author.bot:
            return

        embed = discord.Embed (
            title = "List of available options after typing 'hey endroid'",
            description = "`how are you / how are you doing`\n`who made you / who created you`\n`what's the time / what is the time now`\n`what are the laws of robotics`",
            color=0xc7ecf7
        )
        # you're / ur responses
        embed.add_field(name="`you're / ur`",
        value="stupid\ndumb\ndum\na dumbass\nuseless\nnot helpful\nnot helping\na good bot\na clever bot\na cleverbot\na smart bot\nannoying",
        inline=False)

        await ctx.send(embed=embed)


async def setup(client):
    await client.add_cog(Botcog(client))

async def teardown(client):
    await client.remove_cog(Botcog(client))