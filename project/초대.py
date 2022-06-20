import discord
from discord.ext import commands
from discord_slash import cog_ext, SlashContext

class Slash(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @cog_ext.cog_slash(name="초대", description='봇초대')
    async def help(self, ctx: SlashContext):
        embed = discord.Embed(title="Micro Bot 초대")
        embed.add_field(name='관리자 ⭕', value='[초대장](봇초대링크)')
        embed.add_field(name='관리자 ❌', value='[초대장](봇초대링크)')
        await ctx.send(content="",embeds=[embed])

def setup(bot):
    bot.add_cog(Slash(bot))
