import discord
from discord.ext import commands

class ReactionRoles(commands.Cog):
    """Reaction roles."""
    def __init__(self, client):
        self.client = client
    
    # reaction add to get "Verified" role
    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        message_id = payload.message_id

        if message_id == 1007914062560108555:
            guild_id = payload.guild_id 
            guild = discord.utils.find(lambda g : g.id == guild_id, self.client.guilds)

        if payload.emoji.name == '✅':
            verified_role = discord.utils.get(guild.roles, name='Verified')
            unverified_role = discord.utils.get(guild.roles, name='Unverified')
        
        # react to get "Verified" role
        if verified_role is not None:
            member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
            if member is not None:
                await member.add_roles(verified_role)
                print(f"{verified_role} role given to {member}")
            else:
                print("Member not found")
        else:
            print("Role not found")

        # react to remove "Unverified" role
        if unverified_role is not None:
            member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
            if member is not None:
                await member.remove_roles(unverified_role)
                print(f"{unverified_role} role removed from {member}")
            else:
                print("Member not found")
        else:
            print("Role not found")


    # reaction remove to lose "Verified" role
    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload):
        message_id = payload.message_id

        if message_id == 1007914062560108555:
            guild_id = payload.guild_id
            guild = discord.utils.find(lambda g : g.id == guild_id, self.client.guilds)

        if payload.emoji.name == '✅':
            verified_role = discord.utils.get(guild.roles, name='Verified')
            unverified_role = discord.utils.get(guild.roles, name='Unverified')

        # react to remove "Verified" role
        if verified_role is not None:
            member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
            if member is not None:
                await member.remove_roles(verified_role)
                print(f"{verified_role} role removed from {member}")
            else:
                print("Member not found")
        else:
            print("Role not found")

        # react to get "Unverified" role
        if unverified_role is not None:
            member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
            if member is not None:
                await member.add_roles(unverified_role)
                print(f"{unverified_role} role given to {member}")
            else:
                print("Member not found")
        else:
            print("Role not found")


def setup(client):
    client.add_cog(ReactionRoles(client))