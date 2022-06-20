import discord
from discord.ext import commands
from discord_slash import cog_ext, SlashContext
import urllib.parse, urllib.request, re

class Slash(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @cog_ext.cog_slash(name="유튜브", description='유튜브 영상 랜덤 검색')
    async def youtube(self, ctx: SlashContext, *, search):
     query_string = urllib.parse.urlencode({'search_query': search})
     htm_content = urllib.request.urlopen('http://www.youtube.com/results?' + query_string)
     search_results = re.findall(r'/watch\?v=(.{11})', htm_content.read().decode())
     await ctx.send('http://www.youtube.com/watch?v=' + search_results[0])

def setup(bot):
    bot.add_cog(Slash(bot))
