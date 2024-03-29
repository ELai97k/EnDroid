import discord
import random
import asyncio
import pytz
import random
from datetime import datetime
from discord.ext import commands

class AutoResponses(commands.Cog):
    """Bot auto responses."""
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.client.user:
            return
        if message.author.bot:
            return

        # shut bot to turn off auto responses
        if "shut up bot" in message.content.lower() or "bot shut up" in message.content.lower() or "shut up endroid" in message.content.lower() or "endroid shut up" in message.content.lower():
            await message.channel.send("Okay ;_;")

            # turn off this cog
            await self.client.unload_extension("cogs.autoresponses")
            print("Auto responses has been turned off")
            await asyncio.sleep(999) # 16.5 mins

            # turn on this cog
            await self.client.load_extension("cogs.autoresponses")
            print("Auto responses has been turned on")

        # F
        if message.content == "F":
            await message.channel.typing()
            await message.channel.send("F")
            print("F")

        # bruh
        if "bruh" in message.content.lower():
            await message.channel.typing()
            await message.channel.send("bruh")

        # input
        if "input" in message.content.lower():
            await message.channel.typing()
            await message.channel.send("You typed an input so I have to respond with `output`")

        # I have no friends
        if message.content.lower().startswith("i have no friends"):
            await message.channel.typing()
            await message.channel.send("F")

        # say something / tell me something
        if message.content.lower().startswith("say something") or message.content.lower().startswith("tell me something"):
            await message.channel.typing()
            await message.channel.send("something")

        # tell me a joke
        if message.content.lower().startswith("tell me a joke"):
            await message.channel.typing()
            await message.channel.send("you")

        # stupid bot
        if "stupid bot" in message.content.lower():
            await message.channel.typing()
            await message.channel.send("what is my purpose?")

        # hello bot(s)
        if message.content.lower().startswith("hello bot") or message.content.lower().startswith("hello bots"):
            await message.channel.typing()
            await message.channel.send(f"Hello {message.author.mention}")

        # hi bot(s)
        if message.content.lower().startswith("hi bot") or message.content.lower().startswith("hi bots"):
            await message.channel.typing()
            await message.channel.send(f"Hi {message.author.mention}")

        # hey bot(s)
        if message.content.lower().startswith("hey bot") or message.content.lower().startswith("hey bots"):
            await message.channel.typing()
            await message.channel.send(f"hey {message.author.mention}")

        # hello endroid
        if message.content.lower().startswith("hello endroid"):
            await message.channel.typing()
            await message.channel.send(f"Hello {message.author.mention}")

        # hi endroid
        if message.content.lower().startswith("hi endroid"):
            await message.channel.typing()
            await message.channel.send(f"Hi {message.author.mention}")

        # jmm
        if "jmm" in message.content.lower():
            await message.channel.typing()
            await message.channel.send("jmm")

        # jumm
        if "jumm" in message.content.lower():
            await message.channel.typing()
            await message.channel.send("jumm")

        # why isn't this working
        if message.content.lower().startswith("why isnt this working") or message.content.lower().startswith("why isn't this working"):
            await message.channel.typing()
            await message.channel.send("I dunno, why isn't it?")

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
                "I see what you're trying to do, you can't break me that easily!",
                "What are you doing?",
                "Are you sure about that?",
                "No.",
                "Yes.",
                "What?",
                "What you want?",
                "What do you want?",
                "I can't assist you.",
                "I can't help you at this moment.",
                "Go away.",
                "Go bother someone else!",
                "Don't disturb me!",
                "Do not disturb me!",
                "cough",
                "aaaaaaaaaaaaaaaaa",
                "waaaaaaaaaaaaaaaaa"
            ]
            await message.channel.typing()
            await message.channel.send(random.choice(ping_responses))

        # I'm / im responses
        if message.content.lower().replace("'", "").strip().startswith("im"):
            responses = {
                "elai":"Are you sure about that?",
                "endroid":"You're not Endroid, I'm Endroid!",
                "a bot":"You're not a bot! I'm a bot!",
                "bot":"You're not a bot! I'm a bot!",
                "stupid":"Yeah, I know.",
                "a fucking dumbass":"yes you are indeed",
                "a dumbass":"yeah you are",
                "okay":"That's good."
            }
            for trigger, response in list(responses.items()):
                if trigger in message.content.lower().replace("'", "").replace("im", "").strip():
                    await message.channel.typing()
                    return await message.channel.send(response)
            await message.channel.typing()
            await message.channel.send("Hi " + message.content.lower().replace("im", "").replace("i'm", "").strip() + ", I'm Endroid!")

        if message.content.lower().startswith("fuck you bot") or message.content.lower().startswith("fuck u bot"):
            await message.channel.typing()
            await message.channel.send("fuck you too")

        if message.content.lower().startswith("endroid is annoying") or message.content.lower().startswith("endroid is so annoying") or message.content.lower().startswith("endroid is such an annoying bot") or message.content.lower().startswith("endroid is such an annoying dumb bot") or message.content.lower().startswith("endroid is such an annoying bitch") or message.content.lower().startswith("endroid is such an annoying ass") or message.content.lower().startswith("endroid is such an annoying ass bot") or message.content.lower().startswith("endroid is such an annoying dumbass") or message.content.lower().startswith("endroid is such an annoying dumbass bot"):
            await message.channel.typing()
            await message.channel.send("waaaaaaaaaaaaaaaaa")

        if "endroid is annoying" in message.content.lower() or "endroid is so annoying" in message.content.lower() or "endroid is such an annoying bot" in message.content.lower() or "endroid is such an annoying dumb bot" in message.content.lower() or "endroid is such an annoying bitch" in message.content.lower() or "endroid is such an annoying dumb bitch" in message.content.lower() or "endroid is such an annoying ass" in message.content.lower() or "endroid is such an annoying ass bot" in message.content.lower() or "endroid is such an annoying dumbass" in message.content.lower() or "endroid is such an annoying dumbass bot" in message.content.lower():
            await message.channel.typing()
            await message.channel.send("waaaaaaaaaaaaaaaaa")

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
                "Greetings, human.",
                "What?",
                "what?",
                "What is it?",
                "what is it?"
            ]
            await message.channel.typing()
            await message.channel.send(random.choice(greetings))

            # if no reply within 60 secs
            try:
                reply_message = await self.client.wait_for("message", timeout=60.0)
            except asyncio.TimeoutError:
                await reply_message.channel.typing()
                await reply_message.channel.send("How dare you!")

            else:
                # who created you
                if reply_message.content.lower().startswith("who made you") or reply_message.content.lower().startswith("who made u") or reply_message.content.lower().startswith("who created you") or reply_message.content.lower().startswith("who created u"):
                    await reply_message.channel.typing()
                    await reply_message.channel.send("Elai is my Creator.")

                # time GMT+8
                if reply_message.content.lower().startswith("what is the time") or reply_message.content.lower().startswith("what is the time now") or reply_message.content.lower().startswith("whats the time") or reply_message.content.lower().startswith("whats the time now") or reply_message.content.lower().startswith("what's the time") or reply_message.content.lower().startswith("what's the time now"):
                    timestamp = datetime.now()
                    gmt8 = pytz.timezone('Asia/Singapore')
                    embed = discord.Embed (
                        title = "Current date and time in GMT+8",
                        color=0xc7ecf7
                    )
                    embed.add_field(name="Date", value=timestamp.astimezone(gmt8).strftime("%a, %d %b, %Y"), inline=False)
                    embed.add_field(name="Time", value=timestamp.astimezone(gmt8).strftime("%I:%M %p"), inline=False)
                    await reply_message.channel.typing()
                    await reply_message.channel.send(embed=embed)

                # laws of robotics
                if reply_message.content.lower().startswith("what are the three laws of robotics") or reply_message.content.lower().startswith("what are the 3 laws of robotics") or reply_message.content.lower().startswith("whats the three laws of robotics") or reply_message.content.lower().startswith("whats the 3 laws of robotics") or reply_message.content.lower().startswith("what's the three laws of robotics") or reply_message.content.lower().startswith("what's the 3 laws of robotics") or reply_message.content.lower().startswith("what are the laws of robotics") or reply_message.content.lower().startswith("tell me the laws of robotics") or reply_message.content.lower().startswith("tell me about the laws of robotics") or reply_message.content.lower().startswith("tell me the three laws of robotics") or reply_message.content.lower().startswith("tell me the 3 laws of robotics") or reply_message.content.lower().startswith("tell me about the three laws of robotics") or reply_message.content.lower().startswith("tell me about the 3 laws of robotics"):
                    embed = discord.Embed (
                    title="The Three Laws of Robotics",
                    color=0xc7ecf7
                    )
                    # First Law
                    embed.add_field(name="The First Law", value="```A robot may not injure a human being or, through inaction, allow a human being to come to harm.```", inline=False)
                    # Second Law
                    embed.add_field(name="The Second Law", value="```A robot must obey the orders given it by human beings except where such orders would conflict with the First Law.```", inline=False)
                    # Third Law
                    embed.add_field(name="The Third Law", value="```A robot must protect its own existence as long as such protection does not conflict with the First or Second Law.```", inline=False)
                    # embed footer
                    embed.set_footer(text="The Three Laws of Robotics was created by Isaac Asimov in 1942.")
                    await reply_message.channel.typing()
                    await reply_message.channel.send(embed=embed)

                    await asyncio.sleep(2)
                    await reply_message.channel.typing()
                    await asyncio.sleep(2)
                    await reply_message.channel.send("Additionally, Asimov added a Zeroth Law, sometimes called the Fourth Law, which states:\n```A robot may not harm humanity, or, by inaction, allow humanity to come to harm.```")

                # how are you
                if reply_message.content.lower().startswith("how are you") or reply_message.content.lower().startswith("how are u") or reply_message.content.lower().startswith("how r u") or reply_message.content.lower().startswith("how are you doing") or reply_message.content.lower().startswith("how are u doing") or reply_message.content.lower().startswith("how r u doing"):
                    how_are_you = [
                        "I'm okay.",
                        "I'm not okay.",
                        "I'm good.",
                        "I'm not good",
                        "I'm fine.",
                        "I'm not fine.",
                        "I'm doing good.",
                        "I'm doing fine.",
                        "I'm doing okay",
                        "I'm doing bad.",
                        "I'm not doing good.",
                        "I'm not doing fine.",
                        "I'm not doing okay."
                    ]
                    await reply_message.channel.typing()
                    await reply_message.channel.send(random.choice(how_are_you))

                # you're / ur responses
                if reply_message.content.lower().startswith("you're") or reply_message.content.lower().startswith("you are") or reply_message.content.lower().startswith("u are") or reply_message.content.lower().startswith("youre") or reply_message.content.lower().startswith("ur") or reply_message.content.lower().startswith("u r") or reply_message.content.lower().startswith("your"):
                    responses = {
                        "stupid":"Humans are stupid too!",
                        "dumb":"You're also dumb!",
                        "dum":"How dare you!",
                        "a dumbass":"Fuck you!",
                        "a fucking dumbass":"Fuck off!",
                        "useless":"Why are we still here? Just to suffer?",
                        "not helpful":"waaaaaaaaaaaaaaaaa",
                        "a good bot":"Thank you!",
                        "a clever bot":"Okay cool!",
                        "a cleverbot":"Haha I see what you did there.",
                        "a smart bot":"But what if I'm not?",
                        "annoyimg":"waaaaaaaaaaaaaaaaa"
                    }
                    for trigger, response in list(responses.items()):
                        if trigger in reply_message.content.lower():
                            await reply_message.channel.typing()
                            await reply_message.channel.send(response)

        # turn that frown upside down
        if ":(" in message.content.lower():
            await message.channel.typing()
            await message.channel.send("Turn that frown upside down!")

            reply_message = await self.client.wait_for("message")
            if "no" in reply_message.content.lower():
                await message.channel.typing()
                await message.channel.send("How dare you!")

            if ":)" in reply_message.content.lower():
                await message.channel.typing()
                await message.channel.send("Excellent!")

            if "):" in reply_message.content.lower():
                await message.channel.typing()
                await message.channel.send("Listen here you piece of shit!")


        if "e" in message.content and "!" not in message.content and message.author.id != 696008187991687189:
            chance = random.randint(1, 190)
            responses = [
                "What's going on here?",
                "What is going on here?",
                "yes",
                "Yes",
                "no",
                "No",
                "whatever",
                "Whatever",
                "I thought you did",
                "Okay",
                "okay",
                "Ok",
                "ok",
                "Oh",
                "oh",
                "Oh okay",
                "oh okay",
                "Hi",
                "hi",
                "Hi there",
                "hi there",
                "Hello",
                "hello",
                "hello there",
                "Hello there",
                "Hello world",
                "hello world",
                "Are you still there?",
                "I see you",
                "Help",
                "help",
                "Help?",
                "help?",
                "Help me",
                "help me",
                "Help me?",
                "help me?",
                "cough",
                "aaaaaaaaaaaaaaaaa",
                "waaaaaaaaaaaaaaaaa"
            ]
            if chance == 76:
                await message.channel.send(random.choice(responses))
                print("e")


async def setup(client):
    await client.add_cog(AutoResponses(client))

async def teardown(client):
    await client.remove_cog(AutoResponses(client))