# Amazon Price Tracker

## Overview
This project is a web scraping-based Amazon Price Tracker that monitors product prices and sends alerts via SMS (Twilio) and email (SMTP) when the price drops below a target amount.

## Tech Stack
- **Programming Language:** Python
- **Libraries:** BeautifulSoup, Requests
- **Messaging Services:** Twilio API (SMS), SMTP (Email)
- **Scheduler:** Cron Job / Python Scheduling

## Project Workflow
1. **Extract Product Price:** Scrapes live prices from Amazon using BeautifulSoup.
2. **Compare Against Target Price:** If the price drops, the user is notified.
3. **Send Alerts:** Alerts are sent via Twilio SMS & email for instant notifications.

## Features
- ✔️ Automated Amazon price tracking
- ✔️ Alerts via SMS & email
- ✔️ Easy customization for multiple products

## Future Enhancements 🚀
- Multi-platform support (Flipkart, eBay, etc.)
- Historical price tracking using a database
