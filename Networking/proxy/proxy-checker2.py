#DR4G0N5, ITM1N

import os,  time, requests, sys, threading
PyVer = str(sys.version)

def cls():
    linux = 'clear'
    windows = 'cls'
    os.system([linux,windows][os.name == 'nt'])
cls()

def xx(PROXY, url):
    try:
        s = requests.Session()
        s.proxies.update({
            'http': f"http://{PROXY}",
            'https': f"http://{PROXY}",
            })
        # print(s.__dict__)
        # s.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        #                               ' (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
        aa = s.get(url, timeout=30)
        print(aa.content)
        if aa.status_code == 200:
            print (PROXY + '   GOOD')
            with open('proxys.txt', 'a') as xX:
                xX.write(PROXY + '\n')
        else:
            print (PROXY + '   BAD')
    except:
        print (PROXY + '   BAD')
def main():
    fileproxy = 'https.txt'
    with open(fileproxy, 'r') as x:
        prox = x.read().splitlines()
    thread = []
    for proxy in prox:
        t = threading.Thread(target=xx, args=(proxy, 'http://httpbin.org/ip'))
        t.start()
        thread.append(t)
        time.sleep(0.1)
    for i in thread:
        i.join()
main()