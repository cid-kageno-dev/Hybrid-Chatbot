# Hybrid AI Chatbot (Gemini + Google Sheets)

A professional, Flask-based chatbot that uses **Google Gemini 2.5 Flash** for intelligent responses and **Google Sheets** as a dual-purpose database (History Log & Fallback Knowledge Base).

If the AI service is down or fails, the bot automatically switches to "Fallback Mode," searching the Google Sheet for similar past queries using fuzzy matching to provide an answer.

## 🚀 Features

* **Hybrid Logic:** Seamlessly switches between AI generation and Rule-Based fallback.
* **AI Power:** Uses Google's efficient `gemini-2.5-flash` model.
* **Knowledge Base:** Automatically learns by saving successful AI interactions to Google Sheets.
* **Zero Latency Logging:** Uses background threading to save data to Sheets without slowing down the user response.
* **Fuzzy Matching:** Uses `thefuzz` to find answers in the sheet even if the user makes typos.
* **Production Ready:** Modular folder structure and Gunicorn configuration for deployment.

## 📂 Project Structure

```text
Hybrid-Chatbot/
│
├── .env                    # API Keys (GitIgnored)
├── credentials.json        # Google Service Account Key (GitIgnored)
├── run.py                  # Entry point
├── config.py               # Configuration loader
├── requirements.txt        # Dependencies
│
└── app/
    ├── __init__.py
    ├── routes.py           # API Endpoints
    └── services/
        ├── ai_service.py   # Gemini Logic
        └── sheet_service.py# Google Sheets & Fallback Logic

🛠️ Prerequisites
 * Python 3.9+
 * Google Cloud Project with Sheets and Drive APIs enabled.
 * Google AI Studio Key (for Gemini).
⚙️ Local Installation
 * Clone the repository
   git clone [https://github.com/your-username/your-repo-name.git](https://github.com/your-username/your-repo-name.git)
cd your-repo-name

 * Create a Virtual Environment
   python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

 * Install Dependencies
   pip install -r requirements.txt

 * Setup Credentials
   * Step A: Place your Google Service Account key in the root folder and name it credentials.json.
   * Step B: Create a .env file in the root folder and add:
     GOOGLE_API_KEY=AIzaSy...
SHEET_NAME=Chatbot_KB
GOOGLE_SHEET_CREDS=credentials.json

   * Step C: Share your Google Sheet (Chatbot_KB) with the client_email found inside your credentials.json.
🏃‍♂️ Usage
 * Start the Server
   python run.py

 * Test the Endpoint
   Send a POST request to http://127.0.0.1:5000/chat:
   Payload:
   {
  "message": "Hello, who are you?"
}

   Response:
   {
  "response": "I am Ani, Your Personal AI Assistant...",
  "source": "AI Response"
}

☁️ Deployment (Render.com)
This project is configured for easy deployment on Render.
 * New Web Service: Connect your GitHub repo.
 * Build Command: pip install -r requirements.txt
 * Start Command: gunicorn run:app
 * Environment Variables:
   * GOOGLE_API_KEY: Your Gemini Key.
   * SHEET_NAME: Chatbot_KB
   * GOOGLE_SHEET_CREDS: /etc/secrets/credentials.json


📄 License
This project is open-source and available for modification.

Author: Cid Kageno

