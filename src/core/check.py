import subprocess
import platform

def icmp(ip): 
    command = ["ping", "-c", "1", ip]
    try:
        return subprocess.call(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL) == 0
    except Exception:
        return False
    