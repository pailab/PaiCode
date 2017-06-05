from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep


brow = webdriver.Firefox()
brow.get("https://goo.gl/G47fJj")
brow.find_element_by_name("entry.132484528").send_keys("Ümit Öztürk")
#sleep(1)
brow.find_element_by_name("entry.1327343241").send_keys("umit@pailab.net")
#sleep(1)
brow.find_element_by_xpath(".//*[@id='mG61Hd']/div/div[2]/div[3]/div[1]/div/div/content/span").click()
sleep(5)
brow.find_element_by_xpath(".//*[@id='mG61Hd']/div/div[2]/div[2]/div[2]/div[2]/div/content/div/label[3]/div/div[1]/div[3]/div").click()
#sleep(1)
brow.find_element_by_xpath(".//*[@id='mG61Hd']/div/div[2]/div[2]/div[3]/div[2]/div/content/div/label[4]/div/div[1]/div[3]/div").click()
#sleep(1)
brow.find_element_by_xpath(".//*[@id='mG61Hd']/div/div[2]/div[3]/div[1]/div/div[2]/content").click()
