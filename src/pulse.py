# silentpulse/src/pulse.py

import requests
import json
import time
import os
from datetime import datetime

URLS_FILE = "data/urls.json"
LOG_FILE = "logs/pulse-log.csv"


def load_urls():
    with open(URLS_FILE, "r") as f:
        return json.load(f)


def send_telegram_alert(message):
    token = os.getenv("TELEGRAM_TOKEN_SILENTPULSE")
    chat_id = os.getenv("TELEGRAM_CHAT_ID_SILENTPULSE")
    if not token or not chat_id:
        print("[WARN] Telegram alert skipped (missing secrets)")
        return

    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {"chat_id": chat_id, "text": message}

    try:
        response = requests.post(url, data=payload, timeout=10)
        if response.status_code != 200:
            print(f"[ERROR] Failed to send Telegram alert: {response.text}")
    except Exception as e:
        print(f"[ERROR] Telegram alert error: {e}")


def pulse_url(url):
    try:
        start = time.time()
        response = requests.get(url, timeout=10)
        latency = round((time.time() - start) * 1000)
        result = {
            "url": url,
            "status": response.status_code,
            "latency": latency,
            "timestamp": datetime.utcnow().isoformat() + "Z"
        }

        if response.status_code != 200:
            send_telegram_alert(f"❌ SilentPulse Alert\n{url} returned status: {response.status_code}")

        return result

    except requests.RequestException as e:
        result = {
            "url": url,
            "status": "FAILED",
            "latency": None,
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "error": str(e)
        }
        send_telegram_alert(f"❌ SilentPulse Alert\n{url} is DOWN\nError: {str(e)}")
        return result


def log_result(result):
    headers = ["timestamp", "url", "status", "latency", "error"]
    row = [
        result.get("timestamp", ""),
        result.get("url", ""),
        result.get("status", ""),
        result.get("latency", ""),
        result.get("error", "")
    ]
    write_header = not os.path.exists(LOG_FILE)
    with open(LOG_FILE, "a") as f:
        if write_header:
            f.write(",".join(headers) + "\n")
        f.write(",".join(map(str, row)) + "\n")


def main():
    urls = load_urls()
    results = []
    for url in urls:
        result = pulse_url(url)
        print(f"[{result['timestamp']}] {result['url']} => {result['status']} ({result.get('latency', '-')})ms")
        log_result(result)
        results.append(result)


if __name__ == "__main__":
    main()
