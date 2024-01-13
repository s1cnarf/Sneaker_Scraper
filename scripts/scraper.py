from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

import json
import requests

from urllib.parse import urlparse, urlunparse

from base.models import Product, Offer

def run():
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


    url = 'https://stockx.com/sneakers?page={}'

    for page_number in range(1,26):
        
        driver.get(url.format(page_number))

        driver.implicitly_wait(30)


        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@id = 'browse-wrapper']//script[1]")))

        get_list_element = driver.find_element(By.XPATH, "//div[@id = 'browse-wrapper']//script[1]")

        innerHTML = get_list_element.get_attribute('innerHTML')

        data = json.loads(innerHTML)

        shoes = data['itemListElement']
        print("SHOES SIZE: ", len(shoes))

        try: 
            pass
            # for shoe in shoes:
            #     detail = shoe['item']
                
            #     # details
            #     type = detail['@type']
            #     brand = detail['brand']
            #     color = detail['color']
            #     description = detail['description']

            #     imageURL = modify_url(detail['image'])
            
            #     itemCondition = detail['itemCondition']
            #     model = detail['model']
            #     name = detail['name']
            #     releaseDate = detail['releaseDate']
            #     sku = detail['sku']
            #     url = detail['url']

            #     # offer
            #     offer = detail['offers']
            #     o_type = offer['@type']
            #     o_lowPrice = offer['lowPrice']
            #     o_highPrice = offer['highPrice']
            #     o_priceCurrency = offer['priceCurrency']
            #     o_url = offer['url']
                

            #     offer_object = Offer.objects.create(
            #         type = o_type,
            #         lowPrice = o_lowPrice,
            #         highPrice = o_highPrice,
            #         priceCurrency = o_priceCurrency,
            #         offer_url = o_url
            #     )

            #     Product.objects.create(
            #         type = type,
            #         brand = brand,
            #         color = color,
            #         description = description,
            #         image_url = imageURL,
            #         itemcondition = itemCondition,
            #         model = model,
            #         name = name,
            #         releaseDate = releaseDate,
            #         sku = sku,
            #         product_url = url,
            #         offers = offer_object
            #     )
        except Exception as e: 
            print('Problem inserting in database', e)

        driver.implicitly_wait(30)




def modify_url(url):
    # Parse the URL
    parsed_url = urlparse(url)

    # Create a modified version without the query parameters
    modified_url = urlunparse((parsed_url.scheme, parsed_url.netloc, parsed_url.path,
                                    parsed_url.params, '', parsed_url.fragment))
    
    return modified_url
        