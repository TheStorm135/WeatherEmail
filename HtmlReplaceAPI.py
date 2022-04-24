from WeatherAPI import *

def rpc(old, new):
    html = html.replace(f"api.{old}", str(new))

with open(r'html/index.html', 'r') as file:
    html = file.read()


    html = html.replace("api.location", loc)
    html = html.replace("api.temp", str(temp))
    html = html.replace("api.max", str(max))
    html = html.replace("api.low", str(min))
    html = html.replace("api.cond", str(cond))
    html = html.replace("api.uv", str(uv))
    html = html.replace("api.hum", str(hum))
    html = html.replace("api.rain", str(rain))
    html = html.replace("api.sunrise", str(astro['sunrise']))
    html = html.replace("api.sunset", str(astro['sunset']))
    html = html.replace("api.moon", str(astro['moon_phase']))
    html = html.replace("api.update", str(weather['current']['last_updated']))
