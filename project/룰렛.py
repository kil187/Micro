from random import choice
import discord
from discord.ext import commands
from discord_slash import cog_ext, SlashContext

class Slash(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @cog_ext.cog_slash(name="룰렛", description='도박 룰렛')
    async def help(self, ctx: SlashContext):
        roulette = ['🧱', '❤️', '🖼️', '🎁', '🔰']
        random = f"{choice(roulette)} {choice(roulette)} {choice(roulette)}"
        embed = discord.Embed(ttitle="[ 룰렛 ]", description=f"{ctx.author.mention}님이 뽑은 그림은 {random}입니다!")

        await ctx.send(content="",embeds=[embed])

def setup(bot):
    bot.add_cog(Slash(bot))