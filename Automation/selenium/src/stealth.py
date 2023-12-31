from selenium_stealth import stealth
from selenium import webdriver

# init browser option
options = webdriver.ChromeOptions()

# run_forever
options.add_experimental_option("detach", True) # run forever
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)

# init browser
browser = webdriver.Chrome(options=options)

# init stealth
stealth(browser,
	# user_agent="",
	languages=["en-US", "en"],
	vendor="Google Inc.",
	platform="Win32",
	webgl_vendor="Intel Inc.",
	renderer="Intel Iris OpenGL Engine",
	fix_hairline=True,
)

# go to checking browser bot
browser.get('https://pixelscan.net/')
# browser.get('https://bot.incolumitas.com/')