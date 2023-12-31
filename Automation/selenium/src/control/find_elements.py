from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
browser = webdriver.Chrome(options=options)


browser.get('http://selenium.dev/')

# by name
byname = browser.find_elements(By.NAME, 'element_name')
print(byname)

# by tag
bytag = browser.find_elements(By.TAG_NAME, 'article')
print(bytag)

# by id
byid = browser.find_elements(By.ID, '#container')
print(byid)

# by class
byclass = browser.find_elements(By.CLASS_NAME, '.content')
print(byclass)

# by selector
byselector = browser.find_elements(By.CSS_SELECTOR, '#id.class')
print(byselector)

# by xpath
byxpath = browser.find_elements(By.XPATH, '//')
print(byxpath)
 
# by link text
bylinktext = browser.find_elements(By.LINK_TEXT, '...')
print(bylinktext)

# by partial link text
bypartiallinktext = browser.find_elements(By.PARTIAL_LINK_TEXT, '...')
print(bypartiallinktext)