from discord.ext import commands
from neuralintents import GenericAssistant

class Chatbot(commands.Cog):
    """Cog for Chatbot A.I."""
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.client.user:
            return

        chatbot = GenericAssistant("intents.json")
        chatbot.train_model()
        chatbot.save_model()

        if message.content.lower().startswith("hey endroid"):
            response = chatbot.request(message.content[12:])
            await message.channel.typing()
            await message.channel.send(response)


async def setup(client):
    await client.add_cog(Chatbot(client))

async def teardown(client):
    await client.remove_cog(Chatbot(client))