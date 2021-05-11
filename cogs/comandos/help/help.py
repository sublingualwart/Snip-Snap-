import datetime
import DiscordUtils
import discord
from discord.ext import commands

timing = datetime.datetime.now()


class help_cmd(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(
        aliases=["helpme"],
        description="Send a message containing all of my commands and functions."
    )
    async def help(self, ctx):
        mencinoe_razao = "<User Mention> [Reason]"
        mencione = "<User Mention>"
        mencione_opt = "[User Mention]"
        embeds = []
        embed = discord.Embed(
            title="Help Center",
            description="<> = Required\n[] = Optional",
            color=discord.Colour.random()
        )
        embed.add_field(name=f'!!mute {mencinoe_razao}', value='Mute the mencioned user.', inline=False)
        embed.add_field(name=f'!!unmute {mencinoe_razao}', value='Unmute the mencioned user', inline=False)
        embed.add_field(name=f'!!ban {mencinoe_razao}', value='Ban the mencioned user.', inline=False)
        embed.add_field(name=f'!!unban <User ID> [Reason]', value='Unban the mencioned user.', inline=False)
        embed.add_field(name='!!prefix <New Prefix>', value='Change the prefix of the bot', inline=False)
        embed.set_footer(text=f'{ctx.author}', icon_url=ctx.author.avatar_url)
        timing = datetime.datetime.now()
        embed.timestamp = timing

        embed2 = discord.Embed(
            title="Central de Ajuda",
            description="<>, obrigatório\n[] = opcional",
            color=discord.Colour.random()
        )
        embed2.add_field(name=f'!!userinfo {mencione_opt}', value='Display information of the mencioned user.',
                         inline=False)
        embed2.add_field(name=f'!!avatar {mencione_opt}', value='Display avatar of the mencioned user.', inline=False)
        embed2.add_field(name='!!setsnipe <Channel Mention>',
                         value='Define channel of the send deleted and edited messages.', inline=False)
        embed2.add_field(name=f'!!help', value='Display this message.', inline=False)
        embed2.set_footer(text=f'{ctx.author}', icon_url=ctx.author.avatar_url)
        embed2.timestamp = timing

        embeds.append(embed)
        embeds.append(embed2)

        paginator = DiscordUtils.Pagination.CustomEmbedPaginator(ctx=ctx, timeout=60, auto_footer=True,
                                                                 remove_reactions=ctx.channel.permissions_for(
                                                                     ctx.me).manage_messages)
        paginator.add_reaction('⏮️', 'first')
        paginator.add_reaction('⏪', 'back');
        paginator.add_reaction('🔐', 'lock')
        paginator.add_reaction('⏩', 'next')
        paginator.add_reaction('⏭️', 'last')

        await paginator.run(embeds)


def setup(client):
    client.add_cog(help_cmd(client))
