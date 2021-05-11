import discord
import datetime
from discord.ext import commands

timing = datetime.datetime.now()


class unban_cmd(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(
        name="unban",
        description="Ban the mencioned user.",
        usage="<User ID> [Reason]"
    )
    @commands.has_permissions(ban_members=True)
    @commands.bot_has_permissions(ban_members=True)
    async def unban(self, ctx, usuario: int, *, motivo='None'):
        try:
            user = await self.client.fetch_user(usuario)
            await ctx.guild.unban(user, reason=motivo)
            embed = discord.Embed(
                title="Unban",
                description=f'{user.mention} has been successfully unbanned\nReason: {motivo}',
                color=discord.Colour.random()
            )
            embed.set_footer(text=f'{ctx.author}', icon_url=ctx.author.avatar_url)
            embed.timestamp = timing
            await ctx.send(embed=embed)
        except Exception as err:
            if isinstance(err, discord.NotFound):
                await ctx.send(f'Hey {ctx.author.mention}, this user is not banned!')
            raise err

    @unban.error
    async def unban_error(self, ctx, error):
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
    client.add_cog(unban_cmd(client))
