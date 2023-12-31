import asyncio

from ichrome import AsyncChromeDaemon



# async def main():
# 	"""
# 	example http proxy
# 	"""
# 	async with AsyncChromeDaemon(
# 	# proxy='http://127.0.0.1:9999',
# 	proxy='http://4x.7x.21x.x0:14212',
# 	clear_after_shutdown=True,
# 	headless=False
# 	) as cd:
# 		async with cd.connect_tab() as tab:
# 			await tab.pass_auth_proxy('usna', 'pws')
# 			print('ahihihi')
# 			await tab.goto('https://httpbin.org/ip', timeout=2)
# 			print(await tab.html)
# 			await cd.run_forever()

# async def main():
# 	"""
# 	example socks5 proxy (not working must use gost !!!)
# 	"""
# 	async with AsyncChromeDaemon(
# 	proxy='socks5://4x.7x.21x.x0:14213',
# 	clear_after_shutdown=True,
# 	headless=False
# 	) as cd:
# 		async with cd.connect_tab() as tab:
# 			await tab.pass_auth_proxy('usna', 'pws')
# 			print('ahihihi')
# 			await tab.goto('https://httpbin.org/ip', timeout=2)
# 			print(await tab.html)
# 			await cd.run_forever()

async def main():
	"""
	example use gost proxy
	# run tunnel use gost
	# https://github.com/ginuerzh/gost
	# gost -L 127.0.0.1:9999 -F http://usna:pws@4x.7x.21x.x0:14212
	# gost -L 127.0.0.1:9999 -F socks5://usna:pws@4x.7x.21x.x0:14213
	"""
	async with AsyncChromeDaemon(
	proxy='socks5://127.0.0.1:9999',
	clear_after_shutdown=True,
	headless=False
	) as cd:
		async with cd.connect_tab() as tab:
			await tab.pass_auth_proxy('usna', 'pws')
			print('ahihihi')
			await tab.goto('https://httpbin.org/ip', timeout=2)
			print(await tab.html)
			await cd.run_forever()

asyncio.run(main())



# http:4x.7x.21x.x0:14212:usna:pws
# socks5:4x.7x.21x.x0:14213:usna:pws