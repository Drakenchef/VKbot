import datetime
import json
import PIL
import requests
from _token import WEATHER_KEY

weather_conditions = {
    'Thunderstorm': 'Гроза',
    'Drizzle': 'Морось',
    'Rain': 'Дождь',
    'Snow': 'Снег',
    'Mist': 'Легкий туман',
    'Smoke': 'Смог',
    'Haze': 'Дымка',
    'Dust': 'Пыльно',
    'Fog': 'Туман',
    'Sand': 'Песчаная буря',
    'Ash': 'Пепельный снег',
    'Squall': 'Шквальный ветер',
    'Tornado': 'Торнадо',
    'Clear': 'Ясно',
    'Clouds': 'Облачно'

}


def get_wind_description(speed):
    if speed < 0.2:
        return 'Штиль'
    elif speed < 1.5:
        return 'Очень лёгкий ветер'
    elif speed < 3.3:
        return 'Лёгкий'
    elif speed < 5.4:
        return 'Слабый'
    elif speed < 7.9:
        return 'Умеренный'
    elif speed < 10.7:
        return 'Свежий'
    elif speed < 13.8:
        return 'Сильный'
    elif speed < 17.1:
        return 'Крепкий'
    elif speed < 20.7:
        return 'Очень крепкий'
    elif speed < 24.4:
        return 'Шторм'
    elif speed < 28.4:
        return 'Сильный шторм'
    elif speed < 32.6:
        return 'Жестокий шторм'
    else:
        return 'Ураган'


def get_wind_direction(angle):
    if angle < 0 or angle > 360:
        return("Некорректный угол")
    elif angle < 22.5 or angle > 337.5:
        return("Северный ветер")
    elif angle < 67.5:
        return("Северо-восточный ветер")
    elif angle < 112.5:
        return("Восточный ветер")
    elif angle < 157.5:
        return("Юго-восточный ветер")
    elif angle < 202.5:
        return("Южный ветер")
    elif angle < 247.5:
        return("Юго-западный ветер")
    elif angle < 292.5:
        return("Западный ветер")
    else:
        return("Северо-западный ветер")


def get_weather_now():
    response = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q=moscow&appid={WEATHER_KEY}&units=metric')
    info = response.json()
    res = dict()
    res['main'] = [weather_conditions[info['weather'][0]['main']], info['weather'][0]['icon']]
    res['temperature'] = str(info['main']['temp_min']) + ' - ' + str(info['main']['temp_max'])
    res['pressure'] = int(info['main']['pressure'] * 0.75)
    res['humidity'] = info['main']['humidity']
    res['wind_description'] = get_wind_description(info['wind']['speed'])
    res['wind_speed'] = info['wind']['speed']
    res['wind_direction'] = get_wind_direction(info['wind']['deg'])
    return res


def get_weather_today():
    today = datetime.date.today()
    tomorrow = datetime.date.today() + datetime.timedelta(days=1)
    response = requests.get(f'http://api.openweathermap.org/data/2.5/forecast?q=moscow&appid={WEATHER_KEY}&units=metric')
    info = response.json()
    res = []
    for forecast in info['list']:
        if forecast['dt_txt'] == str(today.year) + '-' + ('0' if today.month < 10 else '') + str(today.month) + '-' + ('0' if today.day < 10 else '') + str(today.day) + ' 09:00:00':
            print('morning')
            morning = dict()
            morning['main'] = [weather_conditions[forecast['weather'][0]['main']], forecast['weather'][0]['icon']]
            morning['temperature'] = str(forecast['main']['temp_min']) + ' - ' + str(forecast['main']['temp_max'])
            morning['pressure'] = int(forecast['main']['pressure'] * 0.75)
            morning['humidity'] = forecast['main']['humidity']
            morning['wind_description'] = get_wind_description(forecast['wind']['speed'])
            morning['wind_speed'] = forecast['wind']['speed']
            morning['wind_direction'] = get_wind_direction(forecast['wind']['deg'])
            res.append(morning)
        if forecast['dt_txt'] == str(today.year) + '-' + ('0' if today.month < 10 else '') + str(today.month) + '-' + ('0' if today.day < 10 else '') + str(today.day) + ' 12:00:00':
            print('day')
            day = dict()
            day['main'] = [weather_conditions[forecast['weather'][0]['main']], forecast['weather'][0]['icon']]
            day['temperature'] = str(forecast['main']['temp_min']) + ' - ' + str(forecast['main']['temp_max'])
            day['pressure'] = int(forecast['main']['pressure'] * 0.75)
            day['humidity'] = forecast['main']['humidity']
            day['wind_description'] = get_wind_description(forecast['wind']['speed'])
            day['wind_speed'] = forecast['wind']['speed']
            day['wind_direction'] = get_wind_direction(forecast['wind']['deg'])
            res.append(day)
        if forecast['dt_txt'] == str(today.year) + '-' + ('0' if today.month < 10 else '') + str(today.month) + '-' + ('0' if today.day < 10 else '') + str(today.day) + ' 18:00:00':
            print('evening')
            evening = dict()
            evening['main'] = [weather_conditions[forecast['weather'][0]['main']], forecast['weather'][0]['icon']]
            evening['temperature'] = str(forecast['main']['temp_min']) + ' - ' + str(forecast['main']['temp_max'])
            evening['pressure'] = int(forecast['main']['pressure'] * 0.75)
            evening['humidity'] = forecast['main']['humidity']
            evening['wind_description'] = get_wind_description(forecast['wind']['speed'])
            evening['wind_speed'] = forecast['wind']['speed']
            evening['wind_direction'] = get_wind_direction(forecast['wind']['deg'])
            res.append(evening)
        if forecast['dt_txt'] == str(tomorrow.year) + '-' + ('0' if tomorrow.month < 10 else '') + str(tomorrow.month) + '-' + ('0' if tomorrow.day < 10 else '') + str(tomorrow.day) + ' 03:00:00':
            print('night')
            night = dict()
            night['main'] = [weather_conditions[forecast['weather'][0]['main']], forecast['weather'][0]['icon']]
            night['temperature'] = str(forecast['main']['temp_min']) + ' - ' + str(forecast['main']['temp_max'])
            night['pressure'] = int(forecast['main']['pressure'] * 0.75)
            night['humidity'] = forecast['main']['humidity']
            night['wind_description'] = get_wind_description(forecast['wind']['speed'])
            night['wind_speed'] = forecast['wind']['speed']
            night['wind_direction'] = get_wind_direction(forecast['wind']['deg'])
            res.append(night)
    print(res)
    return res


