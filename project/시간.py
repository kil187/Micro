import discord
from discord.ext import commands
from discord_slash import cog_ext, SlashContext
import time
from datetime import datetime
from pytz import timezone


class Slash(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @cog_ext.cog_slash(name="시간", description='런던,배를린,중앙유럽,이스라엘,케나다 동쪽,미국,태평양의 시간')
    async def time(self, ctx: SlashContext):
     fmt = "%Y-%m-%d %H:%M:%S %Z%z"

    # Current time in UTC
     now_utc = datetime.now(timezone('UTC'))
     await ctx.send (now_utc.strftime(fmt) + " (UTC)")

    # Convert to Europe/London time zone
     now_london = now_utc.astimezone(timezone('Europe/London'))
     await ctx.send (now_london.strftime(fmt) + " (London)")

    # Convert to Europe/Berlin time zone
     now_berlin = now_utc.astimezone(timezone('Europe/Berlin'))
     await ctx.send (now_berlin.strftime(fmt) + " (Berlin)")

    # Convert to CET time zone
     now_cet = now_utc.astimezone(timezone('CET'))
     await ctx.send (now_cet.strftime(fmt) + " (CET)")

    # Convert to Israel time zone
     now_israel = now_utc.astimezone(timezone('Israel'))
     await ctx.send (now_israel.strftime(fmt) + " (Israel)")

    # Convert to Canada/Eastern time zone
     now_canada_east = now_utc.astimezone(timezone('Canada/Eastern'))
     await ctx.send (now_canada_east.strftime(fmt) + " (Canada/Eastern)")
 
    # Convert to US/Central time zone
     now_central = now_utc.astimezone(timezone('US/Central'))
     await ctx.send (now_central.strftime(fmt) + " (US/Central)")
 
    # Convert to US/Pacific time zone
     now_pacific = now_utc.astimezone(timezone('US/Pacific'))
     await ctx.send (now_pacific.strftime(fmt) + " (US/Pacific)")

def setup(bot):
    bot.add_cog(Slash(bot))