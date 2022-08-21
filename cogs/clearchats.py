import discord
from discord.ext import commands

class ClearChats(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(pass_context=True, aliases=["deletechats", "clearmsgs", "deletemsgs"])
    @commands.has_role("Moderators")
    async def clearchats(self, ctx, amount=None):
        if amount is None:
            print(f"Deleting {amount} messages")
            await ctx.channel.purge(limit=50)

        elif amount == "all":
            print("Purging text channel . . .")
            await ctx.channel.purge()

        else:
            print(f"Deleting {amount} messages")
            await ctx.channel.purge(limit=int(amount))


def setup(client):
    client.add_cog(ClearChats(client))