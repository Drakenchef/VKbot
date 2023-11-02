from _token import TOKEN

import datetime
from datetime import date
import vk_api
from vk_api import VkUpload
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.utils import get_random_id
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
import json
import pickle
import re
import os.path
import requests

from schedule import day_schedule_to_string, get_schedule
from weather import get_weather_now, get_weather_today, get_weather_tomorrow, get_weather_five_days


COMMAND_START = 'start'
COMMAND_WEATHER = 'weather'
COMMAND_SCHEDULE = 'schedule'
SCHEDULE_TODAY = 'сегодня'
SCHEDULE_TOMORROW = 'завтра'
SCHEDULE_CUR_WEEK = 'неделя'
SCHEDULE_NEXT_WEEK = 'следующая неделя'
SCHEDULE_GET_WEEK = 'какая неделя?'
SCHEDULE_GET_GROUP = 'какая группа?'
WEATHER_NOW = 'сейчас'
WEATHER_TODAY = 'сегодня'
WEATHER_TOMORROW = 'завтра'
WEATHER_NEXT_FIVE_DAYS = 'на 5 дней'
WEEKDAYS = ['понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота', 'воскресенье']

user_schedule_groups = pickle.load(open('users_groups.pkl', 'rb')) if os.path.exists('users_groups.pkl') else dict()
schedule_group_regex = re.compile(r'^[а-яА-Я]{4}-\d{2}-\d{2}$')
full_schedule = get_schedule()


