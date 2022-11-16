from discord.ext import tasks
from discord.ext import commands
import time
from utils import get_or_fetch_channel
import aiohttp
import os

class Scraper(commands.Cog, command_attrs=dict(hidden=False)):
    def __init__(self, bot):
        self.bot = bot 
        self.scrape.start()

    @tasks.loop(seconds=float(os.getenv("REPEAT_TIME")))
    async def scrape(self):
        if self.bot.doScrape is True:
            async with aiohttp.ClientSession() as session:
                async with session.get('http://142.202.220.236:8123/up/world/world/1') as resp:
                    data = await resp.json(content_type=None)
                    ch = await get_or_fetch_channel(self, os.getenv("ERROR_CH"))
                    if data['isThundering'] == data['hasStorm'] == True:
                        if self.bot.currentlyThundering is False:
                            await ch.send(f"@everyone a thunderstorm started <t:{int(time.time())}:R>")
                            self.bot.currentlyThundering = True
                    else:
                        if self.bot.currentlyThundering is True:
                            await ch.send("The thunderstorm has stopped...")
                            self.bot.currentlyThundering = False

                    errorCH = await get_or_fetch_channel(self, self.bot.errorCH)
                    await errorCH.send(f"last updated <t:{int(time.time())}:R>\nCurrently Thundering: {self.bot.currentlyThundering}", delete_after=float(os.getenv("REPEAT_TIME")))
                    print("Bot is running")


    @scrape.before_loop
    async def wait(self):
        await self.bot.wait_until_ready()


async def setup(bot):
	await bot.add_cog(Scraper(bot)) 
