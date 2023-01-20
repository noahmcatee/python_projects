import psutil

def check_storage():
    """Checks the storage usage of the local computer"""
    storage = psutil.disk_usage("/")
    print(f"Total storage: {storage.total / (1024 ** 3):.2f} GB")
    print(f"Used storage: {storage.used / (1024 ** 3):.2f} GB")
    print(f"Free storage: {storage.free / (1024 ** 3):.2f} GB")
    print(f"Storage usage percentage: {storage.percent}%")

def check_cpu():
    """Checks the CPU usage of the local computer"""
    cpu_percent = psutil.cpu_percent()
    print(f"CPU usage: {cpu_percent}%")

def check_memory():
    """Checks the memory usage of the local computer"""
    memory = psutil.virtual_memory()
    print(f"Total memory: {memory.total / (1024 ** 3):.2f} GB")
    print(f"Used memory: {memory.used / (1024 ** 3):.2f} GB")
    print(f"Free memory: {memory.free / (1024 ** 3):.2f} GB")
    print(f"Memory usage percentage: {memory.percent}%")

check_storage()
print("\n")
check_cpu()
print("\n")
check_memory()