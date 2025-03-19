import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.webdriver import WebDriver

# - 메인 페이지 열기
# - 검색 (goods 페이지로 이동)
# - 카테고리 (search result 페이지로 이동)


class MainPage:
    URL = "https://mall.ejeju.net/main/index.do"

    def __init__(self, driver: WebDriver):
        self.driver = driver

    # 메인 페이지 열기
    def open(self):
        self.driver.get(self.URL)


    # 상품 검색
    def search_products(self):
        search_btn = self.driver.find_element(By.XPATH, '//*[@id="gnb"]/ul[2]/li[2]/div/span[2]')
        search_btn.click()
        time.sleep(1)

        search_input = self.driver.find_element(By.XPATH, '//*[@id="search-box"]')
        search_input.send_keys("오메기")
        search_input.send_keys(Keys.RETURN)
        time.sleep(3)

    # 상단 카테고리 검색
    def top_menu_chuksan(self):
        chucksan_btn = self.driver.find_element(By.XPATH, '//*[@id="gnb"]/ul[2]/li[1]/ul/li[1]/a')
        chucksan_btn.click()
        time.sleep(3)

    def top_menu_tamnanong(self):
        tamnanogh_btn = self.driver.find_element(By.XPATH, '//*[@id="gnb"]/ul[2]/li[1]/ul/li[2]/a')
        tamnanogh_btn.click()
        time.sleep(3)

    def top_menu_tamnasu(self):
        tamnasu_btn = self.driver.find_element(By.XPATH, '//*[@id="gnb"]/ul[2]/li[1]/ul/li[3]/a')
        tamnasu_btn.click()
        time.sleep(3)

    def top_menu_tamnachuk(self):
        tamnachuk_btn = self.driver.find_element(By.XPATH, '//*[@id="gnb"]/ul[2]/li[1]/ul/li[4]/a')
        tamnachuk_btn.click()
        time.sleep(3)

    def top_menu_tamnagagong(self):
        tamnagagong_btn = self.driver.find_element(By.XPATH, '//*[@id="gnb"]/ul[2]/li[1]/ul/li[5]/a')
        tamnagagong_btn.click()
        time.sleep(3)

    # 히든 카테고리 검색

