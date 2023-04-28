import os
import random
import time
from datetime import datetime

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from http.cookies import SimpleCookie
from reuqests_module import get_article_links
from connect_db import DatabaseConnection
from dotenv import load_dotenv

load_dotenv(dotenv_path='.env')


def set_cookie(cookieStr, driver):
    cookie = SimpleCookie()
    cookie.load(cookieStr)

    for k, v in cookie.items():
        driver.add_cookie({"name": k, "value": v.value})


def runner(cookie_profile):
    db = DatabaseConnection()
    conn = db.get_connection()
    cursor = conn.cursor()
    # create a Service object
    service = Service(os.getenv('CHROME_DRIVER_PATH'))

    driver = webdriver.Chrome(service=service)

    links = get_article_links()
    print(links)
    scroll_random_time = random.uniform(1, 2)

    """ Получение Cookie из базы """

    cookieStr = cookie_profile['value_cookie']

    # Выбираем случайную новость из массива ссылок
    random_link = random.choice(links)

    try:
        driver.get(random_link)

        if len(cookieStr) != 0:
            set_cookie(cookieStr, driver)
            driver.get(random_link)

        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(scroll_random_time)
        cookie_value = driver.execute_script("return document.cookie")
        cookieStr = cookie_value
        current_time = datetime.now()
        cursor.execute(
            "UPDATE cookie_profile SET value_cookie = ?,date_time_last_run=?,count_run=count_run+1 WHERE id = ?",
            (cookieStr, current_time, cookie_profile['id']))
        conn.commit()

    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()
