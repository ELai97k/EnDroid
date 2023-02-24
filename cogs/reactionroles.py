import discord
from discord.ext import commands

class ReactionRoles(commands.Cog):
    """Reaction roles."""
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        guild_id = payload.guild_id 
        guild = discord.utils.find(lambda g : g.id == guild_id, self.client.guilds)
        member = discord.utils.get(guild.members, id=payload.user_id)

        # da rules add member role
        if payload.message_id == 921277460841111583:
            if str(payload.emoji) == "☑️":
                member_role = discord.utils.get(payload.member.guild.roles, name="Member")
            else:
                member_role = discord.utils.get(guild.roles, name=payload.emoji)

            if member is not None:
                print(f"User: {member}, checked.")

            if member_role is not None:
                print(f"Role: {member_role}, checked.")
                await payload.member.add_roles(member_role)
                print(f"{member_role} role added to {member}")

        # get verified add role
        if payload.message_id == 1078645716148293632:
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

            if member is not None:
                print(f"User: {member}, checked.")

            if verified_role is not None:
                print(f"Role: {verified_role}, checked.")
                # add Verified role
                await payload.member.add_roles(verified_role)
                print(f"{verified_role} role added to {member}")

            if unverified_role is not None:
                print(f"Role: {unverified_role}, checked.")
                # remove Unverified role
                await payload.member.remove_roles(unverified_role)
                print(f"{unverified_role} role removed from {member}")

        # announcements add role
        if payload.message_id == 1078645775166349312:
            if str(payload.emoji) == "📢":
                announcements = discord.utils.get(guild.roles, name='announcements')
            else:
                announcements = discord.utils.get(guild.roles, name=payload.emoji)

            if member is not None:
                print(f"User: {member}, checked.")

            if announcements is not None:
                print(f"Role: {announcements}, checked.")
                await payload.member.add_roles(announcements)
                print(f"{announcements} role added to {member}")

        # voter role add
        if payload.message_id == 1078645775166349312:
            if str(payload.emoji) == "🧡":
                voter = discord.utils.get(guild.roles, name='Voter')
            else:
                voter = discord.utils.get(guild.roles, name=payload.emoji)

            if member is not None:
                print(f"User: {member}, checked.")

            if voter is not None:
                print(f"Role: {voter}, checked.")
                await payload.member.add_roles(voter)
                print(f"{voter} role added to {member}")

    
    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload):
        guild_id = payload.guild_id 
        guild = discord.utils.find(lambda g : g.id == guild_id, self.client.guilds)
        member = discord.utils.get(guild.members, id=payload.user_id)

        # da rules remove member role
        if payload.message_id == 921277460841111583:
            if str(payload.emoji) == "☑️":
                member_role = discord.utils.get(guild.roles, name='Member')
            else:
                member_role = discord.utils.get(guild.roles, name=payload.emoji)

            if member is not None:
                print(f"User: {member}, checked.")

            if member_role is not None:
                print(f"Role: {member_role}, checked.")
                await member.remove_roles(member_role)
                print(f"{member_role} role removed from {member}")

        # get verified remove role
        if payload.message_id == 1078645716148293632:
            if str(payload.emoji) == "✅":
                unverified_role = discord.utils.get(guild.roles, name='Unverified')
                verified_role = discord.utils.get(guild.roles, name="Verified")
            else:
                unverified_role = discord.utils.get(guild.roles, name=payload.emoji)
                verified_role = discord.utils.get(guild.roles, name=payload.emoji)

            if member is not None:
                print(f"User: {member}, checked.")

            if unverified_role is not None:
                print(f"Role: {unverified_role}, checked.")
                await member.add_roles(unverified_role)
                print(f"{unverified_role} role added to {member}")

            if verified_role is not None:
                print(f"Role: {verified_role}, checked.")
                await member.remove_roles(verified_role)
                print(f"{verified_role} role removed from {member}")

        # announcements remove role
        if payload.message_id == 1078645775166349312:
            if str(payload.emoji) == "📢":
                announcements = discord.utils.get(guild.roles, name='announcements')
            else:
                announcements = discord.utils.get(guild.roles, name=payload.emoji)

            if member is not None:
                print(f"User: {member}, checked.")

            if announcements is not None:
                print(f"Role: {announcements}, checked.")
                await member.remove_roles(announcements)
                print(f"{announcements} role removed from {member}")

        # voter role remove
        if payload.message_id == 1078645775166349312:
            if str(payload.emoji) == "🧡":
                voter = discord.utils.get(guild.roles, name='Voter')
            else:
                voter = discord.utils.get(guild.roles, name=payload.emoji)

            if member is not None:
                print(f"User: {member}, checked.")

            if voter is not None:
                print(f"Role: {voter}, checked.")
                await member.remove_roles(voter)
                print(f"{voter} role removed from {member}")


def setup(client):
    client.add_cog(ReactionRoles(client))

def teardown(client):
    client.remove_cog(ReactionRoles(client))