# https://stackoverflow.com/questions/28431765/open-web-in-new-tab-selenium-python
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time


"""
second way
"""
driver = webdriver.Chrome()
driver.get('https://www.google.com')

driver.execute_script("window.open('');")
time.sleep(5)

driver.switch_to.window(driver.window_handles[1])
driver.get("https://facebook.com")
time.sleep(5)

driver.close()
time.sleep(5)

driver.switch_to.window(driver.window_handles[0])
driver.get("https://www.yahoo.com")
time.sleep(5)


"""
first way
"""
# options = webdriver.ChromeOptions()
# options.add_experimental_option("detach", True)
# driver = webdriver.Chrome(options=options)
# driver.get("http://www.google.co.in")
# print("Initial Page Title is : %s" %driver.title)
# windows_before  = driver.current_window_handle
# print("First Window Handle is : %s" %windows_before)
# driver.execute_script("window.open('https://www.yahoo.com')")
# WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))
# windows_after = driver.window_handles
# new_window = [x for x in windows_after if x != windows_before][0]
# driver.switch_to.window(new_window)
# print("Page Title after Tab Switching is : %s" %driver.title)
# print("Second Window Handle is : %s" %new_window)