from selenium import webdriver

options = webdriver.SafariOptions()
browser = webdriver.Safari(options=options)


browser.get('http://selenium.dev/')