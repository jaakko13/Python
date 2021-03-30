#import selenium
from selenium import webdriver
import time
#from datetime import date
import datetime
#import webbrowser

#webdriver setup
PATH = "C:\Program Files (x86)\chromedriver.exe"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--disable-notifications")
chrome_options.add_argument("--start-maximized")
driver = webdriver.Chrome(PATH)
driver.maximize_window() 

#XPATH variables that need to be clicked on
driver.get("https://www.kayak.com/flights")
date = '/html/body/div[1]/div[1]/main/div[1]/div[1]/div/div[1]/div/div/section[2]/div/div/div[2]/form[1]/div[1]/div/div[1]/div/div[4]/div/div[3]/div/div/div[1]'
month = '/html/body/div[6]/div/div[2]/div[2]/div/div[4]/div[1]/div/div[3]'
search = '/html/body/div[1]/div[1]/main/div[1]/div[1]/div/div[1]/div/div/section[2]/div/div/div[2]/form[1]/div[1]/div/div[2]/button'
anywhere = '/html/body/div[33]/div[3]/div/div/div/div[2]/div/div[2]/button'
places = '/html/body/div[1]/div[1]/main/div[2]/div[2]/div[2]/div/div[2]/div/div/div/div[3]/div/div/div[1]/div/button/div/div[2]/div[1]'


driver.find_element_by_xpath(date).click()
time.sleep(3)
driver.find_element_by_xpath(month).click()
time.sleep(3)
driver.find_element_by_xpath(search).click()
time.sleep(3)
driver.find_element_by_xpath(anywhere).click()
time.sleep(3)


destinations = driver.find_element_by_xpath(places).text
print(destinations)

