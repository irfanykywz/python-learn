from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains

print(ChromeDriverManager().install())

# driver = webdriver.Chrome(ChromeDriverManager().install())

# driver.get('https://shopee.tw/mall/%E6%9B%B8%E7%B1%8D%E5%8F%8A%E9%9B%9C%E8%AA%8C%E6%9C%9F%E5%88%8A-cat.11041120')
# time.sleep(5)