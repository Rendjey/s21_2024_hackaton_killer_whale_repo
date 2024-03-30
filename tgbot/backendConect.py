import requests

class backConect:
    def __init__(self, apiUrl):
        self.backendApi = apiUrl
        self.ping()
    
    def ping(self):
        try:
            response = requests.get(self.backendApi)
            if response.status_code == 200:
                print(f'\033[32m{response.json()}\033[0m')
            return response.status_code
        except Exception as err:
            print(f'\033[31m{err}\n\nСервер выключен?\033[0m')
            return err
        
    def reg(self, username):
        return self.sendJson('/registration', {"nickname": username})
        
    def sendJson(self, path, data):
        url = self.backendApi+path
        try:
            response = requests.post(url, json=data)
            if response.status_code == 200:
                return response.json()
            else:
                print(f'\033[31mПри обращении на сервер произошла ошибка {response.status_code}\033[0m')
                return response.status_code
        except Exception as err:
            print(f'\033[31m{err}\n\nСервер выключен?\033[0m')
            return err



# registration
if __name__ == '__main__':
    backend = backConect('http://83.147.246.223:6000')
    print(backend.ping())
    print(backend.sendJson('/registration', {"nickname": "user"}))
    print(backend.reg("user"))