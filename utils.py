import discord


async def get_or_fetch_channel(self, channel_id):
    """Only queries API if the channel is not in cache."""
    await self.bot.wait_until_ready()
    ch = self.bot.get_channel(int(channel_id))
    if ch:
        return ch

    try:
        ch = await self.bot.fetch_channel(int(channel_id))
    except discord.HTTPException:
        return None
    else:
        return ch