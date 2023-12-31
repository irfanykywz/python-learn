from selenium import webdriver

# init browser option
options = webdriver.ChromeOptions()


# run_forever
options.add_experimental_option("detach", True)
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)

# argument
options.add_argument("start-maximized")
options.add_argument('disable-infobars')	
# options.add_argument('--headless') 
# options.add_argument('--proxy-server=127.0.0.1:8080')
# options.add_argument(r"--user-data-dir="+chrome_path)
# options.add_argument(r'--profile-directory='+profile)

# page load strategy
options.page_load_strategy = 'normal'
# normal: This strategy waits for the full page loading, which means it waits for all stylesheets, images, and subframes to finish loading. This is the default strategy in Selenium.
# eager: This strategy also waits for the full page loading, but it also waits for the DOMContentLoaded event to be fired before returning.
# none: This strategy doesn't wait for the full page loading. It returns immediately after the initial HTML document has been completely loaded and parsed, without waiting for stylesheets, images, and subframes to finish loading.

# init browser
browser = webdriver.Chrome(options=options)

browser.get('http://selenium.dev/')