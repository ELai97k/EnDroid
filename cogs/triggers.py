import discord
import sqlite3
from discord.ext import commands

class Triggers(commands.Cog):
    """Bot filter for bad words."""
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message, ctx, user:discord.Member, *, reason:str):
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
                "porn",
                "pornhub.com",
                "brazzers.com",
                "faggot",
                "cum ",
                "motherfucker"
            ]
            for bad_word in bad_list:
                if bad_word in message.content.lower():
                    # trigger embed
                    embed = discord.Embed (
                        title=f"**:warning: WARNING for `{message.author}`!**",
                        description=f"{message.author.name}, you're being inappropriate! Don't say that again!",
                        color=discord.Color.dark_red()
                    )
                    await message.channel.send(embed=embed)
                    await message.delete()
                    await message.send(f"{message.author.mention} you have been given a warning!")
                    print(f"{message.author} has been given a warning!")

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

    # trigger words
    @commands.command(help="Command that displays a list of bad words.")
    async def triggers(self, ctx):
        if ctx.author == self.client.user:
            return
        if ctx.author.bot:
            return
 
        embed = discord.Embed (
            title = "Endroid will delete these censored words:",
            description="||`Dick`\n`Cuck(s)`\n`Cock(s)`\n`Sex`\n`Nigga`\n`Nigger`\n`Negro`\n`Penis`\n`Vagina`\n`Pronhub.com`\n`Brazzers.com`\n`Faggot`\n`Cum`\n`Motherfucker`||",
            color=discord.Color.dark_red()
        )
        embed.set_footer(text="You will be given a warning that will trigger Endroid's auto-moderation")
        await ctx.send(embed=embed)


async def setup(client):
    await client.add_cog(Triggers(client))

async def teardown(client):
    await client.remove_cog(Triggers(client))