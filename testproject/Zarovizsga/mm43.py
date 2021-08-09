from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time


driver = webdriver.Chrome(ChromeDriverManager().install())

URL = "https://black-moss-0a0440e03.azurestaticapps.net/mm43.html"

try:
    driver.get(URL)
    time.sleep(3)

    email_field = driver.find_element_by_id("email")
    button = driver.find_element_by_id("submit")

# TC01: Helyes kitöltés
# Tesztadat: email: teszt@elek.hu
# Elvárt eredmény: Nincs validációs hibaüzenet

    email_field.send_keys("teszt@elek.hu")
    button.click()

    # Helyes kitöltésnél a form onsubmit="return false" class = "", => nem ad hibaüzenetet

    form = driver.find_element_by_xpath('/html/body/div/div/form').get_attribute('class')

    assert form == ""

# TC02: Helytelen kitöltés
# Tesztadat: email: teszt@

    elvárt_eredmény = "Kérjük, adja meg a „@” utáni részt is. A(z) „teszt@” cím nem teljes."

    email_field.clear()
    email_field.send_keys("teszt@")
    button.click()
    hiba_üzenet = driver.find_element_by_xpath('/html/body/div/div/form/div').text

    assert hiba_üzenet == elvárt_eredmény

# TC03: Üres kitöltés
# Tesztadat: email: <üres>

    elvárt_hiba = "Kérjük, töltse ki ezt a mezőt."

    email_field.clear()
    email_field.send_keys("")
    button.click()
    hiba_üzenet = driver.find_element_by_xpath('/html/body/div/div/form/div').text

    assert hiba_üzenet == elvárt_hiba

finally:
    driver.close()
