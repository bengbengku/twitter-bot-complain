from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

PROMISE_DOWN = 35
PROMISE_UP = 10
CHROME_DRIVER_PATH = "C:\Development\chromedriver.exe"
LEN_CHAR = 280

s = Service(CHROME_DRIVER_PATH)
options = Options()
options.add_argument("start-maximized")


class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome(service=s, options=options)
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        try:
            self.driver.get("https://www.speedtest.net/id")
            button_speed = self.driver.find_element(
                By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')
            button_speed.click()
            time.sleep(50)
        except:
            pass
        finally:
            text_down = self.driver.find_element(
                By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
            text_up = self.driver.find_element(
                By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span').text
            self.down = float(text_down)
            self.up = float(text_up)

    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/i/flow/login")
        text_template = f"Bandwith for: Download {self.down}, Upload {self.up}"

        try:
            input_username = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.NAME, 'text'))
            )

            input_username.send_keys("USERNAME")
            input_username.send_keys(Keys.ENTER)
            time.sleep(3)
        finally:
            input_username = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.NAME, 'password'))
            )

            input_username.send_keys("YOUR PASSWORD")
            input_username.send_keys(Keys.ENTER)

        try:
            tweet = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div/span'))
            )
        finally:
            tweet.send_keys(f"{text_template}")


main_ = InternetSpeedTwitterBot()

main_.get_internet_speed()

if main_.down < PROMISE_DOWN and main_.up < PROMISE_UP:
    main_.tweet_at_provider()
