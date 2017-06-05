from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
## ▬▶ Adding selenium module  


brow = webdriver.Firefox()  ### ▬▶ Geckodriver sayesinde firefox browserı açar
brow.get('https://www.google.com.tr') ### ▬▶ Parametredeki siteye gider
search = brow.find_element_by_name("q") ### ▬▶ name 'i  "q" olan elementi bulur ▬▶ Bu örnekte google searchbar
search.send_keys("Google - Çeviri") ### ▬▶ Seçilen elemente parametredeki veriyi girer.
search.send_keys(Keys.RETURN) ### ▬▶ Sonuçların bize dönmesini sağlar
