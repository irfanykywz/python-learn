import psutil, os

print(psutil.cpu_times())
# scputimes(user=137617.28125, system=65232.40625, idle=599985.265625, interrupt=1800.484375, dpc=1440.84375)

print(psutil.cpu_percent(1))
# 0.0


print("Number of cores in system", psutil.cpu_count())

print(psutil.cpu_stats())
# scpustats(ctx_switches=1656070893, interrupts=1636935842, soft_interrupts=0, syscalls=214678018)


print(psutil.cpu_freq())
# scpufreq(current=931.42925, min=400.0, max=2000.0) 

print(psutil.getloadavg())
# (0.0, 0.0, 0.0)