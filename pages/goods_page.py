from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

import logging

logging.basicConfig(level=logging.INFO)
logging.info("메인 페이지에 성공적으로 접속했습니다.")
logging.error(f"메인 페이지 접속 중 오류 발생!:{e}")

class GoodsPage:
    def __init__(self, driver):
        self.driver = driver

    # 1. 우선 메인 페이지로 이동하기
    def navigate_to_main_page(self):
        try:
            self.driver.get("https://mall.ejeju.net/main/index.do")
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.TAG_NAME, "body"))
            )
            print("메인 페이지에 성공적으로 접속했습니다!")
        except Exception as e:
            print(f"메인 페이지 접속 중 오류 발생! : {e}")
            raise

    # 2. 페이지 헤더의 카테고리 클릭 (농산물)
    def click_category(self):
        try:
            category_element = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "#gnb > ul.gnb_main > li.top_menu > ul > li.active > a"))
            )
            category_element.click()
            print("농산물 카테고리를 클릭했습니다!")
        except Exception as e:
            print(f"카테고리 클릭 중 오류 발생: {e}")
            raise
    
    # 3. 카테고리 내 감귤/만감류 선택
    def select_citrus_category(self):
        try:
            citrus_category = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "#wrap_container > div.wrap_content > nav > ul > li:nth-child(3) > a"))
            )
            citrus_category.click()
            print("감귤/만감류 카테고리를 클릭했습니다.")
        except Exception as e:
            print(f"카테고리 클릭 중 오류 발생! :{e}")
            raise
    
    # 4. 리스트의 상품 확인 (한라봉 or 천혜향이 검색된 아이템에 포함되어 있는지 여부 확인) < 이 부분은 Coupang 테스트 참고해서 수정해야겠다.
    def verify_citrus_products(self):
        try:
            product_elements = WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#wrap_container .product_name"))
            )
            valid_products = [elem.text for elem in product_elements if "한라봉" in elem.text or "천혜향" in elem.text]

            if valid_products:
                print(f"감귤/만감류 확인 성공: {valid_products}")
            else:
                print("감귤/만감류 확인 실패: 상품 목록에 해당 상품이 없습니다.")
        except Exception as e:
            print(f"상품 확인 중 오류 발생: {e}")
            raise

    # 5. 필터 적용
    def apply_sorting_filter(self, sort_option_css_selector):
        try: # 필터 버튼 클릭 (이름 순)
            filter_button = WebDriverWait(self.driver, 10).until(
                EC. element_to_be_clickable((By.CSS_SELECTOR, sort_option_css_selector))
            )
            filter_button.click()
            print(f"필터를 성공적으로 적용했습니다! : {sort_option_css_selector}")
        except Exception as e:
            print(f"상품 정렬 필터 적용 중 오류 발생!: {e}")
            raise
  
if __name__ == "__main__":
    try:
        driver = webdriver.Chrome()
        goods_page = GoodsPage(driver)

        # 1. 메인 페이지로 이동
        goods_page.navigate_to_main_page()

        # 2. 페이지 헤더의 카테고리 클릭 (농산물)
        goods_page.click_category()

        # 3. 농산물 카테고리 내 감귤/만감류 선택
        goods_page.select_citrus_category()

        # 4. 출력된 상품 확인
        goods_page.verify_citrus_products()

        # 5. 정렬 필터 
        goods_page.apply_sorting_filter("#wrap_container > div > div.sub_layout > form > div.totalSrch_top > div > ul > li:nth-child(6) > a")

    except Exception as e:
        print(f"프로세스 실행 중 오류 발생: {e}")

    finally:
        if 'driver' in locals():
            driver.quit()
