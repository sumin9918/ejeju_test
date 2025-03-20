import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys

# 우선 Goods Detail 확인을 위해 아래의 Url 체크 
class GoodsDetail:
    Url = "https://mall.ejeju.net/main/index.do" # 이후에 변경될 수 있음

    def __init__(self, driver):
        self.driver = driver

    # 메인 페이지 열기
    def open_page(self):
        self.driver.get(self.Url)

    time.sleep(5)

    # 상품 클릭 (첫번째 아이템)
    def click_on_first_product(self):
        try:
            # 배너를 선택하고 클릭
            first_product = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div[3]/div[2]/div[1]/section[1]/ul/li[1]/a[2]"))
            )
            first_product.click()
            print("배너를 성공적으로 클릭했습니다!")
        except Exception as e:
            print(f"배너 클릭 중 오류 발생! : {e}")
            raise

################ 일단 첫 번째 상품 선택은 뭐때문인지 클릭이 안돼서 다음으로 넘김 ################

    # 상품 상세 페이지 정상 진입 여부 확인 (URL 확인)
    def verify_goods_detail_page(self, expected_url):
        try: # 지정된 URL로의 이동 확인
            WebDriverWait(self.driver, 10).until(
                EC.url_to_be(expected_url)
            )
            current_url = self.driver.current_url
            assert current_url == expected_url, f"Expected {expected_url}, but got {current_url}"
            print("상세 페이지 진입 성공!")
        except Exception as e: 
            print(f"상세 페이지 진입 시도 중 오류가 발생했습니다!: {e}")
            raise

    # 상품 상세 페이지로 URL 직접 이동 (대체 옵션)
    def navigate_to_goods_detail(self):
        self.driver.get(self.Url)

################ 일단 첫 번째 상품 선택은 뭐때문인지 클릭이 안돼서 다음으로 넘김 ################

    # 찜 하기
    def add_to_wish(self):
        try: # 찜하기 버튼의 요소를 찾고 클릭하기
            wish_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/div/div[1]/form[2]/div[3]/div[2]/div[5]/div[1]/button[1]'))
                )
            wish_button.click()
            print("찜하기 버튼을 성공적으로 클릭했습니다!")
        except Exception as e:
            print(f"찜하기 버튼 클릭 중 오류 발생! : {e}")
            raise
    
    #찜하기 팝업 종료하기
    def close_favorite_popup(self):
        try:
            #팝업이 나타날 때까지 기다리기
            popup_element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="pop_favorite_add_info"]'))
            )
            # 팝업 종료 버튼 클릭
            close_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="pop_favorite_add_info"]/div/div/div[2]/a[2]'))
            )
            close_button.click()
            print("팝업 종료 버튼을 성공적으로 클릭했습니다!")
        except Exception as e:
            print(f"팝업 종료 중 오류 발생! : {e}")
            raise

################ 옵션 변경이 있는 상품을 찾아야 함 ################

    # # 상품 옵션 변경
    # def change_option(self, option_locator, value):
    #     option_element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, option_locator)))
    #     option_element.click()
    #     option_choice = self.driver.find_element(By.XPATH, f"//option[@value='{value}']")
    #     option_choice.click()


################ 옵션 변경이 있는 상품을 찾아야 함 ################

    # 갯수 조절
    def increase_ea(self, times):
        try:
            increase_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/div/div[1]/form[2]/div[3]/div[2]/div[4]/div[1]/div[2]/span/span/button[2]'))
            )
            for 4 in range(times):
                increase_button.click()
                print("수량 증가 버튼을 클릭했습니다!")
        except Exception as e:
            print(f"수량 증가 중 오류 발생!: {e}")
            raise


    # # 장바구니 담기
    # def add_to_cart(self):
    #     add_to_cart_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, "add-to-cart-button")))
    #     add_to_cart_button.click()


if __name__ == "__main__":
   # Chrome 브라우저 초기화
    driver = webdriver.Chrome()
    
    try:
    # GoodsDetail 클래스 초기화
        goods_detail = GoodsDetail(driver)
        # 메인 페이지 열기
        goods_detail.open_page()
        #상품 클릭 (CSS Selector 사용)
        goods_detail.click_on_product()
        # 상세 페이지 이동 확인
        # goods_detail.verify_goods_detail_page("https://mall.ejeju.net/goods/detail.do?gno=10492&cate=31040")

    finally:
        # 브라우저 종료
        driver.quit()