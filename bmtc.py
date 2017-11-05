from bs4 import BeautifulSoup
import sys
import json
import requests

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

url="https://www.mybmtc.com/en"
driver = webdriver.Firefox()
driver.get(url)

src = driver.page_source 
soup=BeautifulSoup(src,"html.parser")

elem = driver.find_element_by_id("quicktabs-tab-home_quick_tab_bottom-0")
elem.click()

elem = driver.find_element_by_id("edit-route-number") 
elem.clear()
route_id='3E'
elem.send_keys(route_id)

elem = driver.find_element_by_id("edit-via-submit") 
elem.click()

elem=driver.find_element_by_link_text("Bus Stops")
elem.click()

elem = driver.find_elements_by_id("busstop_name")
for element in elem:
    print(element.text)

'''
for i in soup.find_all('class',{'id':'busstop_name'}):
    stop = i.find('text')
    print(stop)
    
'''
elem = driver.find_element_by_id("cboxClose")
elem.click()

elem=driver.find_element_by_link_text("Route Timings")
elem.click()

elem = driver.find_elements_by_id("routes > tbody > tr:nth-child(3) > td > ul > li:nth-child(1)")
for element in elem:
    print(element.text)

elem = driver.find_element_by_id("cboxClose")
elem.click()



elem = driver.find_element_by_id("quicktabs-tab-home_quick_tab_bottom-2")
elem.click()

elem = driver.find_element_by_id("fare_select_id")
elem.send_keys("A/C Service").click()

elem = driver.find_element_by_id("edit-submit--2")
elem.click()

elem = driver.find_element_by_id("pub_fare_list_form > table.sticky-enabled.tableheader-processed.sticky-table")
elem.click()

