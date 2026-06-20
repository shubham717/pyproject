import os
from selenium import webdriver

os.environ['PATH'] += r"/Users/shubham/webdriver"
driver = webdriver.Chrome()
driver.get("https://www.searchhounds.com/")
my_element = driver.find_element_by_class("_domainCTALink_125zm_44")
