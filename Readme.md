# FIO Project 320. Платформа для покупки и продажи.
 git clone <URL_вашего_репозитория> bash
 python -m venv .venv # venv
 .venv\Scripts\activate # activate
 pip install -r requirements.txt
 uvicorn main:app --reload # проверить через uvicorn
### Запуск через Docker Вот теперь основной…
1. **Соберите Docker образ:**
 docker build -t project320 .
2. **Запустите контейнер:**
 docker run -p 8000:8000 project320
- Swagger UI: http://127.0.0.1:8000/docs