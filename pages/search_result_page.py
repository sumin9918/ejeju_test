# - 검색 테스트 시 검색 결과 확인하는 함수

from selenium.webdriver.common.by import By
from pages.main_page import MainPage

class SearchResultPage(MainPage):
    PRODUCT_NAME = (By.CLASS_NAME, "pro-name")  # 상품명
    PRODUCT_PRICE = (By.CLASS_NAME, "price")  # 가격

    def get_search_results(self):
        # 검색된 상품 정보를 리스트로 반환 (개별 컨테이너 없이 인덱스로 매칭)
        names = self.find_elements(*self.PRODUCT_NAMES)  # 모든 상품명 요소 찾기
        prices = self.find_elements(*self.PRODUCT_PRICES)  # 모든 가격 요소 찾기

        results = []
        num_products = min(len(names), len(prices))  # 가장 적은 요소 수 기준으로 조정

        for i in range(num_products):
            results.append({
                "name": names[i].text.strip(),
                "price": prices[i].text.strip()
            })

        return results
