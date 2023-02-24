import discord
from discord.ext import commands

class ReactionRoles(commands.Cog):
    """Reaction roles."""
    def __init__(self, client):
        self.client = client

    # reaction add
    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        guild_id = payload.guild_id 
        guild = discord.utils.find(lambda g : g.id == guild_id, self.client.guilds)
        member = discord.utils.get(guild.members, id=payload.user_id)

        if payload.message_id == 1078563481101553824: # get verified
            if str(payload.emoji) == "✅":
                # Verified role
                verified_role = discord.utils.get(payload.member.guild.roles, name="Verified")
                # Unerified role
                unverified_role = discord.utils.get(payload.member.guild.roles, name="Unverified")

            else:
                # Verified role
                verified_role = discord.utils.get(guild.roles, name=payload.emoji)
                # Unerified role
                unverified_role = discord.utils.get(guild.roles, name=payload.emoji)

            if verified_role is not None:
                # add Verified role
                await payload.member.add_roles(verified_role)
                print(f"{verified_role} role added to {member}")

            if unverified_role is not None:
                # remove Unverified role
                await payload.member.remove_roles(unverified_role)
                print(f"{unverified_role} role removed from {member}")


    # reaction remove
    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload):
        guild_id = payload.guild_id 
        guild = discord.utils.find(lambda g : g.id == guild_id, self.client.guilds)
        member = discord.utils.get(guild.members, id=payload.user_id)

        if payload.message_id == 1078563481101553824: # get verified
            if str(payload.emoji) == "✅":
                unverified_role = discord.utils.get(guild.roles, name='Unverified')
                verified_role = discord.utils.get(guild.roles, name="Verified")
            else:
                unverified_role = discord.utils.get(guild.roles, name=payload.emoji)
                verified_role = discord.utils.get(guild.roles, name=payload.emoji)

            if unverified_role is not None:
                await member.add_roles(unverified_role)
                print(f"{unverified_role} role added to {member}")

            if verified_role is not None:
                await member.remove_roles(verified_role)
                print(f"{verified_role} role removed from {member}")


def setup(client):
    client.add_cog(ReactionRoles(client))

def teardown(client):
    client.remove_cog(ReactionRoles(client))