import psutil, os

# def get_memory_usage():
#     process = psutil.Process(os.getpid())
#     return process.memory_info().rss


# memory_usage = get_memory_usage()
# print(memory_usage)

print(psutil.swap_memory())
# sswap(total=3434647552, used=1228353536, free=2206294016, percent=35.8, sin=0, sout=0)

virtual = psutil.virtual_memory()
print(virtual)
print(virtual.percent)
print(virtual.available)
print(virtual.total)
print(virtual.free)


# Getting % usage of virtual_memory ( 3rd field)
print('RAM memory % used:', psutil.virtual_memory()[2])
# Getting usage of virtual_memory in GB ( 4th field)
print('RAM Used (GB):', psutil.virtual_memory()[3]/1000000000)

# Calling psutil.cpu_precent() for 4 seconds
print('The CPU usage is: ', psutil.cpu_percent(0))