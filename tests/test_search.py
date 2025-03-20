# import 오류

import pytest
from selenium import webdriver
from pages.main_page import MainPage
# search_result_page에서 발생
from pages.search_result_page import SearchResultPage


def setup_module(module):
    global driver
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)


def teardown_module(module):
    driver.quit()


@pytest.fixture
def main_page():
    return MainPage(driver)


@pytest.fixture
def search_result_page():
    return SearchResultPage(driver)


def test_compare_search_results(main_page, search_result_page):
    main_page.open()

    # 로그인 상태에서 검색 결과 가져오기
    logged_in_results = search_result_page.get_logged_in_results(main_page)

    # 로그아웃 상태에서 검색 결과 가져오기
    logged_out_results = search_result_page.get_logged_out_results(main_page)

    # 검색 결과 비교
    assert logged_in_results == logged_out_results, "로그인 상태와 비로그인 상태의 검색 결과가 다릅니다!"
