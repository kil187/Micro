import discord
from discord.ext import commands
from discord_slash import cog_ext, SlashContext

class Slash(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @cog_ext.cog_slash(name="아이디", description='/아이디 [자신의 아이디],/아이디 [@사용자 멘션]')
    async def getuser(self, ctx: SlashContext,*,member : discord.Member = None):
        member = ctx.author if not member else member
        embed = discord.Embed(title="")
        embed.add_field(name='아이디:', value=member.id)
        await ctx.send(content="",embeds=[embed])

def setup(bot):
    bot.add_cog(Slash(bot))