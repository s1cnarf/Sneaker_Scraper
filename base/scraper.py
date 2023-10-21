import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

import json


# Create Chromeoptions instance 
options = webdriver.ChromeOptions() 
 
# Adding argument to disable the AutomationControlled flag 
options.add_argument("--disable-blink-features=AutomationControlled") 
 
# Exclude the collection of enable-automation switches 
options.add_experimental_option("excludeSwitches", ["enable-automation"]) 
 
# Turn-off userAutomationExtension 
options.add_experimental_option("useAutomationExtension", False) 
 
 
service = Service("C:\chromedriver\chromedriver.exe")
driver = webdriver.Chrome(service=service, options=options)    

# Changing the property of the navigator value for webdriver to undefined 
driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})") 

driver.get('https://stockx.com/sneakers')

driver.implicitly_wait(30)



WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@id = 'browse-wrapper']//script[1]")))

get_list_element = driver.find_element(By.XPATH, "//div[@id = 'browse-wrapper']//script[1]")

innerHTML = get_list_element.get_attribute('innerHTML')

data = json.loads(innerHTML)

shoes = data['itemListElement']
print("DATATYPE [SHOES] ", type(shoes))
print("SHOES SIZE: ", len(shoes))

for shoe in shoes:
    print(shoe)






