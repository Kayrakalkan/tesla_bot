# 🚗 Tesla Stock Monitor Bot

A Python-based automation bot that monitors Tesla Model Y inventory on the Turkish Tesla website and sends real-time SMS notifications when the desired vehicle becomes available in stock.

## 📋 Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Docker Deployment](#docker-deployment)
- [How It Works](#how-it-works)
- [Contributing](#contributing)
- [License](#license)

## ✨ Features

- **Automated Web Monitoring**: Uses Playwright to automate browser interactions and check Tesla inventory in real-time
- **Smart Notifications**: Sends SMS alerts via Twilio when the target vehicle is in stock
- **Modal Handling**: Intelligently handles and closes modal dialogs on the website
- **Containerized Deployment**: Includes Dockerfile for easy Docker deployment
- **Environment Configuration**: Secure credential management using environment variables
- **Error Handling**: Robust error handling for network and UI element detection

## 🛠️ Tech Stack

| Technology | Purpose |
|-----------|---------|
| **Python 3.10** | Core programming language |
| **Playwright** | Browser automation and web scraping |
| **Twilio** | SMS notification service |
| **Docker** | Containerization and deployment |
| **Python-dotenv** | Environment variable management |

## 📦 Prerequisites

- Python 3.10+
- Twilio account with SMS credentials
- .env file with Twilio credentials
- Docker (optional, for containerized deployment)

## 🚀 Installation

### Local Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/Kayrakalkan/tesla_bot.git
   cd tesla_bot
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   python -m playwright install --with-deps
   ```

## ⚙️ Configuration

1. **Create a .env file** in the project root:
   ```env
   TWILIO_ACCOUNT_SID=your_account_sid_here
   TWILIO_AUTH_TOKEN=your_auth_token_here
   ```

2. **Update phone numbers in app.py**:
   - `twilio_from`: Your Twilio phone number
   - `twilio_to`: The phone number to receive alerts

3. **Customize the target vehicle** (optional):
   - Modify the selector in the `check_stock()` function to track different Tesla models

## 💻 Usage

### Run Locally

```bash
python app.py
```

The bot will:
1. Launch a Chromium browser (headless mode optional)
2. Navigate to the Tesla Turkish website
3. Select the Tesla Model Y Long Range variant
4. Check inventory status
5. Send an SMS notification if the vehicle is in stock

### Schedule with Cron (Unix/Linux/macOS)

To run the bot at regular intervals, add a cron job:

```bash
# Run every 30 minutes
*/30 * * * * cd /path/to/tesla_bot && python app.py
```

## 🐳 Docker Deployment

### Build the Docker Image

```bash
docker build -t tesla-bot:latest .
```

### Run as a Container

```bash
docker run --env-file .env tesla-bot:latest
```

### Run with Docker Compose (recommended)

Create a `docker-compose.yml`:
```yaml
version: '3.8'
services:
  tesla-bot:
    build: .
    env_file: .env
    restart: on-failure
```

Then run:
```bash
docker-compose up -d
```

## 🔍 How It Works

```
1. Initialize Playwright browser
   ↓
2. Navigate to Tesla.com (Turkish site)
   ↓
3. Close modal dialogs if present
   ↓
4. Select target vehicle (Model Y Long Range)
   ↓
5. Check for "Get Updates" button
   ↓
6. If button NOT found → Vehicle is in stock → Send SMS ✓
   ↓
7. If button found → Vehicle is out of stock → Exit silently
   ↓
8. Close browser
```

## 🎯 Project Structure

```
tesla_bot/
├── app.py              # Main application logic
├── requirements.txt    # Python dependencies
├── Dockerfile          # Container configuration
├── .env               # Environment variables (not committed)
├── .gitignore         # Git ignore rules
└── README.md          # This file
```

## 🔐 Security

- Credentials are stored in `.env` files (never committed to git)
- Add `.env` to `.gitignore` to prevent credential leaks
- Use environment variables for all sensitive data

## 🚦 Error Handling

The bot gracefully handles:
- Missing modal dialogs
- Network timeouts
- Element detection failures
- Twilio API errors

## 📈 Future Enhancements

- [ ] Support for multiple Tesla models
- [ ] Email notification option
- [ ] Web dashboard for monitoring history
- [ ] Database logging of stock changes
- [ ] Configurable monitoring intervals
- [ ] Multiple user support with database
- [ ] Telegram bot integration
- [ ] Price tracking notifications

## 🤝 Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues for bugs and feature requests.

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👨‍💻 Author

**Kayra Kalkan**
- GitHub: [@Kayrakalkan](https://github.com/Kayrakalkan)

## 📞 Support

For issues or questions, please open an issue on GitHub or contact the maintainer.

---

**Note**: This project is for educational purposes. Make sure to follow Tesla's Terms of Service when using automated tools to access their website.
