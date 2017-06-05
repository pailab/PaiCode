from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
## ▬▶ Adding selenium module  
## ▬▶ Adding time module for sleep function


brow = webdriver.Firefox()  ### ▬▶ Geckodriver sayesinde firefox browserı açar
brow.get("https://goo.gl/G47fJj") ### ▬▶ Parametredeki siteye gider ▬▶ Bu örnekte google form
brow.find_element_by_name("entry.132484528").send_keys("Ümit Öztürk") ### ▬▶ Elementin nameine göre elementi yakalar ve send_keys ile istediğimiz parametreyi vermemizi sağlar
#sleep(1) 
brow.find_element_by_name("entry.1327343241").send_keys("umit@pailab.net") ### ▬▶ Elementin nameine göre elementi yakalar ve send_keys ile istediğimiz parametreyi vermemizi sağlar
#sleep(1)
brow.find_element_by_xpath(".//*[@id='mG61Hd']/div/div[2]/div[3]/div[1]/div/div/content/span").click() ### ▬▶ XPATH'e göre elementi yakalar ve send_keys ile istediğimiz parametreyi vermemizi sağlar
sleep(5) ### ▬▶ 5 program saniye bekler
brow.find_element_by_xpath(".//*[@id='mG61Hd']/div/div[2]/div[2]/div[2]/div[2]/div/content/div/label[3]/div/div[1]/div[3]/div").click() ### ▬▶ XPATH'e göre elementi yakalar ve send_keys ile istediğimiz parametreyi vermemizi sağlar
#sleep(1)
brow.find_element_by_xpath(".//*[@id='mG61Hd']/div/div[2]/div[2]/div[3]/div[2]/div/content/div/label[4]/div/div[1]/div[3]/div").click() ### ▬▶ XPATH'e göre elementi yakalar ve send_keys ile istediğimiz parametreyi vermemizi sağlar
#sleep(1)
brow.find_element_by_xpath(".//*[@id='mG61Hd']/div/div[2]/div[3]/div[1]/div/div[2]/content").click() ### ▬▶ XPATH'e göre elementi yakalar ve send_keys ile istediğimiz parametreyi vermemizi sağlar
