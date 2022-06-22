import discord
from discord.ext import commands
import random
import asyncio
import pytz
from datetime import datetime

class Auto_Responses(commands.Cog):
    """Bot auto responses"""
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.client.user:
            return

        # test
        if message.content.lower().startswith("test"):
            await message.channel.trigger_typing()
            await message.channel.send("Testing")

        # ping pomg
        if message.content.lower().startswith("ping"):
            await message.channel.trigger_typing()
            await message.channel.send("🏓pong")

        # beep boop
        if message.content.lower().startswith("beep"):
            await message.channel.trigger_typing()
            await message.channel.send("boop")

        # F
        if message.content == "F":
            await message.channel.trigger_typing()
            await message.channel.send("F")
            print("F")

        # bruh
        if "bruh" in message.content.lower():
            await message.channel.trigger_typing()
            await message.channel.send("bruh")

        # input
        if "input" in message.content.lower():
            await message.channel.trigger_typing()
            await message.channel.send("`output`")

        # I have no friends
        if message.content.lower().startswith("I have no friends"):
            await message.channel.trigger_typing()
            await message.channel.send("F")

        # say something
        if message.content.lower().startswith("say something"):
            await message.channel.trigger_typing()
            await message.channel.send("something")

        # tell me something
        if message.content.lower().startswith("tell me something"):
            await message.channel.trigger_typing()
            await message.channel.send("something")

        # tell me a joke
        if message.content.lower().startswith("tell me a joke"):
            await message.channel.trigger_typing()
            await message.channel.send("you")

        # stupid bot
        if "stupid bot" in message.content.lower():
            await message.channel.trigger_typing()
            await message.channel.send("what is my purpose?")

        # ¯\_(ツ)_/¯
        if "¯\_(ツ)_/¯" in message.content:
            await message.channel.trigger_typing()
            await message.channel.send("¯\_(ツ)_/¯")

        # hello bot(s)
        if message.content.lower().startswith("hello bot") or message.content.lower().startswith("hello bots"):
            await message.channel.trigger_typing()
            await message.channel.send(f"Hello {message.author.mention}")

        # hi bot(s)
        if message.content.lower().startswith("hi bot") or message.content.lower().startswith("hi bots"):
            await message.channel.trigger_typing()
            await message.channel.send(f"Hi {message.author.mention}")

        # hey bot(s)
        if message.content.lower().startswith("hey bot") or message.content.lower().startswith("hey bots"):
            await message.channel.trigger_typing()
            await message.channel.send(f"hey {message.author.mention}")

        # hello endroid
        if message.content.lower().startswith("hello endroid"):
            await message.channel.trigger_typing()
            await message.channel.send(f"Hello {message.author.mention}")

        # hi endroid
        if message.content.lower().startswith("hi endroid"):
            await message.channel.trigger_typing()
            await message.channel.send(f"Hi {message.author.mention}")

        # jmm
        if "jmm" in message.content.lower():
            await message.channel.trigger_typing()
            await message.channel.send("jmm")

        # jumm
        if "jumm" in message.content.lower():
            await message.channel.trigger_typing()
            await message.channel.send("jumm")

        # I thought you did
        if "did not" in message.content.lower() or "didn't" in message.content.lower() or "didnt" in message.content.lower():
            await message.channel.trigger_typing()
            await message.channel.send("I thought you did.")

        # dead chat embed
        if message.content.lower().startswith("dead chat"):
            embed = discord.Embed (
                title = "Dead Chat",
                color=0xc7ecf7
            )
            embed.set_image(url="https://preview.redd.it/b1aottwgbtj51.png?auto=webp&s=b2c132f40a48d15076975cf689ce4e95c92b12dd")
            await message.channel.send(embed=embed)
            print("dead chat")

        # teleport bread embed
        if message.content.lower().startswith("teleport bread"):
            embed = discord.Embed (
                title = "Teleport Bread",
                description = "I have done nothing but teleport bread for 3 days!",
                color=0xc7ecf7
            )
            embed.set_image(url="https://i.redd.it/7bhjucd8g5p81.png")
            await message.channel.send(embed=embed)
            print("teleporting bread")

        # bot ping
        if self.client.user.mention in message.content.lower().split():
            ping_responses = [
                "Why me?",
                "Why ping me?",
                "You mentioned me?",
                "You called?",
                "I see what you're trying to do, you can't break me that easily!",
                "What are you doing?",
                "Are you sure about that?",
                "No",
                "Yes",
                "What",
                "What you want",
                "What do you want",
                "I can't assist you",
                "I can't help you at this moment",
                "Go away",
                "Go bother someone else",
                "Don't disturb me!"
            ]
            await message.channel.trigger_typing()
            await message.channel.send(f"{random.choice(ping_responses)}")
            print("Why me?")

        #pog, poggers and pogchamp
        if "pog" in message.content.lower() or "poggers" in message.content.lower() or "pogchamp" in message.content.lower():
            pog_responses = [
                "pog",
                "poggers",
                "pogchamp",
                "Pog!",
                "Poggers",
                "Pogchamp!"
            ]
            await message.channel.trigger_typing()
            await message.channel.send(f'{random.choice(pog_responses)}')

        # I am responses
        if message.content.lower().replace("'", "").strip().startswith("i am"):
            responses = {
                "elai":"Are you sure about that?",
                "endroid":"You're not Endroid, I'm Endroid!",
                "a bot":"You're not a bot! I'm a bot!",
                "bot":"You're not a bot! I'm a bot!",
                "stupid":"Yeah, I know.",
                "a fucking dumbass":"yes you are indeed",
                "a dumbass":"yeah you are"
            }
            for trigger, response in list(responses.items()):
                if trigger in message.content.lower().replace("'", "").replace("i am", "").strip():
                    await message.channel.trigger_typing()
                    return await message.channel.send(response)
            await message.channel.trigger_typing()
            await message.channel.send("Hi " + message.content.lower().replace("i am", "").strip() + ", I'm Endroid!")

        # I'm responses
        if message.content.lower().replace("'", "").strip().startswith("im"):
            responses = {
                "elai":"Are you sure about that?",
                "endroid":"You're not Endroid, I'm Endroid!",
                "a bot":"You're not a bot! I'm a bot!",
                "bot":"You're not a bot! I'm a bot!",
                "stupid":"Yeah, I know.",
                "a fucking dumbass":"yes you are indeed",
                "a dumbass":"yeah you are"
            }
            for trigger, response in list(responses.items()):
                if trigger in message.content.lower().replace("'", "").replace("im", "").strip():
                    await message.channel.trigger_typing()
                    return await message.channel.send(response)
            await message.channel.trigger_typing()
            await message.channel.send("Hi " + message.content.lower().replace("im", "").strip() + ", I'm Endroid!")

        # hey endroid
        if message.content.lower().startswith("hey endroid"):
            await message.channel.trigger_typing()
            await message.channel.send("hey yo")

            # if no reply within 30 secs
            try:
                reply_message = await self.client.wait_for('message', timeout=30.0)
            except asyncio.TimeoutError:
                await reply_message.channel.trigger_typing()
                await reply_message.channel.send("why won't you reply me?")

            # how are you
            else:
                if reply_message.content.lower().startswith("how are you"):
                    feelings =[
                        "I'm okay, thank you.",
                        "i'm fine, thank you.",
                        "Not good",
                        "Go away",
                        "Not okay",
                        "I'm good!",
                        "I am not okay",
                        "Go bother someone else"
                    ]
                    await reply_message.channel.trigger_typing()
                    await reply_message.channel.send(f'{random.choice(feelings)}')

                # tell me about yourself
                if reply_message.content.lower().startswith("tell me about yourself"):
                    await reply_message.channel.trigger_typing()
                    await reply_message.channel.send("My name is Endroid, I am an android. I am also a bot. ELai made me.")

                # time
                if reply_message.content.lower().startswith("what's the time") or reply_message.content.lower().startswith("whats the time") or reply_message.content.lower().startswith("what is the time"):
                    timestamp = datetime.now()
                    gmt = pytz.timezone('Asia/Singapore')
                    embed = discord.Embed (
                        title = "Current date and time in GMT +08:00",
                        color=0xc7ecf7
                    )
                    embed.add_field(name="Date", value=timestamp.astimezone(gmt).strftime("%a %d %b %Y"), inline=False)
                    embed.add_field(name="Time", value=timestamp.astimezone(gmt).strftime("%I:%M %p"), inline=False)
                    
                    await reply_message.channel.trigger_typing()
                    await reply_message.channel.send(embed=embed)

                # Isaac Asimov Robot Laws
                if reply_message.content.lower().startswith("tell me about robot laws") or reply_message.content.lower().startswith("tell me about the robot laws"):
                    embed = discord.Embed (
                        title="The Three Laws of Robotics",
                        color=0xc7ecf7
                    )
                    # First Law
                    embed.add_field(name="First Law", value="A robot may not injure a human being or, through inaction, allow a human being to come to harm.", inline=False)
                    # Second Law
                    embed.add_field(name="Second Law", value="A robot must obey the orders given it by human beings except where such orders would conflict with the **First Law**.", inline=False)
                    # Third Law
                    embed.add_field(name="Third Law", value="A robot must protect its own existence as long as such protection does not conflict with the **First** or **Second Law**.", inline=False)
                    # embed footer
                    embed.set_footer(text="The Three Laws of Robotics was created by Isaac Asimov in 1942.")

                    await reply_message.channel.trigger_typing()
                    await reply_message.channel.send(embed=embed)

                # you're responses
                if reply_message.content.lower().replace("'", "").strip().startswith("youre"):
                    responses = {
                        "useless":"how dare you!",
                        "dumb":"evrywan dum",
                        "dum":"evrywan dum",
                        "a dumb bot":"Why was I born?",
                        "crazy":"maybe ¯\_(ツ)_/¯",
                        "weird":"everyone is weird, don't pretend you're not!",
                        "good bot":"thank you!",
                        "smart bot":"Yes!",
                        "idiot":"why must you insult me?",
                        "annoying":"Why are we still here? Just to suffer?"
                    }
                    for trigger, response in list(responses.items()):
                        if trigger in reply_message.content.lower().replace("'", "").replace("youre", "").strip():
                            await message.channel.trigger_typing()
                            return await reply_message.channel.send(response)

                # ur responses
                if reply_message.content.lower().startswith("ur"):
                    responses = {
                        "useless":"how dare you!",
                        "dumb":"evrywan dum",
                        "dum":"evrywan dum",
                        "a dumb bot":"Why was I born?",
                        "crazy":"maybe ¯\_(ツ)_/¯",
                        "weird":"everyone is weird, don't pretend you're not!",
                        "good bot":"thank you!",
                        "smart bot":"Yes!",
                        "idiot":"why must you insult me?",
                        "annoying":"Why are we still here? Just to suffer?"
                    }
                    for trigger, response in list(responses.items()):
                        if trigger in reply_message.content.lower().startswith("ur"):
                            await message.channel.trigger_typing()
                            return await reply_message.channel.send(response)

        # turn that frown upside down
        if ":(" in message.content:
            await message.channel.trigger_typing()
            await message.channel.send("Turn that frown upside down!")

            # if no reply within 30 secs
            try:
                reply_message = await self.client.wait_for('message', timeout=30.0)
            except asyncio.TimeoutError:
                await reply_message.channel.trigger_typing()
                await reply_message.channel.send("why won't you reply me?")

            # reply with "no"
            else:
                if "no" in reply_message.content.lower():
                    await reply_message.channel.trigger_typing()
                    await reply_message.channel.send("How dare you!")

                # reply with ":)"
                if ":)" in reply_message.content:
                    await reply_message.channel.trigger_typing()
                    await reply_message.channel.send("Excellent!")

                # reply with "):"
                if "):" in reply_message.content:
                    await reply_message.channel.trigger_typing()
                    await reply_message.channel.send("listen here you piece of shit")

                # reply with "(:"
                if "(:" in reply_message.content:
                    await reply_message.channel.trigger_typing()
                    await reply_message.channel.send(":)")


def setup(client):
    client.add_cog(Auto_Responses(client))