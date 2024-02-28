import discord
from discord.ext import commands

class Facts(commands.Cog):
    """Useless facts."""
    def __init__(self, client):
        self.client = client

    @commands.command(help="Some random useless facts.")
    async def fact(self, ctx):
        if ctx.author == self.client.user:
            return
        if ctx.author.bot:
            return
        
        facts = [
            "Rubber bands last longer when refrigerated.",
            "Movie trailers got their name because they were originally shown after the movie.",
            "The real name of Monopoly mascot Uncle Pennybags is Milburn Pennybags.",
            "Women blink nearly twice as much as men.",
            "Pogonophobia is the fear of beards.",
            "Oreo has made enough cookies to span five back and forth trips to the moon.",
            "Salt used to be a currency.",
            "Your fingernails grow faster on your dominant hand.",
            "Sloths can hold their breath for longer than dolphins.",
            "A giraffe can go longer without water than a camel can.",
            "A dragonfly has a lifespan of only 24 hours.",
            "The average adult spends more time on the toilet than they do exercising.",
            "Honey is the only food that does not spoil.",
            "Four out of five children recognise the Mcdonald's logo at three years old.",
            "One single teaspoon of honey represents the life work of 12 bees.",
            "It's impossible to tickle yourself.",
            "Queen Elizabeth II is a trained mechanic.",
            "Cap'n Crunch's full name is Captain Horatio Magellan Crunch.",
            "Venus is the only planet that rotates clockwise.",
            "Dolphins give each other names.",
            "One man set a world record by putting on 260 T-shirts at once.",
            "There is a metallic asteroid shaped like a dog bone named “Kleopatra.”",
            "A “jiffy” is about one trillionth of a second.",
            "The cigarette lighter was invented before the match.",
            "Dragonflies have six legs but can't walk.",
            "Mulan has the highest kill-count of any Disney character.",
            "3.6 cans of Spam are consumed each second.",
            "Most pandas in the world are on loan from China.",
            "A snail can sleep for three years.",
            "3.6 cans of Spam are consumed each second.",
            "Right handed people, on average, live nine years longer than left handed people.",
            "“Go” is the shortest complete sentence in the English language.",
            "Only one person in two billion will live to be 116 or older.",
            "A crocodile cannot stick its tongue out.",
            "Punctuation wasn't always a part of our written language.",
            "Alaska is the only state whose name is on one row on a keyboard.",
            "There are 32 muscles in a cat's ear.",
            "The King of Hearts is the only king in a deck of cards without a mustache.",
            "Animals that lay eggs don't have belly buttons.",
            "The King of Hearts is the only king in a deck of cards without a mustache."
        ]


async def setup(client):
    await client.add_cog(Facts(client))

async def teardown(client):
    await client.remove_cog(Facts(client))