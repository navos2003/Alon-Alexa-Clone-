import python_weather
import datetime
import asyncio
import requests

url = 'http://ipinfo.io/json'
data = requests.get(url).json()

async def get_weatherInfo():
    client = python_weather.Client(format = python_weather.IMPERIAL)
    weather = await client.find(f'{data["city"]} {data["region"]}')
    print(f'\nWeather in {data["city"]}, {data["region"]}, {data["country"]}:')
    print(f'\nNow\t\t{weather.current.sky_text}\t{weather.current.temperature}°F')
    print('\nDaily Forecast:\n')
    for day, forecast in enumerate(weather.forecasts):
        if day == 2:
            print(f'Tomorrow\t{forecast.sky_text}\t{forecast.temperature}°F')
        elif day == 3:
            print(f'{(datetime.date.today()+datetime.timedelta(days=2)).strftime("%b %-d")}\t\t{forecast.sky_text}\t{forecast.temperature}°F')
        elif day == 4:
            print(f'{(datetime.date.today()+datetime.timedelta(days=3)).strftime("%b %-d")}\t\t{forecast.sky_text}\t{forecast.temperature}°F')
    await client.close()