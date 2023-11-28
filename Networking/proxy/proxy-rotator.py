import random

proxies = ["103.155.217.1:41317", "47.91.56.120:8080", "103.141.143.102:41516", "167.114.96.13:9300", "103.83.232.122:80"]


for i in range(20):
   ip = random.randrange(0, len(proxies))
   print(proxies[ip])