def get_weather_tomorrow():
    today = datetime.date.today() + datetime.timedelta(days=1)
    tomorrow = datetime.date.today() + datetime.timedelta(days=1)
    response = requests.get(f'http://api.openweathermap.org/data/2.5/forecast?q=moscow&appid={WEATHER_KEY}&units=metric')
    info = response.json()
    res = []
    for forecast in info['list']:
        if forecast['dt_txt'] == str(today.year) + '-' + ('0' if today.month < 10 else '') + str(today.month) + '-' + ('0' if today.day < 10 else '') + str(today.day) + ' 06:00:00':
            morning = dict()
            morning['main'] = [weather_conditions[forecast['weather'][0]['main']], forecast['weather'][0]['icon']]
            morning['temperature'] = str(forecast['main']['temp_min']) + ' - ' + str(forecast['main']['temp_max'])
            morning['pressure'] = int(forecast['main']['pressure'] * 0.75)
            morning['humidity'] = forecast['main']['humidity']
            morning['wind_description'] = get_wind_description(forecast['wind']['speed'])
            morning['wind_speed'] = forecast['wind']['speed']
            morning['wind_direction'] = get_wind_direction(forecast['wind']['deg'])
            res.append(morning)
        if forecast['dt_txt'] == str(today.year) + '-' + ('0' if today.month < 10 else '') + str(today.month) + '-' + ('0' if today.day < 10 else '') + str(today.day) + ' 12:00:00':
            day = dict()
            day['main'] = [weather_conditions[forecast['weather'][0]['main']], forecast['weather'][0]['icon']]
            day['temperature'] = str(forecast['main']['temp_min']) + ' - ' + str(forecast['main']['temp_max'])
            day['pressure'] = int(forecast['main']['pressure'] * 0.75)
            day['humidity'] = forecast['main']['humidity']
            day['wind_description'] = get_wind_description(forecast['wind']['speed'])
            day['wind_speed'] = forecast['wind']['speed']
            day['wind_direction'] = get_wind_direction(forecast['wind']['deg'])
            res.append(day)
        if forecast['dt_txt'] == str(today.year) + '-' + ('0' if today.month < 10 else '') + str(today.month) + '-' + ('0' if today.day < 10 else '') + str(today.day) + ' 18:00:00':
            evening = dict()
            evening['main'] = [weather_conditions[forecast['weather'][0]['main']], forecast['weather'][0]['icon']]
            evening['temperature'] = str(forecast['main']['temp_min']) + ' - ' + str(forecast['main']['temp_max'])
            evening['pressure'] = int(forecast['main']['pressure'] * 0.75)
            evening['humidity'] = forecast['main']['humidity']
            evening['wind_description'] = get_wind_description(forecast['wind']['speed'])
            evening['wind_speed'] = forecast['wind']['speed']
            evening['wind_direction'] = get_wind_direction(forecast['wind']['deg'])
            res.append(evening)
        if forecast['dt_txt'] == str(tomorrow.year) + '-' + ('0' if tomorrow.month < 10 else '') + str(tomorrow.month) + '-' + ('0' if tomorrow.day < 10 else '') + str(tomorrow.day) + ' 00:00:00':
            night = dict()
            night['main'] = [weather_conditions[forecast['weather'][0]['main']], forecast['weather'][0]['icon']]
            night['temperature'] = str(forecast['main']['temp_min']) + ' - ' + str(forecast['main']['temp_max'])
            night['pressure'] = int(forecast['main']['pressure'] * 0.75)
            night['humidity'] = forecast['main']['humidity']
            night['wind_description'] = get_wind_description(forecast['wind']['speed'])
            night['wind_speed'] = forecast['wind']['speed']
            night['wind_direction'] = get_wind_direction(forecast['wind']['deg'])
            res.append(night)
    return res


def get_weather_five_days():
    response = requests.get(
        f'http://api.openweathermap.org/data/2.5/forecast?q=moscow&appid={WEATHER_KEY}&units=metric')
    info = response.json()
    cur_day = datetime.date.today()
    morning = []
    night = []
    for forecast in info['list']:
        if forecast['dt_txt'] == str(cur_day.year) + '-' + ('0' if cur_day.month < 10 else '') + str(cur_day.month) + '-' + ('0' if cur_day.day < 10 else '') + str(cur_day.day) + ' 12:00:00':
            morning.append(forecast['main']['temp'])
            cur_day += datetime.timedelta(days=1)
            print(forecast['main']['temp'])
        if forecast['dt_txt'] == str(cur_day.year) + '-' + ('0' if cur_day.month < 10 else '') + str(cur_day.month) + '-' + ('0' if cur_day.day < 10 else '') + str(cur_day.day) + ' 03:00:00':
            night.append(forecast['main']['temp'])
            print()

    print(morning)
    print(night)
    return [morning, night]


if __name__ == '__main__':
    print(len(get_weather_five_days()))
    # print(get_weather_tomorrow())
