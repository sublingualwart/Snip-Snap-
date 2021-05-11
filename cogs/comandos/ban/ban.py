import discord
import datetime
from discord.ext import commands

timing = datetime.datetime.now()


class ban_cmd(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(
        name="ban",
        description="Ban the mencioned user.",
        usage="<User Mention> [Reason]"
    )
    @commands.has_permissions(ban_members=True)
    @commands.bot_has_permissions(ban_members=True)
    async def ban(self, ctx, usuario: discord.Member, *, motivo='None'):
        await usuario.ban(reason=motivo)
        embed = discord.Embed(
            title="Ban",
            description=f'{usuario} has been successfully banned\nReason: {motivo}',
            color=discord.Colour.random()
        )
        embed.set_footer(text=f'{ctx.author}', icon_url=ctx.author.avatar_url)
        embed.timestamp = timing
        await ctx.send(embed=embed)
        await ctx.send(f'**User ID: {usuario.id}**')

    @ban.error
    async def ban_error(self, ctx, error):
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
    client.add_cog(ban_cmd(client))
