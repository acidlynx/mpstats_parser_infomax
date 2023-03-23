import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

DRIVER_PATH = r'drivers/chromedriver.exe'
USER_DATA_DIR = r'Default'
CHROME_PROFILE_NAME = r'Default'
CHROME_PROFILE_PATH = r'C:\Users\eugen\AppData\Local\Google\Chrome\User Data'           # main
WB_URL = r'https://seller.wildberries.ru/'


# Настройте параметры профиля для сохранения данных в нем
options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
# options.add_argument("disable-infobars")
options.add_argument("--disable-extensions")
# options.add_argument("--no-sandbox")
# options.add_argument("--disable-dev-shm-usage")
# options.add_argument('--allow-profiles-outside-user-dir')
# options.add_argument('--enable-profile-shortcut-manager')
# options.add_argument(f"--user-data-dir={CHROME_PROFILE_PATH}")      # ссылка на папку, c профилями Chrome
# options.add_argument(f"--profile-directory={CHROME_PROFILE_NAME}")  # имя папки профиля Chrome

s = Service(executable_path=DRIVER_PATH)
driver = webdriver.Chrome(service=s, options=options)


def open_window(url: str) -> str:
    '''
    Open browser window and return it'd ID
    :param url: gets url to open window
    :return: window id to manipulate
    '''
    try:
        # driver.maximize_window()
        driver.get(url)
        # time.sleep(5)
        return driver.current_window_handle         # возвращаем ID текущего открытого окна
    except Exception as ex:
        print(ex)


def close_window(handler):
    driver.switch_to.window(handler)
    driver.close()
    driver.quit()


if __name__ == '__main__':
    pass




#
# try:
#     driver.maximize_window()
#     driver.get(WB_URL)
#     time.sleep(50)
# except Exception as ex:
#     print(ex)
# finally:
#     driver.close()
#     driver.quit()
