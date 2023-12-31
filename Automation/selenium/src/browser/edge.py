from selenium import webdriver

options = webdriver.EdgeOptions()
browser = webdriver.Edge(options=options)


browser.get('http://selenium.dev/')