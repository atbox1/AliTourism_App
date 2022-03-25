from ast import keyword
from tkinter.font import names
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time 
import requests
import shutil

location_names = [
'Abbey Museum of Art & Archaeology',
'Agnes Water Museum',
'Aquaduck Sunshine Coast',
'Archer Park Rail Museum',
'Australia Zoo',
'Australian Butterfly Sanctuary',
'Australian Whale Watching',
'Bama Way Aboriginal Journeys (Adventure North)',
'Birrunga Gallery and Dining',
'BlackCard Cultural Tours',
'Coral Expeditions - Cape York and Arnhem Land'
]

for location_name in location_names:
    options = Options()

    options.add_experimental_option('excludeSwitches', ['enable-logging'])

    driver = webdriver.Chrome(executable_path=r"C:\Program Files (x86)\Chrome Driver\chromedriver.exe",chrome_options=options)
    driver.set_window_size(1920, 1080)
    driver.get("https://www.queensland.com/au/en/info/search?query=")
    print(driver.title)
    #filtre_option = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, 'category'))).click()
    searchbox = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="search_970281781"]/form/div[1]/div/div[1]/div/div/label/div/input' )))
    searchbox.send_keys(location_name)
    filtre_option = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/div[1]/div[2]/div[1]/div[2]/div[1]/div/div/form/div[3]/div/div[1]/div/div/div/div[2]/div[2]/div/div[1]/fieldset/div[2]/div[3]/div/label/div/span'))).click()  
    time.sleep(5)
    searchbox.send_keys(Keys.ENTER)


    time.sleep(5)

    

    #images = [] 

    xpath = '/html/body/div[1]/div/div/div[1]/div[2]/div[1]/div[2]/div[1]/div/div/form/div[3]/div/div[2]/div/div[3]/div[1]/div/div[1]/div/div/a/div[1]/div[1]/figure/div[1]/div/div/img'
    img_link = driver.find_elements_by_xpath(xpath)
    img_link = [xpath.get_attribute('src') for xpath in img_link]
    print(img_link)
    img_url = (','.join(img_link))

    r = requests.get(str(img_url), stream=True)
    if r.status_code == 200:
        with open(location_name + ".png", 'wb') as f:
            r.raw.decode_content = True
            shutil.copyfileobj(r.raw, f)
    
    location_clicker = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="search_970281781"]/form/div[3]/div/div[2]/div/div[3]/div[1]/div/div[1]/div/div/a'))).click()
    time.sleep(2)
    driver.execute_script("window.scrollTo(0, 1000);")
    time.sleep(2)
    description_xpath = "//*[@id='atdw-description']/div"
    description_scrap = driver.find_element_by_xpath(description_xpath).get_attribute('innerHTML')

    with open(location_name + ".rtf", 'w') as f:
        f.write(description_scrap)


    driver.set_page_load_timeout(12000)

    