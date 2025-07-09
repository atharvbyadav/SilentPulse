# ⚡ SilentPulse

> A lightweight GitHub Actions-powered pulse engine to silently keep your essential services alive.  
> Built by [Atharv Yadav](https://github.com/atharvbyadav)

---

![SilentPulse Status](https://github.com/atharvbyadav/SilentPulse/actions/workflows/silentpulse.yml/badge.svg)
![Last Commit](https://img.shields.io/github/last-commit/atharvbyadav/SilentPulse)
![Repo Size](https://img.shields.io/github/repo-size/atharvbyadav/SilentPulse)
![Stars](https://img.shields.io/github/stars/atharvbyadav/SilentPulse?style=social)
![Uptime](https://img.shields.io/badge/Uptime-Operational-brightgreen?style=flat-square&logo=heartbeat)

---

## 🔧 Features (v1.1)

- 🧠 **Pulse Engine:** Uses GitHub Actions to periodically "pulse" (ping) your web services
- 📡 **Custom URL list:** Easily editable via `data/urls.json`
- 📄 **CSV Logging:** Outputs detailed pulse logs to `logs/pulse-log.csv`
- 🕒 **Scheduled Execution:** Runs automatically every 30 minutes
- 🛠️ **Manual Trigger Support:** You can also run it anytime from the GitHub Actions tab
- 📁 **Minimal Dependencies:** Just Python + `requests`

---

## 🚀 How It Works

SilentPulse reads a list of URLs from `data/urls.json`, sends GET requests to each, and logs:

- HTTP status code
- Response time (ms)
- Timestamp
- Error info (if failed)

---

## 📦 Project Structure

```

SilentPulse/
├── .github/workflows/silentpulse.yml   # GitHub Actions workflow
├── data/urls.json                      # List of URLs to pulse
├── logs/pulse-log.csv                  # Auto-generated pulse logs
├── src/pulse.py                        # Core pulse script
├── requirements.txt                    # Python dependencies
└── README.md                           # You’re reading it

```

---

## ✍️ Setup

> 💡 This project runs **entirely on GitHub Actions** — no server needed.

1. **Fork or clone** this repo
2. Add your URLs to `data/urls.json`:

   ```json
   ["https://your-app-1.com", "https://your-streamlit-app.net"]
   ```

3. (Optional) Modify `pulse.py` or logging logic if needed
4. Push to your `main` branch

---

## 🔄 GitHub Actions

The workflow is located at `.github/workflows/silentpulse.yml`.

It runs:

- 🕓 Every 30 minutes (`0,30 * * * *`)
- ✅ Can also be run manually from GitHub UI

You can see your logs in the **Actions → Run SilentPulse** → `Run SilentPulse` step.

---

## 🧪 Output Example

Console output from a pulse run:

```
[2025-07-09T20:20:08Z] https://reconx.streamlit.app => 200 (1041)ms
[2025-07-09T20:20:08Z] https://ghostpath.onrender.com => FAILED (-)ms
```

Sample CSV log:

```csv
timestamp,url,status,latency,error
2025-07-09T20:20:08Z,https://reconx.streamlit.app,200,1041,
2025-07-09T20:20:08Z,https://ghostpath.onrender.com,FAILED,,ConnectionError
```

---

## 🚧 Roadmap (Future Versions)

> SilentPulse is modular — features will be added incrementally.

- 📊 Web Dashboard for uptime monitoring
- 📈 Uptime % and pulse stats
- 🔔 Alerts (Telegram, Discord, Email)
- 🌐 Dynamic status badges
- 🌍 Public status page
- 🧩 Plugin system for multiple services

---

## 📜 License

[MIT License](LICENSE)

---

## 🤝 Contributing

Want to extend SilentPulse? Open a PR or raise an issue.
Let’s make uptime silent and strong. 💡

---
