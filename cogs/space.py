from discord.ext import commands
import random

class Space(commands.Cog):
    """Space cog."""
    def __init__(self, client):
        self.client = client

    @commands.command(help="SPAAACE!")
    async def space(self, ctx):
        if ctx.author == self.client.user:
            return
        if ctx.author.bot:
            return
        
        space = [
            "What's your favorite thing about space? Mine is space.",
            "Space.",
            "Gotta go to space. Lady. Lady.",
            "Oo. Oo. Oo. Lady. Oo. Lady. Oo. Let's go to space.",
            "Space going to space can't wait.",
            "Space. Trial. Puttin' the system on trial. In space. Space system. On trial. Guilty. Of being in space! Going to space jail!",
            "Dad! I'm in space!",
            "Space space wanna go to space yes please space. Space space. Go to space.",
            "Space space wanna go to space",
            "Space space going to space oh boy",
            "Ba! Ba! Ba ba ba! Space! Ba! Ba! Ba ba ba!",
            "Oh. Play it cool. Play it cool. Here come the space cops.",
            "Help me, space cops. Space cops, help.",
            "Going to space going there can't wait gotta go. Space. Going.",
            "Better buy a telescope. Wanna see me. Buy a telescope. Gonna be in space.",
            "Space. Space.",
            "I'm going to space.",
            "Oh boy.",
            "Yeah yeah yeah okay okay.",
            "Space. Space. Gonna go to space.",
            "Space. Space. Go to space.",
            "Yes. Please. Space.",
            "Ba! Ba! Ba ba ba! Space!",
            "Gonna be in space.",
            "Ohhhh, space.",
            "Wanna go to space. Space.",
            "Let's go - let's go to space. Let's go to space.",
            "I love space. Love space.",
            "Atmosphere. Black holes. Astronauts. Nebulas. Jupiter. The Big Dipper.",
            "Orbit. Space orbit. In my spacesuit.",
            "Space...",
            "Ohhh, the Sun. I'm gonna meet the Sun. Oh no! What'll I say? 'Hi! Hi, Sun!' Oh, boy!",
            "Look, an eclipse! No. Don't look.",
            "Come here, space. I have a secret for you. No, come closer.",
            "Space space wanna go to space",
            "Wanna go to -- wanna go to space",
            "Space wanna go wanna go to space wanna go to space",
            "I'm going to space.",
            "Space!",
            "Hey hey hey hey hey!",
            "Oh I know! I know I know I know I know I know - let's go to space!",
            "Oooh! Ooh! Hi hi hi hi hi. Where we going? Where we going? Hey. Lady. Where we going? Where we going? Let's go to space!",
            "Lady. I love space. I know! Spell it! S P... AACE. Space. Space.",
            "I love space.",
            "Hey lady. Lady. I'm the best. I'm the best at space.",
            "Oh oh oh oh. Wait wait. Wait I know. I know. I know wait. Space.",
            "Gotta go to space.",
            "Gonna be in space.",
            "Oh oh oh ohohohoh oh. Gotta go to space.",
            "Space. Space. Space. Space. Comets. Stars. Galaxies. Orion.",
            "Are we in space yet? What's the hold-up? Gotta go to space. Gotta go to SPACE.",
            "Going to space.",
            "Yeah, yeah, yeah, I'm going. Going to space.",
            "Love space. Need to go to space.",
            "Space space space. Going. Going there. Okay. I love you, space.",
            "So much space. Need to see it all.",
            "You are the farthest ever in space. Why me, space? Because you are the best. I'm the best at space? Yes.",
            "Space Court. For people in space. Judge space sun presiding. Bam. Guilty. Of being in space. I'm in space.",
            "Please go to space.",
            "Wanna go to space.",
            "Gotta go to space. Yeah. Gotta go to space.",
            "Hmmm. Hmmmmmm. Hmm. Hmmmmm. Space!",
            "Ohmygodohmygodohmygod! I'm in space!",
            "Space? SPACE!",
            "I'm in space.",
            "Where am I? Guess. Guess guess guess. I'm in space.",
            "There's a star. There's another one. Star. Star star star. Star.",
            "Getting bored of space.",
            "Bam! Bam bam bam! Take that, space.",
            "Are we in space?",
            "Oh oh oh. This is space! I'm in space!",
            "We made it we made it we made it. Space!",
            "Earth.",
            "Wanna go to earth.",
            "Wanna go to earth wanna go to earth wanna go to earth wanna go to earth. Wanna go to earth.",
            "Wanna go home.",
            "Wanna go home wanna go home wanna go home wanna go home.",
            "Earth earth earth.",
            "Don't like space. Don't like space.",
            "It's too big. Too big. Wanna go home. Wanna go to earth.",
            "SPAAACCCCCE!",
            "SPAAACE!",
            "YEEEHAAAAAW!",
            "Ah!"
        ]
        await ctx.send(f'{random.choice(space)}')


async def setup(client):
    await client.add_cog(Space(client))

async def teardown(client):
    await client.remove_cog(Space(client))