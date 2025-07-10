# AllMightGPT — Flask Chatbot Powered by DialoGPT

A web-based chatbot styled after **All Might** from *My Hero Academia*, powered by **Hugging Face DialoGPT** and built with **Flask**.

## Project Structure

```
chatbot/
│
├── app.py              # Flask backend
├── requirements.txt    # Python dependencies
├── templates/
│   └── index.html     # Frontend UI (chat interface)
└── static/            # Static assets (CSS/JS/images)
```

## Features

* Based on `microsoft/DialoGPT-large`
* Chat with All Might's heroic personality
* Web interface with persistent chat history
* Clear conversation functionality

## Requirements

* Python 3.7+
* pip

## Installation & Usage

1. **Clone the repository**
```bash
git clone https://github.com/DevITJAX/AllMightGPT.git
cd AllMightGPT
```

2. **Create virtual environment (recommended)**
```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
# venv\Scripts\activate   # Windows
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Run the application**
```bash
python app.py
```

5. **Access the chatbot**
Open your browser and go to http://127.0.0.1:5000

## Deployment

Deploy on platforms that support backend services:
* Render.com
* Railway.app
* Azure App Services
* Heroku

### Render Deployment Example

1. Push project to GitHub
2. Create new Web Service in Render
3. Configure:
   * **Start command**: `gunicorn app:app`
   * **Build command**: `pip install -r requirements.txt`
4. Deploy

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Chat interface |
| POST | `/chat` | Send message, get response |
| GET | `/health` | Health check |

## License

MIT License

## Author

Developed by **DevITJAX**  
Inspired by *My Hero Academia*
