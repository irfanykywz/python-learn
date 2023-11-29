import mechanicalsoup, json

cookies = """
"""

# def save_cookies(browser):
#     return browser.session.cookies.get_dict()

# def load_cookies(browser, cookies):
#     from requests.utils import cookiejar_from_dict
#     browser.session.cookies = cookiejar_from_dict(cookies)

# browser = mechanicalsoup.StatefulBrowser()
# browser.open("https://mbasic.facebook.com/")

# cookies = save_cookies(browser)
# print(cookies)
# load_cookies(browser, cookies)
# exit()

# print(json.loads(cookies))
# exit()

# from http.cookies import SimpleCookie

# rawdata = 'devicePixelRatio=1; ident=exists; __utma=13103r6942.2918; __utmc=13103656942; __utmz=13105942.1.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); mp_3cb27825a6612988r46d00tinct_id%22%3A%201752338%2C%22%24initial_referrer%22%3A%20%22https%3A%2F%2Fwww.pion_created_at%22%3A%20%222015-08-03%22%2C%22platform%22%3A%20%22web%22%2C%%22%3A%20%%22%7D; t_session=BAh7DUkiD3Nlc3NpbWVfZV9uYW1lBjsARkkiH1BhY2lmaWMgVGltZSAoVVMgJiBDYW5hZGEpBjsAVEkiFXNpZ25pbl9wZXJzb25faWQGOwBGaQMSvRpJIhRsYXN0X2xvZ2luX2RhdGUGOwBGVTogQWN0aXZlU3VwcG9ydDo6VGltZVdpdGhab25lWwhJdToJVGltZQ2T3RzAAABA7QY6CXpvbmVJIghVVEMGOwBUSSIfUGFjaWZpZWRfZGFzaGJvYXJkX21lc3NhZ2UGOwBGVA%3D%3D--6ce6ef4bd6bc1a469164b6740e7571c754b31cca'
# cookie = SimpleCookie()
# cookie.load(rawdata)

# 1
from requests.utils import cookiejar_from_dict	
browser = mechanicalsoup.Browser()


cookie = {}
for elem in json.loads(cookies):
    cookie[elem["name"]] = elem["value"]

url = "https://www.blogger.com/blog/posts/8610126882772671651"
browser.session.cookies = cookiejar_from_dict(cookie)	
get = browser.get(url)
login_html = get.soup
browser.launch_browser(login_html)

print(get.soup)
exit()

# # 2
# form = login_html.select("form")[0]
# form.select("input")[0]["value"] = "zeus"
# form.select("input")[1]["value"] = "ThunderDude"

# # 3
# profiles_page = browser.submit(form, get.url)

# links = profiles_page.soup.select("a")

# print(links)