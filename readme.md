# Задание
Модуль SQLite
- Создаем базу данных Profile
- Создаем таблицу Cookie Profile:
* Уникальной id для каждой строки (Not NULL)
* Дата и время создания записи (Not NULL)
* Значения Cookie
* Дата и время последнего запуска
* Кол-во всего запусков
- Заполняем таблицу 15 значениями (id, текущая дата и время создания)

Модуль Requests
- GET запросом получаем содержимое страницы (https://news.google.com/home)
- Собираем в массив, ссылки на новости ( пример : https://news.google.com/articles/CBMi….)

Модуль Selenium
- Создаем сессию (если Cookie переданы, передаем их)
- Переходим по рандомной ссылке из массива модуля Requests
- Прокручиваем страницу с рандомной задержкой
- Сохраняем Cookie в SQLite (обновляем значения профиля)
- Закрываем сессию

Модуль Multiprocessing
- Собираем профиля из таблицы Cookie Profile (кол-во потоков)
- Используем Pool для создания потоков на каждый профиль
- Ограничение 5 одновременных потоков

## Инструкция

#### Шаг 1. Клонировать репозиторий себе на компьютер
Введите команду:
```bash
git clone https://github.com/Hovo-93/zm-news-parsing.git
```
#### Шаг 2. Установить все зависимости
```bash
   pip install -r requirements.txt   
```

#### Шаг 3. Скачать [GoogleChrome Driver](https://chromedriver.storage.googleapis.com/index.html?path=112.0.5615.49/)


#### Шаг 4. Создать в клонированной директории файл .env 
```bash
    Указать путь к GoogleChrome драйверу 
    
    Пример:
    CHROME_DRIVER_PATH=/Users/PycharmProjects/NewsInGoogle/ChromeDriver/chromedriver
```
#### Шаг 5. Создать базу и заполнить 15 значениями
```bash
   python fill_db.py
```
#### Шаг 6. Cоздание потоков на каждый профиль
```bash
   python multiprocessing_module.py
```