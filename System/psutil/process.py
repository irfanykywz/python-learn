import psutil, os

process = psutil.Process(os.getpid())

print(process) # psutil.Process(pid=20312, name='python.exe', status='running', started='02:39:51')
print(process.pid) # 20312
print(process.ppid()) # 11012
print(process.name()) # python.exe
print(process.status()) # running
print(process.create_time()) #1704397191.5039022
print(process.is_running()) # True
print(dir(process))
# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_create_time', '_exe', '_exitcode', '_gone', '_hash', '_ident', '_init', '_last_proc_cpu_times', '_last_sys_cpu_times', '_lock', '_name', '_pid', '_pid_reused', '_ppid', '_proc', 'as_dict', 'children', 'cmdline', 'connections', 'cpu_affinity', 'cpu_percent', 'cpu_times', 'create_time', 'cwd', 'environ', 'exe', 'io_counters', 'ionice', 'is_running', 'kill', 'memory_full_info', 'memory_info', 'memory_info_ex', 'memory_maps', 'memory_percent', 'name', 'nice', 'num_ctx_switches', 'num_handles', 'num_threads', 'oneshot', 'open_files', 'parent', 'parents', 'pid', 'ppid', 'resume', 'send_signal', 'status', 'suspend', 'terminate', 'threads', 'username', 'wait']


print('memory ---------------------')
print(process.memory_full_info())
# pfullmem(rss=14737408, vms=8118272, num_page_faults=4515, peak_wset=15089664, wset=14737408, peak_paged_pool=153936, paged_pool=153728, peak_nonpaged_pool=12488, nonpaged_pool=12216, pagefile=8118272, peak_pagefile=8413184, private=8118272, uss=7192576)

print(process.memory_info())
# pmem(rss=15069184, vms=8491008, num_page_faults=3777, peak_wset=15073280, wset=15069184, peak_paged_pool=153920, paged_pool=153744, peak_nonpaged_pool=12360, nonpaged_pool=12216, pagefile=8491008, peak_pagefile=8491008, private=8491008) 

# print(process.memory_maps())

print(process.memory_percent())
# 0.183934828105609


print('cpu ---------------------')

print(process.cpu_affinity())
# [0, 1, 2, 3]

print(process.cpu_percent())
# 0.0

print(process.cpu_times())
# pcputimes(user=0.03125, system=0.109375, children_user=0.0, children_system=0.0)