import psutil
import datetime

def check_storage():
    """Checks the storage usage of the local computer"""
    storage = psutil.disk_usage("/")
    return (f"Total storage: {storage.total / (1024 ** 3):.2f} GB", 
            f"Used storage: {storage.used / (1024 ** 3):.2f} GB",
            f"Free storage: {storage.free / (1024 ** 3):.2f} GB",
            f"Storage usage percentage: {storage.percent}%")

def check_cpu():
    """Checks the CPU usage of the local computer"""
    cpu_percent = psutil.cpu_percent()
    return f"CPU usage: {cpu_percent}%"

def check_memory():
    """Checks the memory usage of the local computer"""
    memory = psutil.virtual_memory()
    return (f"Total memory: {memory.total / (1024 ** 3):.2f} GB", 
            f"Used memory: {memory.used / (1024 ** 3):.2f} GB",
            f"Free memory: {memory.free / (1024 ** 3):.2f} GB",
            f"Memory usage percentage: {memory.percent}%")

def save_to_file(storage_info, cpu_info, memory_info):
    """Saves the system information to a file"""
    date_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    filename = f"system_info {date_time}.txt"
    with open(filename, "w") as file:
        file.write(f"System information as of {date_time}\n\n")
        file.write("Storage:\n")
        for info in storage_info:
            file.write(f"{info}\n")
        file.write("\n")
        file.write(f"{cpu_info}\n")
        file.write("\n")
        file.write("Memory:\n")
        for info in memory_info:
            file.write(f"{info}\n")

storage_info = check_storage()
cpu_info = check_cpu()
memory_info = check_memory()
save_to_file(storage_info, cpu_info, memory_info)
print("System information saved to file.")