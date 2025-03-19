import time
import pytest

from selenium.webdriver.support.ui import WebDriverWait as ws
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException

from pages.main_page import MainPage

""" 
실행방법
- pytest tests/test_main_page.py
"""


@pytest.mark.usefixtures("driver")
class TestMainPage:
    # @pytest.mark.skip(reason="아직 테스트 케이스 발동 안함")
    def test_open_main_page(self, driver: WebDriver):
        try:
            main_page = MainPage(driver)
            main_page.open()

            ws(driver, 10).until(EC.url_contains("mall.ejeju.net"))
            assert "mall.ejeju.net" in driver.current_url

            time.sleep(2)

        except NoSuchElementException as e:
            assert False
