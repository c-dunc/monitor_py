import requests

def send_status_update(config, hosts):

    telegram_config = config.get("telegram", {})
    bot_token = telegram_config.get("bot_token")
    chat_id = telegram_config.get("chat_id")
    
    if not bot_token or not chat_id:
        print("Telegram configuration incomplete")
        return False
    
    api_url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    
    online_hosts = [host for host in hosts if host.get("online", False)]
    offline_hosts = [host for host in hosts if not host.get("online", False)]
    
    message = "*📊 IP Monitoring Status Update*\n\n"
    
    message += f"*Summary:* {len(online_hosts)} online, {len(offline_hosts)} offline\n\n"
    
    if online_hosts:
        message += "*🟢 Online Hosts:*\n"
        for host in online_hosts:
            message += f"• *{host['name']}* ({host['ip']})\n"
        message += "\n"
    
    if offline_hosts:
        message += "*🔴 Offline Hosts:*\n"
        for host in offline_hosts:
            message += f"• *{host['name']}* ({host['ip']})\n"
        message += "\n"
    
    message += "_Monitoring System_"
    
    params = {
        "chat_id": chat_id,
        "text": message,
        "parse_mode": "Markdown"
    }
    
    try:
        response = requests.post(api_url, params=params)
        
        if response.status_code == 200:
            print("Telegram status update sent successfully")
            return True
        else:
            print(f"Failed to send Telegram update: HTTP {response.status_code}")
            print(response.text)
            return False
    except Exception as e:
        print(f"Failed to send Telegram update: {str(e)}")
        return False