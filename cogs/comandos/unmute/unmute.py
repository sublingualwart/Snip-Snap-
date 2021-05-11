import discord
import datetime
from discord.ext import commands

timing = datetime.datetime.now()


class unmute_cmd(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(
        name="unmute",
        description="Mute the mencioned user.",
        usage="<User Mention> [Reason]"
    )
    @commands.has_permissions(manage_roles=True)
    @commands.bot_has_permissions(manage_roles=True)
    async def unmute(self, ctx, usuario: discord.Member, *, motivo='None'):
        guild = ctx.guild
        role = discord.utils.get(guild.roles, name="Muted")
        if role not in usuario.roles:
            await ctx.send(f'Hey {ctx.author.mention}, this user not is muted!')
        else:
            await usuario.remove_roles(role, reason=motivo)
            for canais in guild.channels:
                permissoes = {
                    role: discord.PermissionOverwrite(send_messages=True, connect=True, speak=True)
                }
                await canais.edit(overwrites=permissoes)
            embed = discord.Embed(
                title="Unmute",
                description=f'{usuario} has been successfully unmuted\nReason: {motivo}',
                color=discord.Colour.random()
            )
            embed.set_footer(text=f'{ctx.author}', icon_url=ctx.author.avatar_url)
            embed.timestamp = timing
            await ctx.send(embed=embed)

    @unmute.error
    async def unmute_error(self, ctx, error):
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
    client.add_cog(unmute_cmd(client))
