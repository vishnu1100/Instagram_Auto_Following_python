# Instagram Automation Bot

## Description
This bot automates Instagram activity by following 50 users daily from specified hashtags. Actions are logged to a file (`follow_log.txt`) with timestamps.

## Features
- Logs all follows to `follow_log.txt`.
- Random delays between actions to mimic human behavior.
- Avoids activity during late-night hours.

## Prerequisites
- Python 3.8+
- Instagram account credentials.

## Setup
1. Clone this repository:
   ```bash
   git clone https://github.com/vishnu1100/Instagram_Auto_Following_python.git
   cd instagram-bot
Create and activate a virtual environment:

bash
Copy code
python3 -m venv venv
source venv/bin/activate
Install dependencies:

bash
Copy code
pip install instagrapi
Add your credentials to environment variables:

bash
Copy code
export USERNAME="your_username"
export PASSWORD="your_password"
Run the bot:

bash
Copy code
python3 instagram_bot.py
Deployment
To deploy on Render, follow these steps:

Link this repository to Render.
Set environment variables (USERNAME, PASSWORD).
Configure a daily cron job to execute the bot.
Disclaimer
Use this bot responsibly and adhere to Instagram's Terms of Service.

yaml
Copy code

---

Let me know if you’d like further customization or help with deployment! 😊
