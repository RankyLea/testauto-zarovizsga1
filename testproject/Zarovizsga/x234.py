from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())

URL = "https://black-moss-0a0440e03.azurestaticapps.net/x234.html"

try:
    driver.get(URL)
    time.sleep(2)

    # TC01: Helyes kitöltés
    # Tesztadatok: a = 99, b = 12, várt eredmény = 222

    vart_eredmeny_1 = "222"

    a_input = driver.find_element_by_id("a")
    b_input = driver.find_element_by_id("b")
    kalk_btn = driver.find_element_by_id("submit")

    a_input.send_keys(99)
    b_input.send_keys(12)
    kalk_btn.click()
    time.sleep(2)

    eredmeny_tc01 = driver.find_element_by_xpath('//*[@id="result"]').text

    assert eredmeny_tc01 == vart_eredmeny_1

    # TC02: Helytelen kitöltés
    # Tesztadatok: a = kiskutya, b = 12, várt eredmény = NaN

    vart_eredmeny_2 = "NaN"

    a_input.clear()
    b_input.clear()
    a_input.send_keys("kiskutya")
    b_input.send_keys(12)
    kalk_btn.click()
    time.sleep(2)

    eredmeny_tc02 = driver.find_element_by_xpath('//*[@id="result"]').text

    assert vart_eredmeny_2 == eredmeny_tc02

    # TC03: Üres kitöltés
    # Tesztadatok: a = <üres>, b = <üres>, várt eredmény = NaN

    vart_eredmeny_3 = "NaN"

    a_input.clear()
    b_input.clear()
    a_input.send_keys("")
    b_input.send_keys("")
    kalk_btn.click()
    time.sleep(2)

    eredmeny_tc03 = driver.find_element_by_xpath('//*[@id="result"]').text

    assert eredmeny_tc03 == vart_eredmeny_3

finally:
    driver.close()
