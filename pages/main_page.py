import time
import login_info
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains

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

    # 마이페이지
    def top_menu_my_page(self):
        my_page_btn = self.driver.find_element(By.XPATH, '//*[@id="gnb"]/ul[2]/li[2]/div/span[3]/a')
        my_page_btn.click()
        time.sleep(3)

    # 로그인
    def my_page_login(self):
        login_username = self.driver.find_element(By.XPATH, '//*[@id="member_id"]')
        login_username.send_keys(login_info.USERNAME)
        time.sleep(1)

        login_password = self.driver.find_element(By.XPATH, '//*[@id="member_pw"]')
        login_password.send_keys(login_info.PASSWORD)
        time.sleep(1)

        login_btn = self.driver.find_element(By.XPATH, '//*[@id="login_box"]/div[1]/div/div[1]/fieldset/span/input')
        login_btn.click()
        time.sleep(3)

    # 마이페이지 마우스 호버 후 로그아웃
    def my_page_logout(self):
        my_page_btn = self.driver.find_element(By.XPATH, '//*[@id="gnb"]/ul[2]/li[2]/div/span[3]/a')

        actions = ActionChains(driver)
        actions.move_to_element(my_page_btn).perform()
        time.sleep(1)

        logout_btn = self.driver.find_element(By.XPATH, '//*[@id="gnb"]/ul[2]/li[2]/div/span[3]/div/ul/li[1]/a')
        logout_btn.click()
        time.sleep(3)

