import discord
from discord.ext import commands

class ReactionRole(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        if payload.member.bot:
            return
        if payload.message_id == self.bot.messageid:
            if payload.emoji.name == '\N{WHITE HEAVY CHECK MARK}':
                guild = await self.bot.fetch_guild(payload.guild_id)
                if guild is not None:
                    member = await guild.fetch_member(payload.user_id)

                    guild_member = discord.utils.get(guild.roles, name="thunder")
                    await member.add_roles(guild_member)

    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload):
        if payload.message_id == self.bot.messageid:
            if payload.emoji.name == '\N{WHITE HEAVY CHECK MARK}':
                guild = await self.bot.fetch_guild(payload.guild_id)
                if guild is not None:
                    member = await guild.fetch_member(payload.user_id)
                    if member.bot:
                        return
                    guild_member = discord.utils.get(guild.roles, name="thunder")
                    await member.remove_roles(guild_member)


async def setup(bot):
	await bot.add_cog(ReactionRole(bot)) 