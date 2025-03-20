# 검색 시나리오
# - 비로그인 상태 검색 테스트
# - 로그인 상태 검색 테스트

import pytest
from selenium import webdriver
from pages.main_page import MainPage
from pages.search_result import SearchResultPage


@pytest.fixture
def driver():
    #Chrome WebDriver를 설정하는 pytest fixture
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_search_logged_out(driver):
    # 비로그인 상태에서 검색 실행 및 결과 확인
    main_page = MainPage(driver)
    main_page.open()

    main_page.search_products()
    search_result_page = SearchResultPage(driver)
    results = search_result_page.get_search_results()

    assert results, "검색 결과가 없습니다."
    print(f"비로그인 검색 결과: {len(results)}개 상품")


def test_search_logged_in(driver):
    # 로그인 후 검색 실행 및 결과 확인
    main_page = MainPage(driver)
    main_page.open()

    # 로그인 추가 (로그인 페이지 구현 필요)
    #main_page.login("your_username", "your_password")

    main_page.search_products()
    search_result_page = SearchResultPage(driver)
    results = search_result_page.get_search_results()

    assert results, "로그인 상태에서 검색 결과가 없습니다."
    print(f"로그인 후 검색 결과: {len(results)}개 상품")


def test_compare_search_results(driver):
    #로그인/비로그인 상태에서 검색 결과 비교
    main_page = MainPage(driver)

    # 비로그인 상태에서 검색
    main_page.open()
    main_page.search_products()
    search_result_page = SearchResultPage(driver)
    logged_out_results = search_result_page.get_search_results()

    # 로그인 후 검색
    main_page.open()
    main_page.login("your_username", "your_password")  # 로그인 필요
    main_page.search_products()
    logged_in_results = search_result_page.get_search_results()

    # 검색 결과 비교
    assert logged_out_results == logged_in_results, "로그인/비로그인 검색 결과가 다릅니다!"
    print("로그인/비로그인 상태에서 동일한 검색 결과가 나왔습니다.")

