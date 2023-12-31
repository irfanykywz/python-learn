from seleniumbase import Driver
import time

driver = Driver(uc=True, incognito=True)
driver.get("https://nowsecure.nl/#relax")
time.sleep(8)
driver.quit()