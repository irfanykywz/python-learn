import psutil

print(psutil.disk_partitions())
# [sdiskpart(device='C:\\', mountpoint='C:\\', fstype='NTFS', opts='rw,fixed', maxfile=255, maxpath=260), sdiskpart(device='D:\\', mountpoint='D:\\', fstype='NTFS', opts='rw,fixed', maxfile=255, maxpath=260)]
 
 
print(psutil.disk_usage('/'))
# sdiskusage(total=1000200990720, used=955238920192, free=44962070528, percent=95.5)