# silentpulse/src/pulse.py
import requests
import json
import time
from datetime import datetime

URLS_FILE = "data/urls.json"


def load_urls():
    with open(URLS_FILE, "r") as f:
        return json.load(f)


def pulse_url(url):
    try:
        start = time.time()
        response = requests.get(url, timeout=10)
        latency = round((time.time() - start) * 1000)  # ms
        return {
            "url": url,
            "status": response.status_code,
            "latency": latency,
            "timestamp": datetime.utcnow().isoformat() + "Z"
        }
    except requests.RequestException as e:
        return {
            "url": url,
            "status": "FAILED",
            "latency": None,
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "error": str(e)
        }


def main():
    urls = load_urls()
    results = []
    for url in urls:
        result = pulse_url(url)
        print(f"[{result['timestamp']}] {result['url']} => {result['status']} ({result.get('latency', '-')})ms")
        results.append(result)


if __name__ == "__main__":
    main()
