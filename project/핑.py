from http import client
import discord
from discord.ext import commands
from discord_slash import cog_ext, SlashContext


class Slash(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @cog_ext.cog_slash(name="핑", description='기본 지연시간')
    async def ping(self, ctx: SlashContext):
     embed = discord.Embed(
     title="🏓 퐁!",
     description=f"기본 지연시간은 {round(self.bot.latency*1000)}ms 입니다.",
     
     )
     await ctx.send(embed=embed)
def setup(bot):
    bot.add_cog(Slash(bot))
