from platform import platform
import psutil
import platform

print(platform.node())
print(platform.machine())
print(platform.processor())
print(platform.platform())
print(platform.system())
print(platform.release())
print(platform.version())

print("Disk Usage: ",psutil.disk_usage('/'))
print("Virtual Mem: ",psutil.virtual_memory())
print("CPU percent, last 10 seconds: ",psutil.cpu_percent(interval=10))

