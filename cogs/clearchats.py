from ast import alias
import discord
from discord.ext import commands

class Clear_Chats(commands.Cog):
    def __init__(self, client):
        self.client = client

    # clear chat in text channel
    @commands.command(pass_context=True, name="clearchats", aliases=["deletechats"])
    async def _clearchats(self, ctx, amount=100):
        channel = ctx.message.channel
        messages = []
        async for message in self.client.logs_from(channel, limit=int(amount) + 1):
            messages.append(message)
            await self.client.delete_messages(messages)
            print(f"Deleting messages in {channel} . . .")


def setup(client):
    client.add_cog(Clear_Chats(client))