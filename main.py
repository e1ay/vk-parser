import requests
import time
group_id = 'group_id'  # Идентификатор группы
access_token = 'access_token'  # Ваш токен доступа
api_version = '5.131'  # Версия API

# Получение общего количества участников группы
members_count = requests.get(f'https://api.vk.com/method/groups.getMembers?group_id={group_id}&v={api_version}&access_token={access_token}').json()['response']['count']

# Параметры запроса
params = {
    'group_id': group_id,
    'v': api_version,
    'access_token': access_token,
    'count': 1000,  # Количество пользователей, получаемых за один запрос
    'offset': 0,  # Смещение для получения следующей порции пользователей
}

# Список для хранения всех идентификаторов пользователей
all_members = []

# Повторяем запросы, пока не получим всех участников
while len(all_members) < members_count:
    time.sleep(0.5) # Ставим задержку в 0.5 секунд, чтобы сервер успевал обрабатывать запросы
    response = requests.get('https://api.vk.com/method/groups.getMembers', params=params).json()
    if 'response' in response:
        members = response['response']['items']
        all_members.extend(members)
        params['offset'] += 1000
    else:
        print("Произошла ошибка при выполнении запроса.")
        break
print(f"Количество участников: {members_count}")

# Сохранение в файл
file = open('name.txt', 'w')
for i in all_members:
    file.write(f'{i}\n')