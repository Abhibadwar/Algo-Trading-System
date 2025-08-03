import requests

BOT_TOKEN = '84679910:AAFMIF8ebxkTou7zgeX6DeLEZlz9zkjd0sU'
CHAT_ID = '84679910'
MESSAGE = '🚀 Hello from my Python bot!'

def send_telegram_alert(message):
    url = f"https://api.telegram.org/bot84679910:AAFMIF8ebxkTou7zgeX6DeLEZlz9zkjd0sU/getUpdates"
    data = {'chat_id': 8467991049, 'text': message}
    response = requests.post(url, data=data)
    print(response.json())

send_telegram_alert(MESSAGE)
