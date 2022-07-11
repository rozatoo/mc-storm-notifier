import discord
from discord.ext import commands
import asyncio
import logging
from dotenv import load_dotenv
import os
load_dotenv()



logger = logging.getLogger('discord')
logger.setLevel(logging.INFO)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

intents = discord.Intents.all()
intents.typing = False
intents.presences = False
intents.invites = False

bot = commands.Bot(
    command_prefix="!",
    intents=intents,
    allowed_mentions=discord.AllowedMentions(roles=False, users=True, everyone=True),
    )


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


for ext in extensions:
    bot.load_extension(f"cogs.{ext}")
    print(f'Loaded {ext}')



bot.run(os.getenv("DISCORD_TOKEN_MCSN"))