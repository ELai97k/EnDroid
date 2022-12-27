import discord
from discord.ext import commands

class Triggers(commands.Cog):
    """Bot filter for bad words."""
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.client.user:
            return
        if message.author.bot:
            return

        # bad words
        if message.author.guild.id == 911112792646508624: # Elai's server
            bad_list = [
                "dick",
                "cuck",
                "cock",
                "sex",
                "nigga",
                "nigger",
                "negro",
                "penis",
                "vagina",
                "nude",
                "porn",
                "pornhub.com",
                "brazzers.com",
                "faggot",
                "naked",
                "cum ",
                "motherfucker"
            ]
            for bad_word in bad_list:
                if bad_word in message.content.lower():
                    # trigger embed
                    embed = discord.Embed (
                        title=f"**⚠ WARNING for `{message.author}`!**",
                        description=f"{message.author.name}, you have broken one of Da Rules, and your warning has been recorded and added to your userdata. If you think that this was a mistake, DM or ping the Admin or Mods for further discussion.",
                        color=discord.Color.dark_red()
                    )
                    await message.channel.send(embed=embed)
                    await message.delete()
                    print(f"{message.author} has been given a warning!")


    # trigger words
    @commands.command(help="Command that displays a list of bad words.")
    async def triggers(self, ctx):
        if ctx.author == self.client.user:
            return
        if ctx.author.bot:
            return
 
        embed = discord.Embed (
            title = "Endroid will delete these censored words:",
            description="||`Dick`\n`Cuck(s)`\n`Cock(s)`\n`Sex`\n`Nigga`\n`Nigger`\n`Negro`\n`Penis`\n`Vagina`\n`Nude`\n`Pronhub.com`\n`Brazzers.com`\n`Faggot`\n`Naked`\n`Cum`\n`Motherfucker`||",
            color=discord.Color.dark_red()
        )
        embed.set_footer(text="You will be given a warning that will trigger Endroid's auto-moderation")
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Triggers(client))

def teardown(client):
    client.remove_cog(Triggers(client))