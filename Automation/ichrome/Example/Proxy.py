import asyncio

from ichrome import AsyncChromeDaemon



# async def main():
# 	"""
# 	example http proxy
# 	"""
# 	async with AsyncChromeDaemon(
# 	# proxy='http://127.0.0.1:9999',
# 	proxy='http://45.77.212.20:14212',
# 	clear_after_shutdown=True,
# 	headless=False
# 	) as cd:
# 		async with cd.connect_tab() as tab:
# 			await tab.pass_auth_proxy('bmusproxy314311', 'juy9e49jtnx3')
# 			print('ahihihi')
# 			await tab.goto('https://httpbin.org/ip', timeout=2)
# 			print(await tab.html)
# 			await cd.run_forever()

# async def main():
# 	"""
# 	example socks5 proxy (not working must use gost !!!)
# 	"""
# 	async with AsyncChromeDaemon(
# 	proxy='socks5://45.77.212.20:14213',
# 	clear_after_shutdown=True,
# 	headless=False
# 	) as cd:
# 		async with cd.connect_tab() as tab:
# 			await tab.pass_auth_proxy('bmusproxy312855', 'b4wmcekuytwn')
# 			print('ahihihi')
# 			await tab.goto('https://httpbin.org/ip', timeout=2)
# 			print(await tab.html)
# 			await cd.run_forever()

async def main():
	"""
	example use gost proxy
	# run tunnel use gost
	# https://github.com/ginuerzh/gost
	# gost -L 127.0.0.1:9999 -F http://bmusproxy314311:juy9e49jtnx3@45.77.212.20:14212
	# gost -L 127.0.0.1:9999 -F socks5://bmusproxy312855:b4wmcekuytwn@45.77.212.20:14213
	"""
	async with AsyncChromeDaemon(
	proxy='socks5://127.0.0.1:9999',
	clear_after_shutdown=True,
	headless=False
	) as cd:
		async with cd.connect_tab() as tab:
			await tab.pass_auth_proxy('bmusproxy314311', 'juy9e49jtnx3')
			print('ahihihi')
			await tab.goto('https://httpbin.org/ip', timeout=2)
			print(await tab.html)
			await cd.run_forever()

asyncio.run(main())



# http:45.77.212.20:14212:bmusproxy314311:juy9e49jtnx3
# socks5:45.77.212.20:14213:bmusproxy312855:b4wmcekuytwn