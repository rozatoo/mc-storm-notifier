from discord.ext import tasks
from discord.ext import commands
from arsenic import browsers, services
import arsenic
import time
import random
import asyncio

class Scraper(commands.Cog, command_attrs=dict(hidden=False)):
    def __init__(self, bot):
        self.bot = bot 
        self.scrape.start()

    @tasks.loop(seconds=30.0)
    async def scrape(self):
        if self.bot.doScrape is True:
            start = time.time()
            service = services.Chromedriver(
                binary='C:\\chromedriver\\chromedriver.exe'
            )
            browser = browsers.Chrome()
            browser.capabilities = {
                "goog:chromeOptions": {"args": ["--headless", "--disable-gpu"]}
            }
            
            async with arsenic.get_session(service, browser) as session:
                await session.get("https://ultravanilla.world")
                src = await session.get_page_source()
                ch = self.bot.get_channel(994478862362759188)
                if (("thunder_day" or "thunder_night") in src):
                    if self.bot.currentlyThundering is False:
                        await ch.send(f"@everyone a thunderstorm started <t:{int(time.time())}:R>")
                        self.bot.currentlyThundering = True
                else:
                    if self.bot.currentlyThundering is True:
                        await ch.send("The thunderstorm has stopped...")
                        self.bot.currentlyThundering = False
            end = time.time()
            errorCH = self.bot.get_channel(self.bot.errorCH)
            await errorCH.send(f"last updated <t:{int(time.time())}:R>\nTook {round(end-start, 2)}s", delete_after=30)



    @scrape.before_loop
    async def wait(self):
        await self.bot.wait_until_ready()


async def setup(bot):
	await bot.add_cog(Scraper(bot))