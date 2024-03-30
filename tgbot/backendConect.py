import requests

# error - коды ошибки (0 - ок, 1 - ошибка. повторить запрос у пользователя, 2 - ошибка)
# message - сообщение для пользователя


class backConect:
    def __init__(self, apiUrl):
        self.backendApi = apiUrl
    
    def ping(self):
        try:
            response = requests.get(self.backendApi)
            if response.status_code == 200:
                responseData = response.json()
                if responseData['status'] == 'ok':
                    print(f'\033[32m{responseData}\033[0m')
                    return 0, f'Сервер ответил добром'
                else:
                    print(f'\033[31m{responseData}\033[0m')
                    return 2, f'Подключено, но сервер вернул ошибку: {responseData["description"]}'
        except Exception as err:
            print(f'\033[31m{err}\n\nСервер выключен?\033[0m')
            return 2, "Ошибка подключения к серверу"
        
    def sendJson(self, path, data):
        url = self.backendApi+path
        try:
            response = requests.post(url, json=data)
            # print(f'\033[32m{response.status_code}\033[0m')
            if response.status_code != 200:
                return 2, f'Сервер вернул {response.status_code}'
            return 0, response
        except Exception as err:
            return 2, "Ошибка подключения к серверу"
        
    def login(self, uid):
        error, response = self.sendJson('/login', {"uid": uid})
        if error != 0 or response.status_code != 200:
            return error, response

        responseData = response.json()
        if responseData['status'] == 'ok':
            username = responseData['username']
            return 0, f'Добро пожаловать {username}!\nВыберите свое дальнейшее дейсвие'
        elif responseData['description'] == 'Пользователь не найден':
            return 1, f'Добро пожаловать, пройдите регистрацию! Введите свой ник на платформе'

    def reg(self, username, uid):
        error, response = self.sendJson('/registration', {"username": username, "uid": uid})
        if error != 0 or response.status_code != 200:
            return error, response

        responseData = response.json()
        if responseData['status'] == 'ok':
            return 0, "Регистрация успешна\nОтправте /start для выбора переговорки"
        else:
            return 1, f'Ошибка: {responseData["description"]}'
    
    # !
    def get_floor(self, floor):
        error, response = self.sendJson('/room', {"floor": floor})

        if error != 0 or response.status_code != 200:
            return error, response

        responseData = response.json()
        if responseData['status'] == 'ok':

            return 0, "Регистрация успешна"
        else:
            return 1, f'Ошибка: {responseData["description"]}'


if __name__ == '__main__':
    backend = backConect('http://83.147.246.223:6000')

    error, message = backend.ping()
    print(f'{error}: {message}') 
    
    # print(backend.sendJson('/registration', {"username": "user"}))

    error, message = backend.login(393635636)
    print(f'{error}: {message}') 

    error, message = backend.reg("345", 393635637)
    print(f'{error}: {message}')

    error, message = backend.reg("456", 393635636)
    print(f'{error}: {message}') 