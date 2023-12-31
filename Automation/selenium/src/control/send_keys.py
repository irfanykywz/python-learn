from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
browser = webdriver.Chrome(options=options)


browser.get('http://www.yahoo.com')
print(browser.title)

elem = browser.find_element(By.NAME, 'p')  # Find the search box
elem.clear() # clear input first 
elem.send_keys('seleniumhq' + Keys.RETURN) # send key

browser.quit()