from discord.ext import commands
import random
import asyncio

class Ee(commands.Cog):
    """ e """
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):
        # e
        if "e" in message.content and "!" not in message.content and message.author.id != 696008187991687189 and message.author.id != 973407928654651392:
            await asyncio.sleep(60)
            e_responses = [
                "what's going on here?",
                "wdym",
                "I see",
                "Oh",
                "yes",
                "no",
                "What?",
                "Who?",
                "Why?",
                "When?",
                "How?",
                "ah",
                "ok",
                "Okay",
                "I don't get it"
            ]
            await message.channel.send(f'{random.choice(e_responses)}')
            print("e")


def setup(client):
    client.add_cog(Ee(client))

def teardown(client):
    client.remove_cog(Ee(client))