async def setup(bot):
    print("Setting up the DB")
    await bot.db.execute("CREATE TABLE IF NOT EXISTS subs(user_id INTERGER)")
    print("DB is set up :thumbsup:")