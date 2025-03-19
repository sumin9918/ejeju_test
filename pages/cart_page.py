import time

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as ws
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

# - cart 페이지 이동 (방법 1, 2, 3 중 택1)
#   방법 1. mypage 이동 -> 장바구니 클릭
#   방법 2. 사람 아이콘(?)에 hover -> 장바구구니 클릭
#   방법 3. url 이동
# - 갯수 변경
# - 옵션 수정
# - 삭제


class MainPage:
    URL = "https://mall.ejeju.net/order/cart.do"
    DECREASE_BUTTON_CLASSNAME = "down"
    INCREASE_BUTTON_CLASSNAME = "up"

    def __init__(self, driver: WebDriver):
        self.driver = driver

    # 장바구니 페이지 열기
    def open_cart(self):
        self.driver.get(self.URL)

    # 장바구니 페이지 이동 (추후 개발 예정)

    # 수량 변경
    # 수량 증가 함수
    def increase_quantity(self):
        increase_buttons = self.driver.find_elements(
            By.CLASS_NAME, self.INCREASE_BUTTON_CLASSNAME
        )
        increase_button = increase_buttons[0]  # 증가 버튼들 중 첫번째 요소를 선택
        increase_button.click()

    # 수량 감소 함수
    def decrease_quantity(self):
        decrease_buttons = self.driver.find_elements(
            By.CLASS_NAME, self.DECREASE_BUTTON_CLASSNAME
        )
        decrease_button = decrease_buttons[0]  # 감소 버튼들 중 첫번째 요소를 선택
        decrease_button.click()

    # 옵션 수정
    # 삭제
    # 선택삭제하기
    # 전체삭제하기
