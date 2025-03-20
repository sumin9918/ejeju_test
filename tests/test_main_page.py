import time
import pytest

from selenium import webdriver
from pages.main_page import MainPage
from selenium.webdriver.support.ui import WebDriverWait as ws
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException

from pages.main_page import MainPage

""" 
실행방법
- pytest tests/test_main_page.py
"""


# @pytest.mark.usefixtures("driver")
# class TestMainPage:
#     # @pytest.mark.skip(reason="아직 테스트 케이스 발동 안함")
#     def test_open_main_page(self, driver: WebDriver):
#         try:
#             main_page = MainPage(driver)
#             main_page.open()
#
#             ws(driver, 10).until(EC.url_contains("mall.ejeju.net"))
#             assert "mall.ejeju.net" in driver.current_url
#
#             time.sleep(2)
#
#         except NoSuchElementException as e:
#             assert False


#여기서부터
@pytest.fixture
def driver():
    """Chrome WebDriver를 설정하는 pytest fixture"""
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_open_main_page(driver):
    """메인 페이지가 정상적으로 열리는지 확인"""
    main_page = MainPage(driver)
    main_page.open()

    assert "이제주" in driver.title, "❌ 메인 페이지가 정상적으로 열리지 않았습니다."
    print("✅ 메인 페이지가 정상적으로 열렸습니다.")


def test_search_products(driver):
    """상품 검색 기능 테스트"""
    main_page = MainPage(driver)
    main_page.open()

    main_page.search_products()

    # 검색 결과 페이지가 열렸는지 확인
    assert "search" in driver.current_url, "❌ 검색 결과 페이지로 이동하지 않았습니다."
    print("✅ 상품 검색이 정상적으로 동작했습니다.")


def test_category_navigation(driver):
    """카테고리 이동 기능 테스트"""
    main_page = MainPage(driver)
    main_page.open()

    categories = [
        ("카테고리(축산)", main_page.top_menu_chuksan),
        ("카테고리(탐나는농장)", main_page.top_menu_tamnanong),
        ("카테고리(탐나는수산)", main_page.top_menu_tamnasu),
        ("카테고리(탐나는축산)", main_page.top_menu_tamnachuk),
        ("카테고리(탐나는가공)", main_page.top_menu_tamnagagong),
    ]

    for name, category_func in categories:
        category_func()
        assert "category" in driver.current_url, f"❌ {name} 이동 실패"
        print(f"{name} 이동 성공")

