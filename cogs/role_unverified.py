import discord
from discord.ext import commands

class Role_Unverified(commands.Cog):
    def __init__(self, client):
        self.client = client

    # reaction add for "Unverified" role
    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        message_id = payload.message_id

        if message_id == 973962304611844116:
            guild_id = payload.guild_id 
            guild = discord.utils.find(lambda g : g.id == guild_id, self.client.guilds)

        # react with emoji to remove "Unverified" role
        if payload.emoji.name == '✅':
            unverified_role = discord.utils.get(guild.roles, name='Unverified')

        if unverified_role is not None:
            member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
            if member is not None:
                await member.remove_roles(unverified_role)
                print(f"{unverified_role} role removed from {member}")
            else:
                print("Member not found")
        else:
            print("Role not found")


    # reaction remove for "Unverified" role
    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload):
        message_id = payload.message_id
        if message_id == 973962304611844116:
            guild_id = payload.guild_id 
            guild = discord.utils.find(lambda g : g.id == guild_id, self.client.guilds)

        # remove emoji to gain back "Unverified" role
        if payload.emoji.name == '✅':
            unverified_role = discord.utils.get(guild.roles, name='Unverified')

        if unverified_role is not None:
            member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
            if member is not None:
                await member.add_roles(unverified_role)
                print(f"{unverified_role} role added to {member}")
            else:
                print("Member not found")
        else:
            print("Role not found")


def setup(client):
    client.add_cog(Role_Unverified(client))