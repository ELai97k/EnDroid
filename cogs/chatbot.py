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

        chatbot = GenericAssistant("intents.json")
        chatbot.train_model()
        chatbot.save_model()

        if message.content.lower().startswith("bot"):
            response = chatbot.request(message.content.lower()[2:])
            await message.channel.trigger_typing()
            await message.channel.send(response)


def setup(client):
    client.add_cog(Chatbot(client))