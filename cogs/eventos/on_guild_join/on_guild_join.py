import discord
import sqlite3
from discord.ext import commands

db = sqlite3.connect('./cogs/db/db/db.db')
cursor = db.cursor()


class on_guild_join_event(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        prefix = cursor.fetchall()
        for prefixo in prefix:
            print(prefixo)
        perms = discord.Permissions(send_messages=False, read_messages=True, connect=False, speak=False)
        await guild.create_role(name='Muted', permissions=perms)

        cursor.execute('INSERT INTO prefix(guild_id, prefix, channel) VALUES (?, ?, ?)', (guild.id, '!!', 'None'))
        db.commit()

def setup(client):
    client.add_cog(on_guild_join_event(client))
