from discord.ext import commands
from arsenic import browsers, services
import arsenic

class Commands(commands.Cog, command_attrs=dict(hidden=False)):
    def __init__(self, bot):
        self.bot = bot 

    @commands.command()
    async def disable(self, ctx):
        if ctx.user.id != 982849405357019166:
            return await ctx.reply("no")
        else:
            self.bot.doScrape = False
            return await ctx.reply("ok! disabled")
    
    @commands.command()
    async def enable(self, ctx):
        if ctx.user.id != 982849405357019166:
            return await ctx.reply("no")
        else:
            self.bot.doScrape = True
            return await ctx.reply("ok! enabled")





async def setup(bot):
	await bot.add_cog(Commands(bot))