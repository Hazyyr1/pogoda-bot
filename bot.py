import os
import requests
from twitchio.ext import commands
from dotenv import load_dotenv

# Załaduj zmienne środowiskowe
load_dotenv()

TWITCH_TOKEN = '4l6zdyotud165tqetl3bn2otex8bnv'
OWM_API_KEY = 'e0561e4677fbd9a616065f4043c59ef5'
TWITCH_CLIENT_ID = 'gp762nuuoqcoxyPju8c569th9wz7q5'
TWITCH_NICK = 'opsabot'

bot = commands.Bot(
    irc_token=TWITCH_TOKEN,
    client_id=TWITCH_CLIENT_ID,
    nick=TWITCH_NICK,
    prefix='!',
    initial_channels=['Hazyy_', fake_danon']  # Zamień na właściwe nazwy kanałów
)

def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={OWM_API_KEY}"
    response = requests.get(url)
    data = response.json()
    if response.status_code == 200:
        return f"{data['main']['temp']}°C, {data['weather'][0]['description']}"
    else:
        return "Nie można znaleźć pogody dla podanego miasta."

@bot.event
async def event_ready():
    print(f"Bot jest gotowy i zalogowany jako {bot.nick}")

@bot.command(name='pogoda')
async def weather(ctx):
    if len(ctx.message.content.split()) > 1:
        city = ctx.message.content.split(' ', 1)[1]
        weather_info = get_weather(city)
        await ctx.send(weather_info)
    else:
        await ctx.send("Podaj miasto! Użycie: !pogoda [miasto]")

if __name__ == "__main__":
    bot.run()