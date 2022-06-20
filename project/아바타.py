import discord
from discord.ext import commands
from discord_slash import cog_ext, SlashContext

class Slash(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @cog_ext.cog_slash(name="아바타", description='/아바타 [자신의 아바타],/아바타 [@사용자 멘션]')
    async def avatar(self, ctx: SlashContext,*,member : discord.Member = None):
    
        member = ctx.author if not member else member
        avaEmbed = discord.Embed(title= f"{member.name}#{member.discriminator}의 아바타.")
        avaEmbed.set_image(url = member.avatar_url)
        
        await ctx.send(embed = avaEmbed)

def setup(bot):
    bot.add_cog(Slash(bot))