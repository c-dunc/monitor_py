#!/usr/bin/env python3
import json
import os
import sys

from core import check
from core import telegram_send

class Config:
    @staticmethod
    def load_config():
        config_path = os.path.join(os.path.dirname(__file__), 'config.json')
        try:
            with open(config_path) as f:
                return json.load(f)
        except Exception as e:
            print(f"Error loading config: {str(e)}")
            sys.exit(1)

    @staticmethod
    def load_ips():
        """Load the IPs to monitor"""
        ips_path = os.path.join(os.path.dirname(__file__), 'ips.json')
        try:
            with open(ips_path) as f:
                return json.load(f)
        except Exception as e:
            print(f"Error loading IPs: {str(e)}")
            sys.exit(1)

def check_hosts(ip_list):

    hosts = []
    offline_hosts = []
    
    print(f"Monitoring {len(ip_list.keys())} hosts...")
    
    for hostname, ip in ip_list.items():
        is_online = check.icmp(ip)
        status = "up" if is_online else "down"
        
        host_info = {
            "name": hostname,
            "ip": ip,
            "online": is_online
        }
        hosts.append(host_info)
        
        print(f"{hostname} ({ip}) is {status}")
        
        if not is_online:
            offline_hosts.append(host_info)
    
    return hosts, offline_hosts

def main():
    config = Config.load_config()
    ip_list = Config.load_ips()

    hosts, offline_hosts = check_hosts(ip_list)

    if config.get("alerts-enabled"):
        print("Sending Telegram status update")
        telegram_send.send_status_update(config, hosts)
    
    if offline_hosts:
        print(f"\nSummary: {len(offline_hosts)} of {len(hosts)} hosts are offline")
    else:
        print("\nSummary: All hosts are online")

if __name__ == '__main__':
    main()