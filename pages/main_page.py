from selenium.webdriver.support import expected_conditions as EC
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
