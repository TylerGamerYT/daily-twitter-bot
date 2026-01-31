# Daily Twitter Bot

A simple Python bot that posts a custom message to a Twitter/X account once per day at a random or fixed time.

This bot is configurable via `config.json`, so you can set your own message and Twitter API keys.

---

## Features

* Posts a custom message daily
* Random or fixed posting time
* Fully configurable via `config.json`
* Easy to run locally or host online

---

## Requirements

* Python 3.8+
* Twitter/X Developer account with API keys:

  * API Key
  * API Secret
  * Access Token
  * Access Token Secret
* Tweepy Python library

---

## Setup

1. **Clone this repository:**

```bash
git clone https://github.com/TylerGamerYT/daily-twitter-bot.git
cd daily-twitter-bot
```

2. **Install dependencies:**

```bash
pip install -r requirements.txt
```

3. **Configure the bot:**

Open `config.json` and replace the placeholders with your Twitter API keys and the message you want to post:

```json
{
  "API_KEY": "YOUR_API_KEY_HERE",
  "API_SECRET": "YOUR_API_SECRET_HERE",
  "ACCESS_TOKEN": "YOUR_ACCESS_TOKEN_HERE",
  "ACCESS_SECRET": "YOUR_ACCESS_SECRET_HERE",
  "POST_MESSAGE": "hello world",
  "MODE": "random",
  "FIXED_HOUR": 14,
  "FIXED_MINUTE": 30
}
```

* `"POST_MESSAGE"` → The text the bot will post daily
* `"MODE"` → `"random"` for a random daily time, `"fixed"` for a specific time
* `"FIXED_HOUR"` & `"FIXED_MINUTE"` → Used only if `"MODE"` is `"fixed"`

---

4. **Run the bot:**

```bash
python bot.py
```

* The bot will post your message once per day according to your settings.
* Keep the terminal open for continuous posting.

---

## Optional Hosting

* Run the bot 24/7 using:

  * [Replit](https://replit.com/)
  * [PythonAnywhere](https://www.pythonanywhere.com/)
  * A small VPS/server

* Update `POST_MESSAGE` anytime in `config.json` to change your daily message.

---

# Made By

# **Tyler** and his friend **Chloe**
