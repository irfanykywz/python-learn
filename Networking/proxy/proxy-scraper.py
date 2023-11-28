# https://github.com/JaredLGillespie/proxyscrape
from proxyscrape import create_collector

collector = create_collector('my-collector', 'http')

# Retrieve any http proxy
proxy = collector.get_proxy()

print(proxy)