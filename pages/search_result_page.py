import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver


class SearchResultPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    # 검색 결과에서 상품 정보 가져오기
    def get_search_results(self):
        time.sleep(2)

        products = self.driver.find_elements(By.CSS_SELECTOR, ".goods_list ul li")
        results = []

        for product in products:
            try:
                name = product.find_element(By.CSS_SELECTOR, ".name").text
                price = product.find_element(By.CSS_SELECTOR, ".price").text
                results.append({
                    "name": name,
                    "price": price
                })
            except:
                continue  # 일부 요소가 없을 경우 무시

        return results

    # 로그인 상태에서 검색 결과 가져오기
    def get_logged_in_results(self, main_page):
        main_page.my_page_login()
        time.sleep(2)

        main_page.search_products()
        return self.get_search_results()

    # 로그아웃 상태에서 검색 결과 가져오기
    def get_logged_out_results(self, main_page):
        main_page.my_page_logout()
        time.sleep(2)

        main_page.search_products()
        return self.get_search_results()

    # 로그인/비로그인 상태의 검색 결과 비교
    def compare_results(self, logged_in_results, logged_out_results):
        if logged_in_results == logged_out_results:
            print("로그인 상태와 비로그인 상태에서 검색 결과가 동일.")
        else:
            print("로그인 상태와 비로그인 상태에서 검색 결과가 다름")
            print("로그인 상태 결과:", logged_in_results)
            print("비로그인 상태 결과:", logged_out_results)
