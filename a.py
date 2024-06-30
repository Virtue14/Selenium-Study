# 셀레늄 웹드라이버
from selenium import webdriver

# 웹드라이버 객체 생성시 수반될 서비스나 옵션
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# 선택지 및 키보드 입력
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

########################################################################

# 웹드라이버 매니저 모듈 import
from webdriver_manager.chrome import ChromeDriverManager
# 기타 모듈
import time

########################################################################

# 서비스 변수 생성
customService = Service(ChromeDriverManager().install())
# 옵션 변수 생성
customOption = Options()

# 드라이버 객체 생성
browser = webdriver.Chrome(service = customService, options = customOption)

########################################################################

# URL get 요청
URL = 'https://naver.com/'

browser.get(URL)
browser.implicitly_wait(10) # 요소가 로드될 때까지 최대 10초간 기다림

time.sleep(3) # 3초간 명시적으로 대기