from os import path
import json

# {"TGtoken": "6611074263:AAEiT9jX3C7hnMc8toJ54Yc3DsY1qjsPfcA",
#  "BackendApi": "http://83.147.246.223:6000"}

class Config:
    def __init__(self, file):
        self.configFile = file
        self.load_config()
        
    def load_config(self):
        if not path.exists(self.configFile):
            print(f'\033[31mНе удалось найти конфиг файл {self.configFile}. Введите необходимые для работы данные\033[0m')
            sign_in = json.dumps(
                {"TGtoken": str(input("Ваш телеграмм токен: ")), "BackendApi": str(input("Адрес до BackendApi: "))}
            )
            with open(self.configFile, "w") as line:
                line.write(sign_in)
            config_data = json.loads(sign_in)
        else:
            with open(self.configFile, "r") as line:
                config_data = json.loads(line.read())
        self.TGtoken = config_data["TGtoken"]
        self.backendApi = config_data["BackendApi"]

    def get_tokenTG(self):
        return self.TGtoken

    def get_backendApi(self):
        return self.backendApi

if __name__ == "__main__":
    appConfig = Config("bot.config")
    tokenTG = appConfig.get_tokenTG()
    backendApi = appConfig.get_backendApi()
    print(f'ваш токен: {tokenTG}\nваш BackendApi: {backendApi}\n')
