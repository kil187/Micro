import discord
from discord.ext import commands
from discord_slash import cog_ext, SlashContext

class Slash(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @cog_ext.cog_slash(name="청소", description='/청소 [메세지 개수]')
    @commands.has_permissions(administrator = True)
    async def clear(self,ctx: SlashContext,amount = 2):
        await ctx.channel.purge(limit=int(amount))
        await ctx.send("메세지 " + str(amount) + "개를 삭제했어요.")

def setup(bot):
    bot.add_cog(Slash(bot))
