import discord
import datetime
from discord.ext import commands

timing = datetime.datetime.now()


class userinfo_cmd(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(
        aliases=["ui", "info"],
        description="Display this message.",
        usage="[User Mention]"
    )
    async def userinfo(self, ctx, usuario: discord.Member = None):
        if usuario is None:
            usuario = ctx.author
        status = {
            'online': 'Online',
            'dnd': 'Do not Disturb',
            'idle': 'Idle',
            'offline': 'Offline'
        }
        days = {
            'January': '01',
            'February': '02',
            'March': '03',
            'April': '04',
            'May': '05',
            'June': '06',
            'July': '07',
            'August': '08',
            'September': '09',
            'October': '10',
            'November': '11',
            'December': '12',
        }
        am_pm = {
            'AM': 'AM',
            'PM': 'PM'
        }

        mes = days[str((usuario.joined_at.strftime("%B")))]
        am_pm = am_pm[str((usuario.joined_at.strftime("%p")))]
        role = []
        for roles in usuario.roles:
            if roles.name == "@everyone":
                pass
            else:
                role.append(roles.name)
        if len(role) == 0:
            role.append("None")
        embed = discord.Embed(
            title=f'{usuario.name}',
            colour=discord.Colour.random()
        )
        format = f"%d/{mes}/%Y às %H:%M:%S {am_pm}"
        embed.add_field(name="Nickname: ", value=usuario)
        embed.add_field(name="ID: ", value=usuario.id)
        embed.add_field(name="Roles: ", value="".join(role))
        embed.add_field(name="Status:", value=status[str(usuario.status)])
        embed.add_field(name="Created at: ",
                        value=usuario.created_at.strftime(format))
        embed.add_field(name="Joined at: ", value=usuario.joined_at.strftime(format))
        embed.set_thumbnail(url=usuario.avatar_url)
        embed.set_footer(text=f'{ctx.author}', icon_url=ctx.author.avatar_url)
        embed.timestamp = timing
        await ctx.send(embed=embed)

    @userinfo.error
    async def userinfo_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(f'Hey {ctx.author.mention}, you do not type all the necessary parameters')
        raise error


def setup(client):
    client.add_cog(userinfo_cmd(client))
