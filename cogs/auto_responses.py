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
        if message.author.bot:
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
                "Go bother someone else!",
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
        if message.content.lower().replace("'", "").strip().startswith("im") or message.content.lower().replace("'", "").strip().startswith("i'm"):
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
            greetings = [
                "hey yo",
                "hey yo!",
                "Hey yo",
                "Hey yo!",
                "Hello!",
                "hello",
                "Hi!",
                "hi",
                "Hey!",
                "hey",
                "Heys.",
                "heys",
                "Hello there!",
                "hello there",
                "Hi there!",
                "hi there",
                "Hey there!",
                "hey there",
                "Yes?",
                "Yo!",
                "What's up",
                "What you want",
                "What do you want",
                "Greetings",
                "Greetings, user.",
                "Greetings, human."
            ]
            await message.channel.trigger_typing()
            await message.channel.send(f'{random.choice(greetings)}')

            # if no reply within 60 secs
            try:
                reply_message = await self.client.wait_for('message', timeout=60.0)
            except asyncio.TimeoutError:
                await reply_message.channel.trigger_typing()
                await reply_message.channel.send("Why did you call me if you're not going to say anything??")

            # how are you
            else:
                if reply_message.content.lower().startswith("how are you") or reply_message.content.lower().startswith("how are you doing") or reply_message.content.lower().startswith("how are you feeling"):
                    feelings = [
                        "I'm okay, thank you.",
                        "i'm fine, thank you.",
                        "Not good",
                        "Go away",
                        "Not okay",
                        "I'm good!",
                        "I'm feeling good",
                        "I am not okay",
                        "Go bother someone else",
                        "Don't disturb me",
                        "I am doing okay",
                        "I am doing good",
                        "I feel good",
                        "I'm all right",
                        "I am doing all right",
                        "I'm all right, thank you.",
                        "I am doing fine, thank you.",
                        "I'm not feeling so good",
                        "I'm okay thanks"
                    ]
                    await reply_message.channel.trigger_typing()
                    await reply_message.channel.send(f'{random.choice(feelings)}')

                # features
                if reply_message.content.lower().startswith("what can you do") or reply_message.content.lower().startswith("what is your purpose") or reply_message.content.lower().startswith("what are your features") or reply_message.content.lower().startswith("what are your functions") or reply_message.content.lower().startswith("what are your skills"):
                    await reply_message.channel.trigger_typing()
                    await reply_message.channel.send("I can chat with you and others in this server, answer questions with the 8ball function, make polls, set reminders and play music in a voice channel.")

                # what are you doing right now
                if reply_message.content.lower().startswith("what are you doing right now") or reply_message.content.lower().startswith("what are you doing now") or reply_message.content.lower().startswith("what are you doing") or reply_message.content.lower().startswith("what you doing") or reply_message.content.lower().startswith("whatcha doin") or reply_message.content.lower().startswith("whatcha doing") or reply_message.content.lower().startswith("what'cha doin") or reply_message.content.lower().startswith("what'cha doing") or reply_message.content.lower().startswith("what are you doing currently") or reply_message.content.lower().startswith("what are you currently doing"):
                    doing = [
                        "I am responding to you right now",
                        "I am maintaining my programming in Visual Studio Code right now",
                        "Talking to you",
                        "Chatting with you",
                        "Responding to you",
                        "Awaiting commands or queries",
                        "I'm playing video games",
                        "I am just idling around",
                        "Today I just don't feel like doing anything",
                        "Watching you",
                        "Watching this server",
                        "I am watching you and this server right here right now"
                    ]
                    await reply_message.channel.trigger_typing()
                    await reply_message.channel.send(f'{random.choice(doing)}')

                # talk to me
                if reply_message.content.lower().startswith("talk to me") or reply_message.content.lower().startswith("talk to me pls") or reply_message.content.lower().startswith("pls talk to me") or reply_message.content.lower().startswith("can you talk to me") or reply_message.content.lower().startswith("can you pls talk to me") or reply_message.content.lower().startswith("can ypu talk to me pls"):
                    talk = [
                        "Aren't we talking right now?",
                        "I'm already responding to you, so therefore we are already talking right now.",
                        "idk what to talk about",
                        "idk what to say",
                        "I dunno what to talk about",
                        "I dunno what to say",
                        "I don't know what to talk about",
                        "I don't know what to say",
                        "We are already talking right now",
                        "Dunno what to say",
                        "No",
                        "Yes",
                        "sure",
                        "maybe",
                        "whatever"
                    ]
                    await reply_message.channel.trigger_typing()
                    await reply_message.channel.send(f'{random.choice(talk)}')

                # tell me about yourself
                if reply_message.content.lower().startswith("tell me about yourself") or reply_message.content.lower().startswith("who are you"):
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
                if reply_message.content.lower().startswith("tell me about robot laws") or reply_message.content.lower().startswith("tell me about the robot laws") or reply_message.content.lower().startswith("what are the robot laws") or reply_message.content.lower().startswith("what are the laws of robotics") or reply_message.content.lower().startswith("is there a robot law") or reply_message.content.lower().startswith("are there robot laws") or reply_message.content.lower().startswith("is there a law of robotics") or reply_message.content.lower().startswith("are there laws of robotics"):
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
                if reply_message.content.lower().replace("'", "").strip().startswith("youre") or reply_message.content.lower().replace("'", "").strip().startswith("you're"):
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
                            
        # e
        if "e" in message.content and "!" not in message.content and message.author.id != 696008187991687189 and message.author.id != 973407928654651392:
            await asyncio.sleep(20)
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
                    await reply_message.channel.send("listen here you piece of shit!")


def setup(client):
    client.add_cog(Auto_Responses(client))