def get_week(cur_date=date.today()):
    now = cur_date
    if now.month + 1 > 8:
        first_day = date(now.year, 9, 1)
    else:
        first_day = date(now.year, 2, 9)
    while first_day.weekday() != 0:
        first_day += datetime.timedelta(days=1)

    days = now - first_day
    return (days.days // 7) + 2


def on_message(vk, user_id, text: str, vk_session):
    if schedule_group_regex.match(text):
        user_schedule_groups[user_id] = text.lower()
        vk.messages.send(
            user_id=user_id,
            random_id=get_random_id(),
            message=f'Я запомнил, что ты из группы {text}',
            keyboard=VkKeyboard.get_empty_keyboard()
        )
        pickle.dump(user_schedule_groups, open('users_groups.pkl', 'wb'))
        return

    words = text.lower().split()

    if words[0] == 'бот':
        on_schedule_command(vk, user_id, words[1:], vk_session)
        return

    if words[0] == 'погода':
        on_weather_command(vk, user_id, words[1:], vk_session)
        return

    vk.messages.send(
        user_id=user_id,
        random_id=get_random_id(),
        message='Не понял...'
    )


def on_start_command(vk, user_id, _, __):
    vk.messages.send(
        user_id=user_id,
        random_id=get_random_id(),
        message='Напиши "бот", если ты хочешь посмотреть рассписание!\n'
                'Напиши "погода", если ты хочешь посмотреть погоду!\n'
                'Удачи!'
    )


def on_weather_command(vk, user_id, args, vk_session):
    if not args:
        keyboard = VkKeyboard(one_time=False)
        keyboard.add_button('сейчас', color=VkKeyboardColor.PRIMARY, payload={
            'command': COMMAND_WEATHER,
            'args': [WEATHER_NOW]
        })
        keyboard.add_button('сегодня', color=VkKeyboardColor.POSITIVE, payload={
            'command': COMMAND_WEATHER,
            'args': [WEATHER_TODAY]
        })
        keyboard.add_button('завтра', color=VkKeyboardColor.POSITIVE, payload={
            'command': COMMAND_WEATHER,
            'args': [WEATHER_TOMORROW]
        })
        keyboard.add_line()
        keyboard.add_button('на 5 дней', color=VkKeyboardColor.POSITIVE, payload={
            'command': COMMAND_WEATHER,
            'args': [WEATHER_NEXT_FIVE_DAYS]
        })
        vk.messages.send(
            user_id=user_id,
            random_id=get_random_id(),
            keyboard=keyboard.get_keyboard(),
            message='Показать погоду в Москве...'
        )
        return

    if args[0] == WEATHER_NOW:
        info = get_weather_now()

        upload = VkUpload(vk_session)
        attachments = []
        image = requests.get(f"http://openweathermap.org/img/wn/{info['main'][1]}@2x.png", stream=True)
        photo = upload.photo_messages(photos=image.raw)[0]
        attachments.append("photo{}_{}".format(photo["owner_id"], photo["id"]))

        vk.messages.send(
            user_id=user_id,
            attachment=','.join(attachments),
            random_id=get_random_id(),
            message='Погода в Москве'
        )
        text = f"{info['main'][0]}, температура: {info['temperature']} °С\n" \
               f"Давление: {info['pressure']} мм рт. ст., влажность: {info['humidity']}%\n" \
               f"Ветер: {info['wind_description']}, {info['wind_speed']}м/с, {info['wind_direction']}"
        vk.messages.send(
            user_id=user_id,
            random_id=get_random_id(),
            message=text
        )
        return

    if args[0] == WEATHER_TODAY:
        time = ['УТРО\n', 'ДЕНЬ\n', 'ВЕЧЕР\n', 'НОЧЬ\n']
        text = ''
        i = 0
        l = get_weather_today()
        for info in l:
            text += time[i] + f"{info['main'][0]}, температура: {info['temperature']} °С\n" \
                   f"Давление: {info['pressure']} мм рт. ст., влажность: {info['humidity']}%\n" \
                   f"Ветер: {info['wind_description']}, {info['wind_speed']}м/с, {info['wind_direction']}\n\n"
            i += 1
        vk.messages.send(
            user_id=user_id,
            random_id=get_random_id(),
            message=text
        )
        return

    if args[0] == WEATHER_TOMORROW:
        time = ['УТРО\n', 'ДЕНЬ\n', 'ВЕЧЕР\n', 'НОЧЬ\n']
        text = ''
        i = 0
        l = get_weather_tomorrow()
        for info in l:
            text += time[i] + f"{info['main'][0]}, температура: {info['temperature']} °С\n" \
                              f"Давление: {info['pressure']} мм рт. ст., влажность: {info['humidity']}%\n" \
                              f"Ветер: {info['wind_description']}, {info['wind_speed']}м/с, {info['wind_direction']}\n\n"
            i += 1
        vk.messages.send(
            user_id=user_id,
            random_id=get_random_id(),
            message=text
        )
        return

    if args[0] == WEATHER_NEXT_FIVE_DAYS:
        temps = get_weather_five_days()
        text = '/ '
        for i in range(len(temps[0])):
            text += str(temps[0][i]) + ' / '
        text += 'День\n'
        for i in range(len(temps[1])):
            text += str(temps[1][i]) + ' / '
        text += 'Ночь'
        vk.messages.send(
            user_id=user_id,
            random_id=get_random_id(),
            message=text
        )
        return


def on_schedule_command(vk, user_id, args, _):
    if not args or schedule_group_regex.match(args[0]):
        group = args[0] if args else ''
        keyboard = VkKeyboard(one_time=True)
        keyboard.add_button('на сегодня', color=VkKeyboardColor.POSITIVE, payload={
            'command': COMMAND_SCHEDULE,
            'args': [SCHEDULE_TODAY, group]
        })
        keyboard.add_button('на завтра', color=VkKeyboardColor.NEGATIVE, payload={
            'command': COMMAND_SCHEDULE,
            'args': [SCHEDULE_TOMORROW, group]
        })
        keyboard.add_line()
        keyboard.add_button('на эту неделю', color=VkKeyboardColor.PRIMARY, payload={
            'command': COMMAND_SCHEDULE,
            'args': [SCHEDULE_CUR_WEEK, group]
        })
        keyboard.add_button('на следующую неделю', color=VkKeyboardColor.PRIMARY, payload={
            'command': COMMAND_SCHEDULE,
            'args': [SCHEDULE_NEXT_WEEK, group]

        })
        keyboard.add_line()
        keyboard.add_button('какая неделя?', color=VkKeyboardColor.SECONDARY, payload={
            'command': COMMAND_SCHEDULE,
            'args': [SCHEDULE_GET_WEEK]
        })
        keyboard.add_button('какая группа', color=VkKeyboardColor.SECONDARY, payload={
            'command': COMMAND_SCHEDULE,
            'args': [SCHEDULE_GET_GROUP]
        })
        vk.messages.send(
            user_id=user_id,
            random_id=get_random_id(),
            keyboard=keyboard.get_keyboard(),
            message='Показать расписание...'
        )
        return

    if args[0] == SCHEDULE_GET_GROUP:
        if user_id in user_schedule_groups:
            message = 'Показываю расписание группы ' + user_schedule_groups.get(user_id)
        else:
            message = 'группа не указана'

        vk.messages.send(
            user_id=user_id,
            random_id=get_random_id(),
            message=message
        )
        return

    if args[0] == SCHEDULE_GET_WEEK:
        vk.messages.send(
            user_id=user_id,
            random_id=get_random_id(),
            message=f'Идет {get_week()} неделя'
        )
        return

    if len(args) >= 2 and schedule_group_regex.match(args[1]):
        group = args[1]
    elif user_id in user_schedule_groups:
        group = user_schedule_groups[user_id]
    else:
        vk.messages.send(
            user_id=user_id,
            random_id=get_random_id(),
            message='Не указана группа!'
        )
        return

    if args[0] in WEEKDAYS:
        text = day_schedule_to_string(full_schedule[group][0][WEEKDAYS.index(args[0])])
        text += '\n' + day_schedule_to_string(full_schedule[group][1][WEEKDAYS.index(args[0])])
        vk.messages.send(
            user_id=user_id,
            random_id=get_random_id(),
            message=text
        )
        return

    if args[0] == SCHEDULE_TODAY:
        today = date.today()
        schedule = full_schedule[group][(get_week(today) + 1) % 2][today.weekday()]
        text = day_schedule_to_string(schedule, today)

        vk.messages.send(
            user_id=user_id,
            random_id=get_random_id(),
            message=text
        )
        return

    if args[0] == SCHEDULE_TOMORROW:
        tomorrow = date.today() + datetime.timedelta(days=1)
        schedule = full_schedule[group][(get_week(tomorrow) + 1) % 2][tomorrow.weekday()]
        text = day_schedule_to_string(schedule, tomorrow)

        vk.messages.send(
            user_id=user_id,
            random_id=get_random_id(),
            message=text
        )
        return

    if args[0] == SCHEDULE_CUR_WEEK:
        text = ''
        cur_day = date.today() - datetime.timedelta(days=date.today().weekday())
        schedule = full_schedule[group][(get_week(cur_day) + 1) % 2]
        while cur_day.weekday() != 6:
            text += day_schedule_to_string(schedule[cur_day.weekday()], cur_day) + '\n\n'
            cur_day += datetime.timedelta(days=1)

        vk.messages.send(
            user_id=user_id,
            random_id=get_random_id(),
            message=text
        )
        return

    if args[0] == SCHEDULE_NEXT_WEEK:
        text = ''
        cur_day = date.today() + datetime.timedelta(days=7-date.today().weekday())
        schedule = full_schedule[group][(get_week(cur_day) + 1) % 2]
        while cur_day.weekday() != 6:
            text += day_schedule_to_string(schedule[cur_day.weekday()], cur_day) + '\n\n'
            cur_day += datetime.timedelta(days=1)

        vk.messages.send(
            user_id=user_id,
            random_id=get_random_id(),
            message=text
        )
        return


command_handlers = {
    COMMAND_START: on_start_command,
    COMMAND_WEATHER: on_weather_command,
    COMMAND_SCHEDULE: on_schedule_command,
}


def main():
    vk_session = vk_api.VkApi(token=TOKEN)
    vk = vk_session.get_api()
    longPoll = VkLongPoll(vk_session)
    print('Listening...')
    for event in longPoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me:
            if hasattr(event, 'payload'):
                payload = json.loads(event.payload)
                handler = command_handlers[payload['command']]
                handler(vk, event.user_id, payload.get('args'), vk_session)
            else:
                on_message(vk, event.user_id, event.message, vk_session)


if __name__ == '__main__':
    main()
