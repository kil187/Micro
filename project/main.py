import discord
from discord.ext import commands
from discord_slash import SlashCommand


bot = commands.Bot(command_prefix="prefix")
slash = SlashCommand(bot, sync_commands=True, sync_on_cog_reload=True)

@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=discord.Game("/도움"))
    print('봇 로그인.')

@bot.event
async def on_command_error(ctx, error):
    embed = discord.Embed(title="오류!!", description="오류가 발생했습니다.", color=0xFF0000)
    embed.add_field(name="상세", value=f"{error}")
    
    await ctx.send(embed=embed)

@bot.event
async def on_message(message):
    # do some extra stuff here

    await bot.process_commands(message)

bot.load_extension("도움")
bot.load_extension("핑")
bot.load_extension("아바타")
bot.load_extension("청소")
bot.load_extension("아이디")
bot.load_extension("시간")
bot.load_extension("날씨")
bot.load_extension("초대")
bot.load_extension("저격")
bot.load_extension("유튜브")
bot.load_extension("룰렛")
bot.load_extension("유저정보")

bot.run('TOKEN')
