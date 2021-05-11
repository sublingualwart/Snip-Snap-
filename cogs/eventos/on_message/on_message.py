import discord
import sqlite3
from discord.ext import commands

db = sqlite3.connect('./cogs/db/db/db.db')
cursor = db.cursor()


def get_db(client, message):
    cursor.execute('SELECT prefix FROM prefix WHERE guild_id=?', (message.guild.id,))
    prefixes = cursor.fetchone()
    prefix = prefixes[0]
    return prefix


class on_message_event(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):
        id = self.client.user.id
        if message.content == f'<@!{id}>':
            await message.channel.send(
                f'{message.author.mention}, my prefix is ``{get_db(self.client, message)}`` ')


def setup(client):
    client.add_cog(on_message_event(client))
