from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://www.example.com")

try:

    wait_type = EC.presence_of_element_located((By.ID, "myDynamicElement"))
    # wait_type = EC.element_to_be_clickable((By.ID, "myDynamicElement"))
    # wait_type = EC.visibility_of_element_located((By.ID, "myDynamicElement"))
    # wait_type = EC.invisibility_of_element_located((By.ID, "myDynamicElement"))

    element = WebDriverWait(driver, timeout=10).until(wait_type)
    print("Page is ready!")
except:
    print("Timeout exceeded, page is not ready")
finally:
    driver.quit()