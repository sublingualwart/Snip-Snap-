import discord
import sqlite3
from discord.ext import commands

db = sqlite3.connect('./cogs/db/db/db.db')
cursor = db.cursor()


def get_channel(client, message):
    cursor.execute('SELECT channel FROM prefix WHERE guild_id=?', (message.guild.id,))
    channel = cursor.fetchone()
    canal = channel[0]
    return canal


class on_message_delete_event(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message_delete(self, message):
        canal = get_channel(self.client, message)
        canal = self.client.get_channel(int(canal))
        embed = discord.Embed(
            title="Deleted message",
            color=discord.Colour.random()
        )
        embed.add_field(name="Sended by: ", value=message.author)
        embed.add_field(name="Sended in: ", value=message.channel.mention)
        embed.add_field(name="Message: ", value=message.content)
        if canal == "None":
            pass
        else:
            await canal.send(embed=embed)


def setup(client):
    client.add_cog(on_message_delete_event(client))
