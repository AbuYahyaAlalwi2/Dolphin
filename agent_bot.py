import os
import requests
import time
from playwright.sync_api import sync_playwright

# سحب البيانات من متغيرات السيرفر
TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

def send_msg(text):
    if not TOKEN or not CHAT_ID:
        return
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, json={"chat_id": CHAT_ID, "text": text})

def execute_task(command):
    if "افتح جوجل" in command:
        send_msg("جاري تنفيذ طلبك يا سيدي...")
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()
            page.goto("https://www.google.com")
            send_msg("تم فتح جوجل بنجاح.")
            browser.close()
    elif "سجل الدخول" in command:
        send_msg("عملية تسجيل الدخول قيد التطوير...")

if __name__ == "__main__":
    print("دولفين يعمل الآن في السحابة...")
    last_update_id = 0
    while True:
        try:
            url = f"https://api.telegram.org/bot{TOKEN}/getUpdates?offset={last_update_id + 1}"
            response = requests.get(url).json()
            if response.get('result'):
                for update in response['result']:
                    last_update_id = update['update_id']
                    msg = update.get('message', {}).get('text', '')
                    if msg:
                        execute_task(msg)
        except Exception as e:
            print(f"خطأ: {e}")
        time.sleep(2)