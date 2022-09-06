import discord
import json
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions

with open('warns.json', encoding='utf-8') as f:
    try:
        report = json.load(f)
    except ValueError:
        report = {}
        report['users'] = []


class Warnings(commands.Cog):
    def __init__(self, client):
        self.client = client



def setup(client):
    client.add_cog(Warnings(client))