import discord
import sqlite3
import datetime
from discord.ext import commands

db = sqlite3.connect('./cogs/db/db/db.db')
cursor = db.cursor()

timing = datetime.datetime.now()


class setsnipe_cmd(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(
        name='setsnipe',
        description='Define channel of the send deleted and edited messages.',
        usage="<Channel Mention>"
    )
    @commands.has_permissions(administrator=True)
    async def setsnipe(self, ctx, channel: discord.TextChannel):
        cursor.execute('UPDATE prefix SET channel=? WHERE guild_id=?', (channel.id, ctx.guild.id))
        db.commit()
        embed = discord.Embed(
            title="Defined snipe",
            description=f"The snipe channel has been set to ``{channel.name}``",
            color=discord.Colour.random()
        )
        embed.set_footer(text=f'{ctx.author}', icon_url=ctx.author.avatar_url)
        embed.timestamp = timing
        await ctx.send(embed=embed)

    @setsnipe.error
    async def setsnipe_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(f"Hey {ctx.author.mention}, you don't have permissions to execute this command!")
        raise error
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(f'Hey {ctx.author.mention}, you do not type all the necessary parameters')
        raise error


def setup(client):
    client.add_cog(setsnipe_cmd(client))
