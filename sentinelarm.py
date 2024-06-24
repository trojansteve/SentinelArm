import subprocess
import platform
import psutil
import os
import socket
import nmap
import hashlib
import datetime
from urllib import request
import json

def get_system_info():
    try:
        # List of sysctl keys for fetching hardware information
        sysctl_keys = [
            'hw.model',            # Model of the device
            'hw.machine',          # Machine architecture
            'hw.memsize',          # Total memory size
            'machdep.cpu.brand_string',  # CPU brand string
            'kern.version',        # Kernel version
            'kern.osproductversion',  # OS version
            'hw.physicalcpu',      # Number of physical CPUs
            'hw.logicalcpu',       # Number of logical CPUs
            'hw.cpufrequency',     # CPU frequency
            'hw.busfrequency',     # Bus frequency
            'hw.l1icachesize',     # L1 instruction cache size
            'hw.l1dcachesize',     # L1 data cache size
            'hw.l2cachesize',      # L2 cache size
            'hw.l3cachesize',      # L3 cache size
            'hw.cachelinesize',    # Cache line size
        ]

        # Fetch system information for each sysctl key
        system_info = {}
        for key in sysctl_keys:
            output = subprocess.check_output(['sysctl', '-n', key])
            system_info[key] = output.decode('utf-8').strip()

        # Print system information
        print("\n=== System Information ===")
        for key, value in system_info.items():
            print(f"{key}: {value}")

        # Check for potential low-hanging fruits (example checks)
        print("\n=== Potential low-hanging fruits ===")

        # Check for outdated OS version
        os_version = system_info.get('kern.osproductversion', '')
        if os_version < '12.0':  # Example: Check if OS version is older than macOS Monterey
            print(f"  - Update to the latest macOS version (Current: {os_version})")

        # Check for high CPU usage or anomalies
        cpu_usage = psutil.cpu_percent(interval=1)
        if cpu_usage > 80.0:  # Example: Check if CPU usage exceeds 80%
            print(f"  - High CPU usage detected ({cpu_usage:.2f}%)")

        # Check for available memory
        mem_usage = psutil.virtual_memory()
        if mem_usage.available < 2 * 1024 * 1024 * 1024:  # Example: Check if less than 2GB RAM available
            print(f"  - Low memory available ({mem_usage.available / (1024*1024*1024):.2f} GB)")

        # Check disk usage
        disk_usage = psutil.disk_usage('/')
        if disk_usage.percent > 90.0:  # Example: Check if disk usage exceeds 90%
            print(f"  - High disk usage ({disk_usage.percent}%)")

        # Check network interfaces and connections
        print("\n=== Network Security ===")

        # Scan open ports
        print("Scanning for open ports...")
        scanner = nmap.PortScanner()
        scanner.scan('localhost', arguments='-p 1-65535 --open')
        for host in scanner.all_hosts():
            for proto in scanner[host].all_protocols():
                ports = scanner[host][proto].keys()
                for port in ports:
                    print(f"  - Port {port}/{proto}: {scanner[host][proto][port]['state']}")

        # Check active network connections
        print("\nChecking active network connections...")
        net_connections = psutil.net_connections(kind='inet')
        if len(net_connections) > 10:  # Example: Check if more than 10 active network connections
            print(f"  - High number of active network connections ({len(net_connections)})")

        # Check for external IP address
        #print("\nChecking external IP address...")
        #external_ip = request.urlopen('https://api64.ipify.org?format=json').read().decode('utf8')
        #external_ip = json.loads(external_ip)['ip']
        #print(f"  - External IP address: {external_ip}")

        # Check running processes

        # Check for specific processes (e.g., common malware or suspicious processes)

        # Additional checks can be added based on specific requirements

    except subprocess.CalledProcessError as e:
        print(f"Error executing sysctl command: {e}")
    except psutil.Error as e:
        print(f"Error with psutil library: {e}")
    except Exception as e:
        print(f"Unexpected error occurred: {e}")

# Example usage:
if __name__ == "__main__":
    print(f"Running reconnaissance on macOS ARM64 ({platform.mac_ver()[0]})")
    get_system_info()
