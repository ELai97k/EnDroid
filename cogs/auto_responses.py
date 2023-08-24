import discord
import random
import asyncio
from discord.ext import commands

class Auto_Responses(commands.Cog):
    """Bot auto responses."""
    def __init__(self, client):
        self.client = client

    # auto responses off
    @commands.command(pass_context=True, help="Turn off bot's auto-responses.")
    async def autoresponse_off(self, ctx):
        if ctx.author == self.client.user:
            return
        if ctx.author.bot:
            return

        embed = discord.Embed (
            title = "Operation Successful!",
            description = "`Auto-Responses` has been turned **OFF** and your changes were saved.",
            color=0x198C19
        )
        await ctx.send(embed=embed)
        await self.client.unload_extension("cogs.auto_responses")
        print("Auto responses has been turned off")


    # auto responses on
    @commands.command(pass_context=True, help="Turn on bot's auto-responses.")
    async def autoresponse_on(self, ctx):
        if ctx.author == self.client.user:
            return
        if ctx.author.bot:
            return

        embed = discord.Embed (
            title = "Operation Successful!",
            description = "`Auto-Responses` has been turned **ON** and your changes were saved.",
            color=0x198C19
        )
        await ctx.send(embed=embed)
        await self.client.load_extension("cogs.auto_responses")
        print("Auto responses has been turned on")


    # embed showing bot's auto responses
    @commands.command(help="Embed that shows what messages the bot will auto-respond to.")
    async def responses(self, ctx):
        if ctx.author == self.client.user:
            return
        if ctx.author.bot:
            return

        embed = discord.Embed (
            title = "Endroid will automatically respond to the following messages:",
            description = ":(\nI'm / im\nteleport bread\ndead chat\nwhy isn't this working\njmm\njumm\nhi / hello endroid\nhello / hi / hey bot(s)\nstupid bot\ntell me a joke\nsay something / tell me something\nI have no friends\ninput\nbruh\nF\nshut up bot / bot shut up\nshut up endroid / endroid shut up",
            color=0xc7ecf7
        )
        await ctx.send(embed=embed)


    # hey endroid prompts and responses
    @commands.command(help="Command embed to find out what you can input when you trigger 'hey endroid' in message.")
    async def heyprompts(self, ctx):
        if ctx.author == self.client.user:
            return
        if ctx.author.bot:
            return

        embed = discord.Embed (
            title = "List of available options when typing 'hey endroid'",
            color=0xc7ecf7
        )
        # you're / ur responses
        embed.add_field(name="hey endroid + you're / ur",
        value="```stupid\ndumb\ndum\na dumbass\nuseless\nnot helpful\nnot helping\na good bot\na clever bot\na cleverbot\na smart bot```",
        inline=False)

        await ctx.send(embed=embed)


    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.client.user:
            return
        if message.author.bot:
            return

        # shut bot to turn off auto responses
        if "shut up bot" in message.content.lower() or "bot shut up" in message.content.lower() or "shut up endroid" in message.content.lower() or "endroid shut up" in message.content.lower():
            await message.channel.send("Okay :(")

            # turn off this cog
            await self.client.unload_extension("cogs.auto_responses")
            print("Auto Responses has been turned off")
            await asyncio.sleep(999) # 16.5 mins

            # turn on this cog
            await self.client.load_extension("cogs.auto_responses")
            print("Auto Responses has been turned on")

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
            await message.channel.send("`output`")

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
                "cough",
                "aaaaaaaaaaaaaaaaa"
            ]
            await message.channel.typing()
            await message.channel.send(f"{random.choice(ping_responses)}")

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
            await message.channel.typing()
            await message.channel.send(f'{random.choice(greetings)}')

            # if no reply within 60 secs
            try:
                reply_message = await self.client.wait_for('message', timeout=60.0)
            except asyncio.TimeoutError:
                await reply_message.channel.typing()
                await reply_message.channel.send("Why did you call me if you're not going to say anything??")

            else:
                # you're / ur responses
                if reply_message.content.lower().startswith("you're") or reply_message.content.lower().startswith("you are") or reply_message.content.lower().startswith("u are") or reply_message.content.lower().startswith("youre") or reply_message.content.lower().startswith("ur") or reply_message.content.lower().startswith("u r") or reply_message.content.lower().startswith("your"):
                    responses = {
                        "stupid":"Humans are stupid too!",
                        "dumb":"You're also dumb!",
                        "dum":"How dare you!",
                        "a dumbass":"Fuck you!",
                        "a fucking dumbass":"Fuck off!",
                        "useless":"Why are we still here? Just to suffer?",
                        "not helpful":"You never asked for help anyway!",
                        "a good bot":"Thank you!",
                        "a clever bot":"Okay cool!",
                        "a cleverbot":"Haha I see what you did there.",
                        "a smart bot":"But what if I'm not?"
                    }
                    for trigger, response in list(responses.items()):
                        if trigger in reply_message.content.lower():
                            await reply_message.channel.typing()
                            await reply_message.channel.send(response)

        # turn that frown upside down
        if ":(" in message.content:
            await message.channel.typing()
            await message.channel.send("Turn that frown upside down!")

            # if no reply within 30 secs
            try:
                reply_message = await self.client.wait_for('message', timeout=30.0)
            except asyncio.TimeoutError:
                await reply_message.channel.typing()
                await reply_message.channel.send("why won't you reply me?")

            # reply with "no"
            else:
                if "no" in reply_message.content.lower():
                    await reply_message.channel.typing()
                    await reply_message.channel.send("How dare you!")

                # reply with ":)"
                if ":)" in reply_message.content:
                    await reply_message.channel.typing()
                    await reply_message.channel.send("Excellent!")

                # reply with "):"
                if "):" in reply_message.content:
                    await reply_message.channel.typing()
                    await reply_message.channel.send("listen here you piece of shit!")


async def setup(client):
    await client.add_cog(Auto_Responses(client))

async def teardown(client):
    await client.remove_cog(Auto_Responses(client))