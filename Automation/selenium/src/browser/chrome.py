from selenium import webdriver

options = webdriver.ChromeOptions()
browser = webdriver.Chrome(options=options)


browser.get('http://selenium.dev/')