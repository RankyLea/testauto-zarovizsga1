from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time


driver = webdriver.Chrome(ChromeDriverManager().install())

URL = "https://black-moss-0a0440e03.azurestaticapps.net/rv4.html"


try:
    driver.get(URL)
    time.sleep(2)

    cities_elements = driver.find_elements_by_xpath('//ul[@id="randomCities"]/li')

# Kigyűjtöm a városokat egy txt fájlba

    with open("varosok.txt", "w") as cityfile:
        for city in cities_elements:
            cityfile.write(city.text)
            cityfile.write(",")

# Kiolvasom a fájlból a városok neveit egy listába

    cities = []

    with open("varosok.txt", "r") as city_data:
        for city in city_data:
            city_data.read().split(", ")
            cities.append(city_data)


# Összehasonlítom  a két listát, és megkeresem azt az elemet, ami csak az egyikben van - ez lesz a hiányzó város

    for varos in cities:
        if varos not in cities_elements:
            print(varos)

finally:
    driver.close()