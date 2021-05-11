import discord
import os
import sqlite3
from data import data
from discord.ext import commands, tasks
from itertools import cycle

db = sqlite3.connect('cogs/db/db/db.db')
cursor = db.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS prefix(guild_id INTEGER, prefix TEXT, channel TEXT)')


def get_db(client, message):
    cursor.execute('SELECT prefix FROM prefix WHERE guild_id=?', (message.guild.id,))
    prefixes = cursor.fetchone()
    prefix = prefixes[0]
    return prefix


client = commands.Bot(command_prefix=get_db, intents=discord.Intents.all())


class Bot(discord.Client):
    @client.event
    async def on_ready():
        print(f'Online como: {client.user}')

        def load(cog_name):
            for filename in os.listdir(f'./cogs/comandos/{cog_name}'):
                if filename.endswith(".py"):
                    try:
                        client.load_extension(f'cogs.comandos.{cog_name}.{filename[:-3]}')
                    except Exception as err:
                        print(err)

        def db_load(db_name):
            for filename in os.listdir(f'./cogs/db/db'):
                if filename.endswith(".py"):
                    try:
                        client.load_extension(f'cogs.db.db.{filename[:-3]}')
                    except Exception as err:
                        print(err)

        def events(event_name):
            for filename in os.listdir(f'./cogs/eventos/{event_name}'):
                if filename.endswith(".py"):
                    try:
                        client.load_extension(f'cogs.eventos.{event_name}.{filename[:-3]}')
                    except Exception as err:
                        print(err)

        for filename in os.listdir('./cogs/comandos'):
            load(filename)
        for filename in os.listdir('./cogs/db'):
            db_load(filename)
        for filename in os.listdir('./cogs/eventos'):
            events(filename)

        alternar = cycle(["I'm was created by NemRela#6044!", "My default prefix is !!"])
        @tasks.loop(seconds=5)
        async def task():
            await client.change_presence(status=discord.Status.online,
                                         activity=discord.Activity(type=discord.ActivityType.playing,
                                                                   name=next(alternar)))
        task.start()
        client.loop.create_task(task())
client.remove_command("help")
client.run(data.token)
