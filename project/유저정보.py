import discord
from discord.ext import commands
from discord_slash import cog_ext, SlashContext
from datetime import timedelta, datetime

class Slash(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @cog_ext.cog_slash(name="유저정보", description='유저정보')
    async def help(self, ctx: SlashContext,*,member : discord.Member = None):
     member = ctx.author if not member else member


     rlist = []
     for role in member.roles:
      if role.name != "@everyone":
        rlist.append(role.mention)

     b = ", ".join(rlist)


     embed = discord.Embed(timestamp = datetime.now())

     embed.set_author(name=f"User Info - {member}"),
     embed.set_thumbnail(url=member.avatar_url),
     embed.set_footer(text=f'Requested by - {ctx.author}',
     icon_url=ctx.author.avatar_url)

     embed.add_field(name='ID:',value=member.id,inline=False)
     embed.add_field(name='Name:',value=member.display_name,inline=False)
 
     embed.add_field(name='Created at:',value=member.created_at,inline=False)
     embed.add_field(name='Joined at:',value=member.joined_at,inline=False)

  
 
     embed.add_field(name='Bot:',value=member.bot,inline=False)
 
     embed.add_field(name=f'Roles:({len(rlist)})',value=''.join([b]),inline=False)
     embed.add_field(name='Top Role:',value=member.top_role.mention,inline=False)
     await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Slash(bot))