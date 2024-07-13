from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException, StaleElementReferenceException
import time
import random


service = Service(executable_path=r"C:\Program Files (x86)\geckodriver.exe")
options = webdriver.FirefoxOptions()
options.add_argument("--headless")
options.binary_location = r"C:\Program Files\Mozilla Firefox\firefox.exe"
driver = webdriver.Firefox(service=service, options=options)
driver.maximize_window()
driver.get("https://www.varusteleka.com/en/product/sarma-tst-cp15-combat-pack-w-flat-shoulder-straps/75036")
cookies = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH,"/html/body/div[4]")))
cookies_btn = driver.find_element(By.XPATH, '//*[@id="accept_necessary_cookies"]')
cookies_btn.click()
time.sleep(random.random())
driver.execute_script("window.scrollBy(0, 500);")
time.sleep(random.random())
backpack_types = driver.find_elements(By.CLASS_NAME, "vt_n")
snow_camo_section = None
for type in backpack_types:
    if type.text == "M05 Snow Camo":
        print(type.text)
        snow_camo_section = type.find_element(By.XPATH, "..")


