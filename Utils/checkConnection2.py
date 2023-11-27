from urllib import request

def internet_on():
    try:
        request.urlopen('https://google.com/', timeout=1)
        return True
    except request.URLError as err: 
        return False

if internet_on():
    print("The Internet is connected.")
else:
    print("The Internet is not connected.")