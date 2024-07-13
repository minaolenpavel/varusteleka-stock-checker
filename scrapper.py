from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random
import datetime
import os

def setup_driver():
    service = Service(executable_path=r"/usr/local/bin/geckodriver")
    options = webdriver.FirefoxOptions()
    options.add_argument("--headless")
    options.binary_location = r"/usr/bin/firefox"
    driver = webdriver.Firefox(service=service, options=options)
    return driver

def get_stock(url, model):
    driver = setup_driver()
    driver.maximize_window()
    driver.get(url)
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH,"/html/body/div[4]")))
    cookies_btn = driver.find_element(By.XPATH, '//*[@id="accept_necessary_cookies"]')
    cookies_btn.click()

    item_name = driver.find_element(By.TAG_NAME, "h1").text

    time.sleep(random.random())
    driver.execute_script("window.scrollBy(0, 220);")
    time.sleep(random.random())
    backpack_types = driver.find_elements(By.CLASS_NAME, "vt_n")
    
    snow_camo_section = None
    for type in backpack_types:
        if type.text == model:
            snow_camo_section = type.find_element(By.XPATH, "..")
    snow_camo_section_children = snow_camo_section.find_elements(By.XPATH, "./*")
    
    stock = None
    for child in snow_camo_section_children:
        if child.get_attribute("class") == "variation_saldo":
            stock = child.text

    screenshot_path = get_datetime()
    screenshot_path = f'img/{screenshot_path}.png'
    take_screenshot(driver, screenshot_path)
    return {"name" : item_name, "stock" : stock, "model" : model, "image" : screenshot_path}

#DRIVER IS NOT INPUT YET
def take_screenshot(driver, screenshot_path):
    if os.path.isdir("./img/"):
        driver.save_screenshot(str(screenshot_path))
    else:
        os.mkdir("./img/")
        driver.save_screenshot(str(screenshot_path))


def get_datetime():
    now = datetime.datetime.now()
    formatted_datetime = now.strftime("%d.%m.%Y-%Hh%Mm%Ss")
    return formatted_datetime