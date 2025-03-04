# monitor_py

Python script to monitor a list of IP addresses and notify a user through Telegram.
## Overview

This tool is designed to run as a cronjob to regularly check the status of a list of IP addresses and send a complete status update to your Telegram chat every time it runs.

- Ping monitoring for multiple IP addresses
- Telegram status updates with both online and offline hosts
- Easy configuration via JSON files

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/c-dunc/monitor_py
   cd monitor_py
   ```

2. Install the required dependencies:
   ```
   pip3 install -r requirements.txt
   ```

3. Configure the settings:
   - Edit `src/config.json` with your bot settings
   - Edit `src/ips.json` with the hosts you want to monitor



Each entry consists of a hostname (used for identification) and its IP address.

Since the status update is sent every time the script runs, you'll receive a message on each cronjob execution. This gives you real-time visibility into your network status.

## License

[MIT License](LICENSE)