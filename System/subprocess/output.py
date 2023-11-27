import subprocess

cmd = "ping 8.8.8.8 -t"
process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,universal_newlines=True)
for line in process.stdout:
    print(line)