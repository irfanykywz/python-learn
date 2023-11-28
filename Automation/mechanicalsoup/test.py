import mechanicalsoup, json

cookies = """
[
{
    "domain": ".blogger.com",
    "expirationDate": 1731912469.969122,
    "hostOnly": false,
    "httpOnly": false,
    "name": "__Secure-1PAPISID",
    "path": "/",
    "sameSite": "unspecified",
    "secure": true,
    "session": false,
    "storeId": "0",
    "value": "-UGMORohqFjmAzxu/AMxK3dovnRTgniVuF",
    "id": 1
},
{
    "domain": ".blogger.com",
    "expirationDate": 1731912469.968809,
    "hostOnly": false,
    "httpOnly": true,
    "name": "__Secure-1PSID",
    "path": "/",
    "sameSite": "unspecified",
    "secure": true,
    "session": false,
    "storeId": "0",
    "value": "cAipdZIRNXlKkxmwoQRmT6IlpJR9mMeVLfSCZhkWvhNusT_KIJRV9jgnMFnR18zX02BGNw.",
    "id": 2
},
{
    "domain": ".blogger.com",
    "expirationDate": 1731912469.969155,
    "hostOnly": false,
    "httpOnly": false,
    "name": "__Secure-3PAPISID",
    "path": "/",
    "sameSite": "no_restriction",
    "secure": true,
    "session": false,
    "storeId": "0",
    "value": "-UGMORohqFjmAzxu/AMxK3dovnRTgniVuF",
    "id": 3
},
{
    "domain": ".blogger.com",
    "expirationDate": 1731912469.968849,
    "hostOnly": false,
    "httpOnly": true,
    "name": "__Secure-3PSID",
    "path": "/",
    "sameSite": "no_restriction",
    "secure": true,
    "session": false,
    "storeId": "0",
    "value": "cAipdZIRNXlKkxmwoQRmT6IlpJR9mMeVLfSCZhkWvhNusT_KS0NnsGgXeSPj8ARgHJTW9g.",
    "id": 4
},
{
    "domain": ".blogger.com",
    "expirationDate": 1732226192.531342,
    "hostOnly": false,
    "httpOnly": false,
    "name": "_ga",
    "path": "/",
    "sameSite": "unspecified",
    "secure": false,
    "session": false,
    "storeId": "0",
    "value": "GA1.2.1261912687.1692339686",
    "id": 5
},
{
    "domain": ".blogger.com",
    "expirationDate": 1731912469.96905,
    "hostOnly": false,
    "httpOnly": false,
    "name": "APISID",
    "path": "/",
    "sameSite": "unspecified",
    "secure": false,
    "session": false,
    "storeId": "0",
    "value": "ho9S18F8QtpI0Ype/AuNBBUSXb2Ox0mqAX",
    "id": 6
},
{
    "domain": ".blogger.com",
    "expirationDate": 1731912469.968888,
    "hostOnly": false,
    "httpOnly": true,
    "name": "HSID",
    "path": "/",
    "sameSite": "unspecified",
    "secure": false,
    "session": false,
    "storeId": "0",
    "value": "Ag8yhsvta2q8-Ha4C",
    "id": 7
},
{
    "domain": ".blogger.com",
    "expirationDate": 1708514860.937751,
    "hostOnly": false,
    "httpOnly": true,
    "name": "NID",
    "path": "/",
    "sameSite": "unspecified",
    "secure": true,
    "session": false,
    "storeId": "0",
    "value": "511=ZwYFk1s-Yhx72NkTre3SvD0ng5Z37ykKSvV3D_gKUHUTxRIUh6P270_khNNOJR_QxXCI56CPz7zo2xPZ8bKY_k1jqr3MKiqf_WA9Ay2VvwwkapUxEpxEb0Ah846QeZaa0B3KUJGw3HAKi21wxjrFoyFr68QM_HXpEnEvvU6L2ttOTQEUuvxDI9RgWo7nn-InPA",
    "id": 8
},
{
    "domain": ".blogger.com",
    "expirationDate": 1731912469.969087,
    "hostOnly": false,
    "httpOnly": false,
    "name": "SAPISID",
    "path": "/",
    "sameSite": "unspecified",
    "secure": true,
    "session": false,
    "storeId": "0",
    "value": "-UGMORohqFjmAzxu/AMxK3dovnRTgniVuF",
    "id": 9
},
{
    "domain": ".blogger.com",
    "expirationDate": 1731912469.968679,
    "hostOnly": false,
    "httpOnly": false,
    "name": "SID",
    "path": "/",
    "sameSite": "unspecified",
    "secure": false,
    "session": false,
    "storeId": "0",
    "value": "cAipdZIRNXlKkxmwoQRmT6IlpJR9mMeVLfSCZhkWvhNusT_Kz18RCHupLTTGowiiTOcgGA.",
    "id": 10
},
{
    "domain": ".blogger.com",
    "expirationDate": 1731912469.968921,
    "hostOnly": false,
    "httpOnly": true,
    "name": "SSID",
    "path": "/",
    "sameSite": "unspecified",
    "secure": true,
    "session": false,
    "storeId": "0",
    "value": "ADtUsLKKvOPoqPbHQ",
    "id": 11
},
{
    "domain": "www.blogger.com",
    "expirationDate": 1700859377,
    "hostOnly": true,
    "httpOnly": false,
    "name": "OTZ",
    "path": "/",
    "sameSite": "unspecified",
    "secure": true,
    "session": false,
    "storeId": "0",
    "value": "7266056_28_28__28_",
    "id": 12
}
]
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