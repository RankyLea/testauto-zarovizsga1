from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())

URL = "https://black-moss-0a0440e03.azurestaticapps.net/tts4.html"

try:
    driver.get(URL)
    time.sleep(3)


    def penzfeldobas():
        for i in range(101):
            button = driver.find_element_by_id("submit")
            button.click()


    penzfeldobas()

    oldalak = driver.find_elements_by_xpath('//ul[@li]')
    fej = driver.find_elements_by_xpath('//ul[@li="fej"]')
    irás = driver.find_elements_by_xpath('//ul[@li="írás"]')

    if len(fej) <= 31:
        print("Helyes működés")
    else:
        print("Hibás működés")


finally:
    driver.close()
