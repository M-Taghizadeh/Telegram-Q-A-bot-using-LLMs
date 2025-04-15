# Telegram Q&A Bot using LLMs (GPT-4o)

This project is a fully functional Telegram bot powered by OpenAI's GPT-4o model. The bot can answer a wide range of questions, from general knowledge to technical programming inquiries, making it a versatile assistant right inside your Telegram chat.

## 📌 Features

- Answer general knowledge and programming questions
- Natural language understanding via GPT-4o
- Hosted using [PythonAnywhere](https://www.pythonanywhere.com/)
- Clean and modular Python code
- Easy to extend and customize

## 🛠️ Technologies Used

- Python 3
- Telegram Bot API (`python-telegram-bot`)
- OpenAI GPT-4o API
- PythonAnywhere (for deployment)

## 📖 What You'll Learn

- How to build a Telegram bot with Python
- How to integrate LLMs like GPT-4o into a chat interface
- How to deploy Python applications on PythonAnywhere

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/M-Taghizadeh/Telegram-Q-A-bot-using-LLMs.git
cd Telegram-Q-A-bot-using-LLMs
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Set Up Environment Variables
```bash
TELEGRAM_BOT_TOKEN=your_telegram_bot_token
OPENAI_API_KEY=your_openai_api_key
```

You can generate your tokens from:
- [BotFather on Telegram](https://telegram.me/BotFather)
- [OpenAI API Key](https://platform.openai.com/account/api-keys)

### 4. Run the Bot Locally
```bash
python bot.py
```

### 5. Deploy on PythonAnywhere
Create an account at [pythonanywhere.com](pythonanywhere.com)
Upload your files via the dashboard or Git
Set up a "Always-on task" to run your bot

## 🤖 Example Interaction
```
>> User: What's the capital of Germany?
>> Bot: The capital of Germany is Berlin. 🇩🇪
```

## 📂 Project Structure
```
Telegram-Q&A-bot-using-LLMs/
│
├── app.py                # Main bot logic
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation
```

## 🤝 Contributions
Feel free to fork this repository, open issues, or submit pull requests. Contributions are welcome!