# oxy-grabber

This Python script gathers system information and sends it to a Discord webhook.

## Usage

1. Make sure you have Python installed on your system.
2. Install the `requests` library if you haven't already by running:
    ```
    pip install requests
    ```
3. Replace the `webhook_url` variable in the script with your actual Discord webhook URL.
4. Run the script. It will automatically gather the following system information and send it to the specified Discord webhook:

   - IP Address
   - Username
   - Home Directory
   - Operating System
   - CPU Cores
   - Memory (GB)
   - Machine Architecture
   - Python Version
   - Hostname
   - Boot Time
   - Process ID

## Dependencies

- Python 3.x
- requests library
