import time
import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as ws
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException

from pages.login_page import LoginPage
from pages.cart_page import CartPage
from pages.cart_page import CartModal
from login_info import LOGIN_INFO

""" 
실행방법
- pytest tests/test_cart.py
"""

"""
[장바구니 테스트]

[사전 조건]
- 로그인 계정 장바구니에 미리 상품을 추가
- 로그인 정보는 공용 로그인으로 해주세요

[테스트케이스 목록]
1. 장바구니 상품 확인 테스트
    - 장바구니에서 상품 확인
    - 장바구니에 상품을 추가하는 함수가 만들어지면 후에 장바구니에 상품을 추가하는 로직 추가
2. 상품 수량 테스트
    - 상품의 수량이 추가, 감소되는지 확인
3. 상품 옵션 수정 테스트
    - 상품 옵션을 모달을 통해 수정한 뒤 변경되었는지 확인
4. 상품 삭제 테스트
    - 상품을 삭제하고 삭제되었는지 확인

"""

# @pytest.mark.skip(reason="에러 발생")


# 임시 로그인 함수
def login(driver: WebDriver):
    login_page = LoginPage(driver)

    # 로그인 페이지 열기
    login_page.login_open()

    ws(driver, 10).until(EC.url_contains("login"))
    ws(driver, 10).until(EC.element_to_be_clickable((By.NAME, "id")))

    # 로그인
    id_input = driver.find_element(By.NAME, "id")
    password_input = driver.find_element(By.NAME, "pw")
    login_btn = driver.find_element(By.XPATH, "//input[@value='로그인']")

    id_input.send_keys(LOGIN_INFO["id"])
    password_input.send_keys(LOGIN_INFO["password"])
    login_btn.click()

    print("✅ 로그인 완료")


@pytest.mark.usefixtures("driver")
class TestCart:
    """
    Test Data (장바구니 상품)
    - 이름 : [이제주] 블루탐 오메기떡 60g(오메기,흑임자,귤,크림치즈)
    - 옵션 : 블루탐 혼합4종 20개입
    - 수량 : 1
    - https://mall.ejeju.net/goods/detail.do?gno=30516&cate=31043
    """

    # Test Data
    TEST_GOODS_NAME = "[이제주] 블루탐 오메기떡 60g(오메기,흑임자,귤,크림치즈)"

    # constants
    GOODS_NAMES_STRONG_XPATH = "//p[@class='txt']/a/strong"
    QUANTITY_INPUT_XPATH = "//input[@title='수량']"

    # 장바구니 상품 확인 테스트
    @pytest.mark.skip(reason="아직 테스트 케이스 발동 안함")
    def test_confirm_cart_goods(self, driver: WebDriver):
        try:
            # 로그인
            login(driver)

            # 장바구니 페이지 이동
            cart_page = CartPage(driver)
            cart_page.open()

            ws(driver, 10).until(
                EC.url_contains("https://mall.ejeju.net/order/cart.do")
            )

            time.sleep(2)

            # 상품 이름 확인
            goods_names = [
                goods_name.get_attribute("textContent").strip()
                for goods_name in driver.find_elements(
                    By.XPATH, self.GOODS_NAMES_STRONG_XPATH
                )
            ]

            # 장바구니에 있는 상품들 중 TEST_GOODS_NAME과 같은 이름이 있는지 확인
            assert self.TEST_GOODS_NAME in goods_names

        except NoSuchElementException as e:
            driver.save_screenshot("error_at_tc1.png")
            assert False

    # 상품 수량 테스트
    def test_change_quantity(self, driver: WebDriver):
        try:
            # 로그인
            login(driver)

            # 장바구니 페이지 이동
            cart_page = CartPage(driver)
            cart_page.open()

            ws(driver, 10).until(
                EC.url_contains("https://mall.ejeju.net/order/cart.do")
            )

            time.sleep(2)

            # 상품 수량 증가 테스트
            quantity = driver.find_element(By.XPATH, self.QUANTITY_INPUT_XPATH)
            before_increase_quantity = int(quantity.get_attribute("value"))

            print(f"수량 증가 전: {before_increase_quantity}")

            cart_page.increase_quantity()  # 1 증가

            # 증가 반영될 때까지 기다리기 (바로 새로고침 X)
            ws(driver, 10).until(
                lambda d: int(
                    d.find_element(By.XPATH, self.QUANTITY_INPUT_XPATH).get_attribute(
                        "value"
                    )
                )
                == before_increase_quantity + 1
            )

            quantity = driver.find_element(By.XPATH, self.QUANTITY_INPUT_XPATH)
            after_increase_quantity = int(quantity.get_attribute("value"))

            print(f"수량 증가 후: {after_increase_quantity}")

            assert before_increase_quantity + 1 == after_increase_quantity

            time.sleep(2)

            # 상품 수량 감소 테스트
            quantity = driver.find_element(By.XPATH, self.QUANTITY_INPUT_XPATH)
            before_decrease_quantity = int(quantity.get_attribute("value"))

            print(f"수량 감소 전: {before_decrease_quantity}")

            cart_page.decrease_quantity()  # 1 감소

            # 감소 반영될 때까지 기다리기
            ws(driver, 10).until(
                lambda d: int(
                    d.find_element(By.XPATH, self.QUANTITY_INPUT_XPATH).get_attribute(
                        "value"
                    )
                )
                == before_decrease_quantity - 1
            )

            quantity = driver.find_element(By.XPATH, self.QUANTITY_INPUT_XPATH)
            after_decrease_quantity = int(quantity.get_attribute("value"))

            print(f"수량 감소 후: {after_decrease_quantity}")

            assert before_decrease_quantity - 1 == after_decrease_quantity

        except NoSuchElementException as e:
            driver.save_screenshot("error_at_tc2.png")
            assert False

    # 3. 모달 테스트
    # - 로그인
    # - 장바구니 페이지 이동
    # - 수정 클릭 -> 모달 열기
    # - 옵션 선택
    # - 확인
    # - 옵션 변경 확인

    # 4. 삭제
    # - 로그인
    # - 장바구니 페이지 이동
    # - 삭제 클릭
    # - 상품 확인
