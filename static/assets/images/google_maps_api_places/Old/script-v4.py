from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time 
options = Options()

options.add_experimental_option('excludeSwitches', ['enable-logging'])

driver = webdriver.Chrome(executable_path=r"C:\Program Files (x86)\Chrome Driver\chromedriver.exe",chrome_options=options)
driver.set_window_size(1920, 1080)

driver.get("https://www.queensland.com/au/en/info/search?query=")
print(driver.title)

searchbox = driver.find_element(by=By.XPATH, value = '/html/body/div[1]/div/div/div[1]/div[2]/div[1]/div[2]/div[1]/div/div/form/div[1]/div/div[1]/div/div/label/div/input')
searchbox.send_keys("Abbey Museum of Art & Archaeology")
searchbox.send_keys(Keys.RETURN)

try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="search_970281781"]/form/div[3]/div/div[2]/div/div[3]/div[1]/div/div[1]/div/div/a'))
    )
    element.click()  
except:
    driver.quit()







#searchbutton = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div[2]/div[1]/div[2]/div[1]/div/div/form/div[1]/div/div[2]/div/div/button')
#searchbutton.click

time.sleep(60)
driver.quit()  