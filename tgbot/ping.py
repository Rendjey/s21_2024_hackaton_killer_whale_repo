import requests

url = 'http://83.147.246.223:6000/registration'
try:
    data = {"nickname": "user"}  # Ваши данные JSON
    response = requests.post(url, json=data)
    if response.status_code == 200:
        print("Запрос успешно выполнен:")
        print(response.json())  # Если ответ в формате JSON
    else:
        print("Произошла ошибка при выполнении запроса. Код ошибки:", response.status_code)
except Exception as err:
    print(f'\033[31m{err} \033[0m')  # Python 3.6
