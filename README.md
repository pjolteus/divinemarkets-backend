# DivineMarkets AI Backend

This is the backend service for **DivineMarkets**, a predictive AI-driven stock options platform.  
It uses machine learning to generate day-trading signals, predict entry/exit points, and assess bankruptcy risks — all exposed via a robust FastAPI framework.

---

## 🚀 Features

- 📈 Daily stock option signals (CALL & PUT)
- 🎯 Entry, Exit, and Stop-Loss price prediction
- ⚠️ Bankruptcy & volatility risk analysis
- ⚡ FastAPI + modular AI engine design
- 🔐 CORS-enabled and ready for frontend integration

---

## 📦 Project Structure

```
divinemarkets_backend/
├── main.py
├── requirements.txt
├── routes/
│   └── oracle_routes.py
├── models/
│   └── schemas.py
├── services/
│   ├── oracle_engine.py
│   ├── oracle_api_integration.py
│   ├── oracle_signal_generator.py
│   ├── oracle_entry_exit_model.py
│   ├── oracle_entry_exit_inference.py
│   ├── oracle_bankruptcy_model.py
│   ├── oracle_bankruptcy_inference.py
│   ├── oracle_data_pipeline.py
│   └── oracle_model_training.py
```

---

## ⚙️ Deployment (Render.com)

1. Push this project to a GitHub repository
2. Go to [https://render.com](https://render.com)
3. Create a **Web Service** with the following settings:
   - **Build Command**:  
     ```
     pip install -r requirements.txt
     ```
   - **Start Command**:  
     ```
     uvicorn main:app --host 0.0.0.0 --port 10000
     ```
4. Click deploy — your live public API will be available shortly!

---

## 📡 Endpoints

| Method | Endpoint                        | Description                             |
|--------|----------------------------------|-----------------------------------------|
| GET    | `/`                              | API health check                        |
| GET    | `/docs`                          | Swagger UI (interactive API docs)       |
| GET    | `/oracle/daily-signals`          | Top 10 daily stock signals (5 CALL/PUT) |
| POST   | `/oracle/entry-exit`             | Entry, exit, and stop-loss prediction   |
| GET    | `/oracle/risk-report/{ticker}`   | Bankruptcy and volatility risk report   |
| GET    | `/oracle/history/{ticker}`       | Mock signal history                     |

---

## 📜 License

MIT License — Use it freely. Credit appreciated.

---

## 🤝 Contact

Philippe Jolteus  
[https://divinemarkets.org](https://divinemarkets.org)
