import discord
from discord.ext import commands
from discord_slash import cog_ext, SlashContext
import platform
class Slash(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @cog_ext.cog_slash(name="도움", description='명령어 도움말')
    async def help(self, ctx: SlashContext):
        embed = discord.Embed(title="**Micro Bot 사용 설명서**")
        embed.add_field(name='일반명령어:', value='`도움`,`핑`,`아바타`,`아이디`,`시간`,`날씨`,`초대`,`저격`,`유튜브`',inline=False)
        embed.add_field(name='관리명령어:', value='`청소`',inline=False)
        embed.add_field(name='접두사:', value='`/(슬래쉬 커맨드)`',inline=False)
        embed.add_field(name='개발자:', value='`눈꽃#3197`',inline=False)
        embed.add_field(name='파이썬 버전:', value= platform.python_version(),inline=False)
        embed.set_footer(text='Micro Bot 버그나 오류 문의는 [눈꽃#3197으로 DM으로 넣어주세요.]')
        await ctx.send(content="",embeds=[embed])

def setup(bot):
    bot.add_cog(Slash(bot))