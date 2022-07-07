import discord
from discord.ext import commands
import aiosqlite
import asyncio
import logging
from dotenv import load_dotenv
import os
load_dotenv()

import utils.dbsetup


handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')

intents = discord.Intents.all()
intents.typing = False
intents.presences = False
intents.invites = False

bot = commands.Bot(
    command_prefix="!",
    intents=intents,
    allowed_mentions=discord.AllowedMentions(roles=False, users=True, everyone=True),
    )


loop = asyncio.get_event_loop()
bot.db = loop.run_until_complete(aiosqlite.connect('database.db'))
bot.currentlyThundering = False
bot.doScrape = True
bot.errorCH = 994483840087248906


extensions = (
    "commands",
    "scraper"
    )

@bot.event
async def on_ready():
    await bot.wait_until_ready()
    print('--------------------------')
    print(f'Logged in as: {bot.user.name}')
    print(f'With ID: {bot.user.id}')
    print(f"Servers - {str(len(bot.guilds))}")
    print('--------------------------')
    print('Bot is ready!')


async def main():
    #Setup the DB if it hasn't been done already
    await utils.dbsetup.setup(bot)
    #Load extensions
    for ext in extensions:
        await bot.load_extension(f"cogs.{ext}")
        print(f'Loaded {ext}')
    

    # start the client
    async with bot:
        await bot.start(os.getenv("DISCORD_TOKEN_MCSN"))

asyncio.run(main())