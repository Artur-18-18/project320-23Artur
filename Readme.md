# FIO Project 320. Платформа для покупки и продажи.
 git clone <URL_вашего_репозитория> bash
 python -m venv .venv # venv
 .venv\Scripts\activate # activate
 pip install -r requirements.txt
 uvicorn main:app --reload # проверить через uvicorn
### Запуск через Docker (используйте строчные буквы в теге)
1. **Соберите Docker образ:**
```powershell
# Тег должен быть в нижнем регистре, например:
docker build -t project320-23artur:latest .
```
2. **Запустите контейнер:**
```powershell
docker run --rm -p 8000:8000 project320-23artur:latest
```

Примечание: Docker требует, чтобы имя репозитория/тега было в нижнем регистре. Если ранее запускали с тегом с заглавными буквами — используйте новый тег или выполните `docker tag` для переименования образа.

Swagger UI: http://127.0.0.1:8000/docs