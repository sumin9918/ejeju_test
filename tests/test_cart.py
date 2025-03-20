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
2. 상품 최대, 최소 수량 확인 테스트
    - 상품의 수량을 최대, 최소로 수량으로 변경했을 때 경고 문구 확인
3. 상품 옵션 수정 테스트
    - 상품 옵션을 모달을 통해 수정한 뒤 변경되었는지 확인
4. 상품 삭제 테스트
    - 상품을 삭제하고 삭제되었는지 확인

"""

# @pytest.mark.skip(reason="아직 테스트 케이스 발동 안함")


# 임시 로그인 함수
def login(driver: WebDriver):
    login_page = LoginPage(driver)

    # 로그인 페이지 열기
    login_page.login_open()

    ws(driver, 10).until(EC.url_contains("login"))

    # 로그인
    check_is_login_text = login_page.login_process()

    # check_is_login_text가 로그아웃이면 로그인 된 것
    assert check_is_login_text == "로그아웃"

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

    # 장바구니 추가 테스트
    def test_open_main_page(self, driver: WebDriver):
        try:
            # 로그인
            login(driver)

            # 장바구니 페이지 이동
            cart_page = CartPage(driver)
            cart_page.open()

            ws(driver, 10).until(EC.url_contains("cart"))
            assert "cart" in driver.current_url

            time.sleep(2)

            # 상품 이름 확인
            goods_names = [
                goods_name.text
                for goods_name in self.driver.find_elements(
                    By.XPATH, self.GOODS_NAMES_STRONG_XPATH
                )
            ]

            # 장바구니에 있는 상품들 중 TEST_GOODS_NAME과 같은 이름이 있는지 확인
            assert self.TEST_GOODS_NAME in goods_names

        except NoSuchElementException as e:
            assert False

    # 2. 갯수 변경 테스트
    # - 로그인
    # - 장바구니 페이지 이동
    # - 갯수 증가 (최대치)
    # - 경고 문구 확인
    # - 갯수 감소 (최소치)
    # - 경고 문구 확인

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
