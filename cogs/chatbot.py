import discord
from discord.ext import commands
from neuralintents import GenericAssistant

class Chatbot(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.client.user:
            return

        

def setup(client):
    client.add_cog(Chatbot(client))