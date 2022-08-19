from discord.ext import commands

class Commands(commands.Cog, command_attrs=dict(hidden=False)):
    def __init__(self, bot):
        self.bot = bot 

    @commands.guild_only()
    @commands.command()
    async def disable(self, ctx):
        if ctx.author.id != 982849405357019166:
            return await ctx.reply("no")
        else:
            self.bot.doScrape = False
            return await ctx.reply("ok! disabled")
    @commands.guild_only()
    @commands.command()
    async def enable(self, ctx):
        if ctx.author.id != 982849405357019166:
            return await ctx.reply("no")
        else:
            self.bot.doScrape = True
            return await ctx.reply("ok! enabled")





async def setup(bot):
	await bot.add_cog(Commands(bot)) 