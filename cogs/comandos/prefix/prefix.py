import discord
import sqlite3
import datetime
from discord.ext import commands

db = sqlite3.connect('./cogs/db/db/db.db')
cursor = db.cursor()

timing = datetime.datetime.now()


class prefix_cmd(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(
        aliases=["setprefix"],
        description="Change the prefix of the bot.",
        usage="<New Prefix>"
    )
    @commands.has_permissions(administrator=True)
    async def prefix(self, ctx, prefixo):
        cursor.execute('UPDATE prefix SET prefix=? WHERE guild_id=?', (prefixo, ctx.guild.id))
        db.commit()
        embed = discord.Embed(
            title="New prefix",
            description=f"Prefix changed to ``{prefixo}``",
            color=discord.Colour.random()
        )
        embed.set_footer(text=f'{ctx.author}', icon_url=ctx.author.avatar_url)
        embed.timestamp = timing
        await ctx.send(embed=embed)

    @prefix.error
    async def prefix_error(self, ctx, error):
        if isinstance(error, commands.BotMissingPermissions):
            await ctx.send(f"Hey {ctx.author.mention}, i don't have permissions to execute this command!")
        raise error
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(f"Hey {ctx.author.mention}, you don't have permissions to execute this command!")
        raise error
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(f'Hey {ctx.author.mention}, you do not type all the necessary parameters')
        raise error


def setup(client):
    client.add_cog(prefix_cmd(client))
