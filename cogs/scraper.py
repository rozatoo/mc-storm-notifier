from discord.ext import tasks
from discord.ext import commands
from arsenic import browsers, services
import arsenic
import time
from utils import get_or_fetch_channel
#test

class Scraper(commands.Cog, command_attrs=dict(hidden=False)):
    def __init__(self, bot):
        self.bot = bot 
        self.scrape.start()

    @tasks.loop(seconds=60.0)
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
                worldtime = await session.wait_for_element(3, 'div.largeclock.timeofday')
                worldtime = await worldtime.get_text()
                src = await session.get_page_source()
                ch = await get_or_fetch_channel(self, 994478862362759188)
                if "thunder_night" in src:
                    if self.bot.currentlyThundering is False:
                        await ch.send(f"@everyone a thunderstorm started <t:{int(time.time())}:R>")
                        self.bot.currentlyThundering = True
                elif "thunder_day" in src:
                    if self.bot.currentlyThundering is False:
                        await ch.send(f"@everyone a thunderstorm started <t:{int(time.time())}:R>")
                        self.bot.currentlyThundering = True
                else:
                    if self.bot.currentlyThundering is True:
                        await ch.send("The thunderstorm has stopped...")
                        self.bot.currentlyThundering = False
            end = time.time()
            errorCH = await get_or_fetch_channel(self, self.bot.errorCH)
            await errorCH.send(f"last updated <t:{int(time.time())}:R>\nTook {round(end-start, 2)}s\nWorld time: {worldtime}\nCurrently Thundering: {self.bot.currentlyThundering}", delete_after=60)



    @scrape.before_loop
    async def wait(self):
        await self.bot.wait_until_ready()


def setup(bot):
	bot.add_cog(Scraper(bot))