import discord
import sqlite3
from discord.ext import commands

class Triggers(commands.Cog):
    """Bot filter for bad words."""
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, ctx, user:discord.Member, *, message):
        if message.author == self.client.user:
            return
        if message.author.bot:
            return

        if bad_word in message.content.lower().split():
            bad_list = [
                "dick",
                "cuck",
                "cock",
                "sex",
                "sexy",
                "nigga",
                "nigger",
                "negro",
                "penis",
                "vagina",
                "porn",
                "pornhub.com",
                "brazzers.com",
                "faggot",
                "cum",
                "motherfucker"
            ]
            for bad_word in bad_list:
                if bad_word in message.content.lower().split():
                    # trigger embed
                    embed = discord.Embed (
                        title=f"**:warning: WARNING for `{message.author}`**",
                        description=f"{message.author.name}, you're being inappropriate! Don't say that again!",
                        color=discord.Color.dark_red()
                    )
                    await message.delete()
                    await message.channel.send(embed=embed)
                    print(f"{message.author} has been given a warning!")

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


        async def addwarn(ctx, bad_word, user):
            user = message.author
            db = sqlite3.connect('warnings.sqlite')
            cursor = db.cursor()
            cursor.execute(
                """
                INSERT INTO warns (
                    user_id,
                    user_name,
                    bad_word,
                    guild_id,
                    guild_name
                )
                VALUES (?, ?, ?, ?, ?)
                """, (user.id, user.name, bad_word, ctx.guild.id, ctx.guild.name)
            )
            db.commit()
        await addwarn(ctx, bad_word, user)


async def setup(client):
    await client.add_cog(Triggers(client))

async def teardown(client):
    await client.remove_cog(Triggers(client))