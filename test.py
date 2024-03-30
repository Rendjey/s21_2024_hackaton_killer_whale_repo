from datetime import datetime, timedelta

# Получаем сегодняшнюю дату
today = datetime.now().date()

# Выводим 7 дней, начиная с сегодняшнего дня
for i in range(7):
    print(today + timedelta(days=i))
