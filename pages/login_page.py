# - login 페이지 이동
# - 로그인
# - 로그아웃
from login_info import LOGIN_INFO
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
import time
class LoginPage:

    Main_URL = "https://mall.ejeju.net/main/index.do"
    Login_URL = "https://mall.ejeju.net/member/login.do"

    def __init__(self, driver: WebDriver):
        self.driver = driver

    # 메인 페이지 열기
    def main_open(self):
        self.driver.get(self.Main_URL)

    def login_open(self):
        self.driver.get(self.Login_URL)

    def hover_mypage(self):
        hover_mypage = self.driver.find_element(By.XPATH,'//*[@id="gnb"]/ul[2]/li[2]/div/span[3]/a')
        actions = ActionChains(self.driver)
        actions.move_to_element(hover_mypage).perform()

    def move_to_login_page(self):
        self.hover_mypage()
        time.sleep(1.5)
        hover_login = self.driver.find_element(By.XPATH,'//*[@id="gnb"]/ul[2]/li[2]/div/span[3]/div/ul/li[1]/a')
        hover_login.click()
        

    def login_process(self):
        user_id = LOGIN_INFO["id"]
        user_password = LOGIN_INFO["password"]
        id_input = self.driver.find_element(By.NAME,"id")
        password_input = self.driver.find_element(By.NAME,"pw")
        login_btn = self.driver.find_element(By.XPATH,"//input[@value='로그인']")
        id_input.send_keys(user_id)
        password_input.send_keys(user_password)
        self.driver.implicitly_wait(5)
        login_btn.click()
        self.driver.implicitly_wait(5)
        self.hover_mypage()
        self.driver.implicitly_wait(5)
        btn_name = self.driver.find_element(By.XPATH,'//*[@id="gnb"]/ul[2]/li[2]/div/span[3]/div/ul/li[1]/a')
        return btn_name.text
    
    def logout_process(self):
        self.login_process()
        btn_name = self.driver.find_element(By.XPATH,'//*[@id="gnb"]/ul[2]/li[2]/div/span[3]/div/ul/li[1]/a')
        btn_name.click()
        self.driver.implicitly_wait(5)
        self.hover_mypage()
        self.driver.implicitly_wait(5)
        btn_name = self.driver.find_element(By.XPATH,'//*[@id="gnb"]/ul[2]/li[2]/div/span[3]/div/ul/li[1]/a')
        return btn_name.text