import requests
import json
import time
import csv
import os
from datetime import datetime

URLS_FILE = "data/urls.json"
LOG_FILE = "logs/pulse-log.csv"

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

def log_result(result):
    os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
    file_exists = os.path.isfile(LOG_FILE)
    with open(LOG_FILE, mode='a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=["timestamp", "url", "status", "latency", "error"])
        if not file_exists:
            writer.writeheader()
        writer.writerow({
            "timestamp": result["timestamp"],
            "url": result["url"],
            "status": result["status"],
            "latency": result.get("latency", ""),
            "error": result.get("error", "")
        })

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
