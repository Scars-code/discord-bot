import json
from datetime import datetime, timedelta

user_balance = {}
user_messages = {}
user_cooldowns = {}

try:
    with open("economy.json", "r") as f:
        data = json.load(f)
        user_balance = data.get("balance", {})
        user_messages = data.get("messages", {})
        user_cooldowns = data.get("cooldowns", {})
except (FileNotFoundError, json.JSONDecodeError):
    pass


def check_account(username: str) -> None:
    global user_balance, user_messages, user_cooldowns
    
    if username not in user_balance:
        user_balance[username] = 100
        user_messages[username] = 0
        user_cooldowns[username] = "2000-01-01 00:00:00"
        
        with open("economy.json", "w") as f:
            json.dump({
                "balance": user_balance, 
                "messages": user_messages, 
                "cooldowns": user_cooldowns
            }, f)


def work(username: str):
    global user_balance, user_messages, user_cooldowns
    check_account(username)
    
    right_now = datetime.now()
    unlock_time = datetime.strptime(user_cooldowns[username], "%Y-%m-%d %H:%M:%S")
    
    if right_now >= unlock_time:
        messages_sent = user_messages[username]
        earnings = (messages_sent * 5) + 20
        
        user_messages[username] = 0
        user_balance[username] += earnings
        
        future_lock = right_now + timedelta(days=1)
        user_cooldowns[username] = future_lock.strftime("%Y-%m-%d %H:%M:%S")
        
        with open("economy.json", "w") as f:
            json.dump({
                "balance": user_balance, 
                "messages": user_messages, 
                "cooldowns": user_cooldowns
            }, f)
            
        print(f"Congrats you earned {earnings} coins!")
        return f"SUCCESS:{earnings}"
        
        
    else:
        time_left = unlock_time - right_now
        total_seconds = int(time_left.total_seconds())
        hours = total_seconds // 3600
        minutes = (total_seconds % 3600) // 60
        seconds = total_seconds % 60
        return f"LOCKED:{hours}h {minutes}m {seconds}s"
