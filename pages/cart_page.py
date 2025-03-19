import time

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as ws
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class CartPage:
    URL = "https://mall.ejeju.net/order/cart.do"
    DECREASE_BUTTON_CLASSNAME = "down"
    INCREASE_BUTTON_CLASSNAME = "up"
    DELETE_BUTTON_XPATH = "//button[text()='삭제']"

    def __init__(self, driver: WebDriver):
        self.driver = driver

    # 장바구니 페이지 열기
    def open(self):
        self.driver.get(self.URL)

    # 장바구니 페이지 이동 (추후 개발 예정)
    # - cart 페이지 이동 (방법 1, 2 중 택1)
    #   방법 1. mypage 이동 -> 장바구니 클릭
    #   방법 2. 사람 아이콘(?)에 hover -> 장바구구니 클릭

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

    # 삭제
    def delete_goods(self):
        delete_buttons = self.driver.find_elements(By.XPATH, self.DELETE_BUTTON_XPATH)
        delete_button = delete_buttons[0]  # 삭제 버튼들 중 첫번째 요소를 선택
        delete_button.click()

    # 선택삭제하기
    # 전체삭제하기


# 장바구니 수정 모달
# - wish 페이지에 있다고 가정
class CartModal:
    MODIFY_BUTTON_XPATH = "//button[text()='수정']"
    TITLE_H4_XPATH = "//h4[@class='title']"
    CLOSE_A_XPATH = "//a[@class='pop_close']"

    def __init__(self, driver: WebDriver):
        self.driver = driver

    # 모달 열림
    def open(self):

        # test_wish에서 검사할 내용

        # 현재 장바구니 페이지에 있는지 검사
        # assert "wish" in self.driver.current_url

        # 장바구니에 상품이 있는지 검사
        # assert len(self.driver.find_elements(By.CLASS_NAME, "ui_goods_tmp")) > 0

        modify_buttons = self.driver.find_elements(By.XPATH, self.MODIFY_BUTTON_XPATH)
        modify_button = modify_buttons[0]  # 수정 버튼들 중 첫번째 요소를 선택
        modify_button.click()

        # 장바구니 수정 Modal이 열렸는지 확인
        title = self.driver.find_element(By.XPATH, self.TITLE_H4_XPATH)

        assert title.text == "장바구니 수정"

    # 모달 닫힘
    def close(self):
        close_button = self.driver.find_element(By.XPATH, self.CLOSE_A_XPATH)
        close_button.click()

    # 수량 변경
    # 옵션 변경
    # 확인
    # 창닫기
