import discord
from discord.ext import commands
from discord_slash import cog_ext, SlashContext
import requests

class Slash(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @cog_ext.cog_slash(name="날씨", description='/날씨 [나라,도시 이름]')
    async def weather(self, ctx: SlashContext, *, location : str=None):
     API_ID = "API ID"
     if location == None:
        ctx.command.reset_cooldown(ctx)
        await ctx.send('You havent provided a location!')
     else:
        try:
            x = location.lower()
            x = requests.get('http://api.openweathermap.org/data/2.5/weather?q={}&APPID={}'.format(x, API_ID)).json()
            country, city = x['sys']['country'], x['name']
            cord1, cord2 = x['coord']['lon'], x['coord']['lat']
            main, desc = x['weather'][0]['main'], x['weather'][0]['description']
            speed, humid = x['wind']['speed'], x['main']['humidity']
            icon, pressure, clouds = x['weather'][0]['icon'], x['main']['pressure'], x['clouds']['all']
            temp, temp_f, zone = x['main']['temp'], x['main']['feels_like'], x['timezone']
            embed=discord.Embed(
                title=f'{city} ({country})',
                colour=discord.Color.blue(),
                description=f'Longitude : {cord1} | Latitude : {cord2}'
            )
            embed.add_field(name='Wind', value=f'{speed} MPH')
            embed.add_field(name='Humidity', value=f'{humid}%')
            embed.add_field(name='Weather', value=f'{main} ({desc})')
            embed.add_field(name='Pressure', value=f'{pressure}')
            embed.add_field(name='Clouds', value=f'{clouds}')
            embed.add_field(name='Temperature', value=f'{round(temp - 273.15)} °C')
            embed.add_field(name='Feels Like', value=f'{round(temp_f - 273.15)} °C')
            embed.add_field(name=f'Time Zone', value=f'{zone}')
            embed.add_field(name=f'Min Temp', value=str(round(x['main']['temp_min'] - 273.15)) + ' °C')
            embed.add_field(name=f'Max Temp', value=str(round(x['main']['temp_max'] - 273.15)) + ' °C')
            await ctx.send(embed=embed)
        except KeyError:
            await ctx.send('Location was invalid.')


def setup(bot):
    bot.add_cog(Slash(bot))
