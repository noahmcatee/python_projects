from platform import platform
import psutil
import platform

print("Device name:", platform.node())
print("Device type:", platform.machine())
print("Device processer:", platform.processor())
print("Device platform:", platform.platform())
print("Device OS:", platform.system())
print("Device OS release:", platform.release())
print("Device OS version:", platform.version())

print("Disk Usage: ",psutil.disk_usage('/'))
print("Virtual Mem: ",psutil.virtual_memory())
print("CPU percent, last 10 seconds: ",psutil.cpu_percent(interval=10))
