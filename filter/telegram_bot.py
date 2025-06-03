import requests

TELEGRAM_TOKEN = "your_token"
CHAT_ID = "your_chat_id"

def send_telegram_message(text):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    data = {
        'chat_id': CHAT_ID,
        'text': text
    }
    response = requests.post(url, data=data)
    return response.json()
