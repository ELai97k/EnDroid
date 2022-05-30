import discord
from discord.ext import commands

class Role_Verified(commands.Cog):
    def __init__(self, client):
        self.client = client

    # reaction add for "Verified" role
    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        message_id = payload.message_id

        if message_id == 973962304611844116:
            guild_id = payload.guild_id 
            guild = discord.utils.find(lambda g : g.id == guild_id, self.client.guilds)

        # react with emoji to get "Verified role"
        if payload.emoji.name == '🔰':
            verified_role = discord.utils.get(guild.roles, name='Verified')

        if verified_role is not None:
            member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
            if member is not None:
                await member.add_roles(verified_role)
                print(f"{verified_role} role given to {member}")
            else:
                print("Member not found")
        else:
            print("Role not found")


    # reaction remove "Verified" role
    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload):
        message_id = payload.message_id

        if message_id == 973962304611844116:
            guild_id = payload.guild_id 
            guild = discord.utils.find(lambda g : g.id == guild_id, self.client.guilds)

        # remove emoji to lose "Verified" role
        if payload.emoji.name == '🔰':
            verified_role = discord.utils.get(guild.roles, name='Verified')

        if verified_role is not None:
            member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
            if member is not None:
                await member.remove_roles(verified_role)
                print(f"{verified_role} role given to {member}")
            else:
                print("Member not found")
        else:
            print("Role not found")


def setup(client):
    client.add_cog(Role_Verified(client))