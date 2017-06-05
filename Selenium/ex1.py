from selenium import webdriver
from selenium.webdriver.common.keys import Keys

brow = webdriver.Firefox()
brow.get('https://www.google.com.tr')
search = brow.find_element_by_name("q")
search.send_keys("Google - Çeviri")
search.send_keys(Keys.RETURN)
