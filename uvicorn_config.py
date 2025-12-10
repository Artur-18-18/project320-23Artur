"""
Конфигурация для uvicorn
Позволяет запускать сервер с помощью: uvicorn main:app --reload
и автоматически использует 127.0.0.1:8000
"""

import uvicorn

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=8000,
        reload=True
    )
