import pytest
from selenium.webdriver.support.ui import WebDriverWait as ws
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage

@pytest.mark.usefixtures("driver")
class TestLoginPage:
    @pytest.mark.skip(reason="일단 넘김")
    def test_move_to_login_page(self, driver: WebDriver):
        main_page = LoginPage(driver)
        main_page.main_open()
        ws(driver, 10).until(EC.url_contains("mall.ejeju.net"))
        main_page.move_to_login_page()
        driver.implicitly_wait(5)
        assert "https://mall.ejeju.net/member/login.do" in driver.current_url #로그인 페이지로 이동되었는지 검증

    @pytest.mark.skip(reason="일단 넘김")
    def test_login_process(self, driver: WebDriver):
        login_page = LoginPage(driver)
        login_page.login_open()
        ws(driver, 10).until(EC.url_contains("mall.ejeju.net"))
        btn_text = login_page.login_process()
        assert btn_text == "로그아웃" #로그인 되었는지 검증, 로그인 상태이기에 로그아웃으로 나와야 함

    @pytest.mark.skip(reason="일단 넘김")
    def test_logout_process(self, driver: WebDriver):
        login_page = LoginPage(driver)
        login_page.login_open()
        ws(driver, 10).until(EC.url_contains("mall.ejeju.net"))
        btn_text = login_page.logout_process()
        assert btn_text == "로그인" #로그아웃 후 로그인 되었는지 검증, 로그아웃 상태이기에 로그인으로 나와야 함