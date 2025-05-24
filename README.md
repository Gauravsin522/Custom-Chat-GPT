# 🧠 Custom ChatGPT — Your Personal AI Conversationalist

Welcome to **Custom ChatGPT**, a modular, customizable, and developer-friendly interface to interact with a GPT-based AI model. This repository is your entry point into building, tweaking, and running your own personalized version of ChatGPT — no fluff, just function.

---

## 🚀 Why This Project?

In a world of generic AI chatbots, **Custom ChatGPT** gives you the reins to build something truly yours. Whether you're a researcher, developer, or hobbyist, this project provides a robust foundation to:

- 🌐 Prototype an AI assistant
- 🔧 Tweak GPT settings via config
- 📚 Analyze conversations and logs
- 🤖 Experiment with AI behavior using Notebooks

---

## 🧭 Features at a Glance

✅ Modular architecture  
✅ Config-driven customization (`config.yaml`)  
✅ Integrated logging (`logs/app.log`)  
✅ Jupyter-based analysis tools  
✅ Lightweight and fast to deploy  

---

## 📁 Project Directory

Custom-Chat-GPT/
│
├── app/ # Core application script
│ └── app.py
│
├── config/ # YAML configuration file
│ └── config.yaml
│
├── logger/ # Logging utility
│ └── logger.py
│
├── logs/ # Runtime logs for traceability
│ └── app.log
│
├── Notebook/ # Jupyter notebooks for testing and analysis
│ └── analysis.ipynb
│
├── requirements.txt # Project dependencies
└── README.md # You’re reading it


---

## ⚙️ Configuration Magic

All key parameters — model details, token settings, logging preferences — are stored in a single `config.yaml` file. Change it, tune it, experiment freely.

```yaml
model_name: "gpt-3.5-turbo"
temperature: 0.7
max_tokens: 500
log_level: "INFO"

🛠️ Setup & Installation
1. Clone this repo

git clone https://github.com/Gauravsin522/Custom-Chat-GPT.git
cd Custom-Chat-GPT

2. (Optional) Create a virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

3. Install dependencies
pip install -r requirements.txt

🧪 Run the Chat App
Kick off the application with:
python app/app.py

🗨️ You’ll now be chatting with a GPT model using your custom setup.

📊 Jupyter Notebook (for Analysts & Tinkerers)
Inside the Notebook/ folder, you’ll find analysis.ipynb — a playground for:

Understanding input/output flow

Visualizing token usage

Prompt tuning experiments

📝 Logging Everything
Logs are automatically saved in logs/app.log. Stay informed on:

Session activity

Errors and exceptions

Timestamped conversations

🔒 Security & API Notes
⚠️ Note: This project assumes you already have access to an OpenAI API key or similar. DO NOT hardcode sensitive keys into the repo.

Use environment variables or .env files for security:

export OPENAI_API_KEY="your-key-here"

🤝 Contribution Guidelines
We welcome contributions of all kinds — code, ideas, issues, even documentation.

Fork the repository

Create a new branch (git checkout -b feature-name)

Commit your changes

Push and open a Pull Request

Let’s make AI better — together.

👨‍💻 Author
Gaurav Singh
📍 Delhi, India
📧 gauravsin333@gmail.com
🔗 LinkedIn
🐙 GitHub

