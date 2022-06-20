import discord
from discord.ext import commands
from discord_slash import cog_ext, SlashContext

class Slash(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @cog_ext.cog_slash(name="저격", description='/저격 [자신을 저격],/저격 [@사용자 멘션]')
    async def snipe(self, ctx: SlashContext,*,member : discord.Member = None):
        member = ctx.author if not member else member
        embed = discord.Embed(description=f'{member.name}#{member.discriminator}🔫 빵야 빵야')
        await ctx.send(content="",embeds=[embed])


def setup(bot):
    bot.add_cog(Slash(bot))