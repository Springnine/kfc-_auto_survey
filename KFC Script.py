from selenium import webdriver
from selenium.webdriver.common.keys import Keys

Coupon = input("쿠폰 입력 :")

# Chrome 웹 드라이버 생성
driver = webdriver.Chrome('C:\chromedriver.exe')

# url 로딩
driver.get('https://s.kfcvisit.com/kor')

elem = driver.find_element_by_id("NextButton")
elem.click()


# 쿠폰 입력
elem = driver.find_element_by_id("InputCouponNum")
elem.send_keys(Coupon)
elem = driver.find_element_by_id("NextButton")
elem.click()

	
# 1번 설문
elem = driver.find_element_by_id("R001000.2")
driver.execute_script("arguments[0].click();", elem)
elem = driver.find_element_by_id("R002000.3")
driver.execute_script("arguments[0].click();", elem)
elem = driver.find_element_by_id("NextButton")
elem.click()

# 2번 설문
elem = driver.find_element_by_id("R000242.4")
driver.execute_script("arguments[0].click();", elem)
elem = driver.find_element_by_id("NextButton")
elem.click()	

# 3번 설문
elem = driver.find_element_by_id("R004000.5")
driver.execute_script("arguments[0].click();", elem)
elem = driver.find_element_by_id("NextButton")
elem.click()	

# 4번 설문
elem = driver.find_element_by_id("R020000.5")
driver.execute_script("arguments[0].click();", elem)
elem = driver.find_element_by_id("R009000.5")
driver.execute_script("arguments[0].click();", elem)
elem = driver.find_element_by_id("R007000.5")
driver.execute_script("arguments[0].click();", elem)
elem = driver.find_element_by_id("R013000.5")
driver.execute_script("arguments[0].click();", elem)
elem = driver.find_element_by_id("R032000.5")
driver.execute_script("arguments[0].click();", elem)
elem = driver.find_element_by_id("R024000.5")
driver.execute_script("arguments[0].click();", elem)	
elem = driver.find_element_by_id("NextButton")
elem.click()	


# 5번 설문
elem = driver.find_element_by_id("R033000.2")
driver.execute_script("arguments[0].click();", elem)
elem = driver.find_element_by_id("NextButton")
elem.click()	

# 6번 설문
elem = driver.find_element_by_id("R011000.37")
driver.execute_script("arguments[0].click();", elem)
elem = driver.find_element_by_id("NextButton")
elem.click()	

# 7번 설문
elem = driver.find_element_by_id("R035000.5")
driver.execute_script("arguments[0].click();", elem)
elem = driver.find_element_by_id("R036000.5")
driver.execute_script("arguments[0].click();", elem)
elem = driver.find_element_by_id("NextButton")
elem.click()	

# 이유
elem = driver.find_element_by_id("NextButton")
elem.click()


# 8번 설문
elem = driver.find_element_by_id("R038000.2")
driver.execute_script("arguments[0].click();", elem)
elem = driver.find_element_by_id("NextButton")
elem.click()	

# 9번 설문
elem = driver.find_element_by_id("R040000.6")
driver.execute_script("arguments[0].click();", elem)

a=input("visit case(Y/n): ")

if(a == 'y' or a == 'Y'):
	elem = driver.find_element_by_id("R041000.4")
	driver.execute_script("arguments[0].click();", elem)
elem = driver.find_element_by_id("NextButton")
elem.click()

# 10번 설문
elem = driver.find_element_by_id("R003000.1")
driver.execute_script("arguments[0].click();", elem)
elem = driver.find_element_by_id("NextButton")
elem.click()

# 11번 설문
elem = driver.find_element_by_id("R048000.2")
driver.execute_script("arguments[0].click();", elem)
elem = driver.find_element_by_id("NextButton")
elem.click()