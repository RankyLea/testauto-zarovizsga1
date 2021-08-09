from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())

URL = "https://black-moss-0a0440e03.azurestaticapps.net/ioa8.html"

try:
    driver.get(URL)
    time.sleep(3)

    szam_1 = driver.find_element_by_xpath('//*[@id="num1"]').text
    operator = driver.find_element_by_xpath('//*[@id="op"]').text
    szam_2 = driver.find_element_by_xpath('//*[@id="num2"]').text

    print(szam_1, szam_2)

    if operator == "*":
        eredmeny = int(szam_1) * int(szam_2)
    elif operator == "+":
        eredmeny = int(szam_1) + int(szam_2)
    elif operator == "-":
        eredmeny = int(szam_1) - int(szam_2)
    elif operator == "/":
        eredmeny = int(szam_1) / int(szam_2)

    print(type(eredmeny))
    print(eredmeny)

    kalk_btn = driver.find_element_by_id("submit")
    kalk_btn.click()

    result = driver.find_element_by_xpath('//*[@id="result"]').text

    print(type(result))
    print(int(result))

    assert eredmeny == int(result)


finally:
    driver.close()
