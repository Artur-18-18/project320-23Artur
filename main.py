from funcartur import artur, inoyatov
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
from proekt320ShakirjanovXasan import p1
import funcSoliyev as s
from pathlib import Path


print(artur(6,3))
print(inoyatov(25,5))

print(p1(2,3))


app = FastAPI( title="proj320-23Artur",
version="1.0.0",
description="Платформа для покупки и продажи",
docs_url="/docs",
redoc_url="/redoc",)
#debug=settings.DEBUG, # Используем из настроек)

class TwoNumbers(BaseModel):
 x: float
 y: float

@app.get("/artur")
def get_c2(x: float, y: float):
 return {"result": artur(x, y)}
@app.post("/artur")
def post_c2(data: TwoNumbers):
 return {"result": artur(data.x, data.y)}

@app.get("/inoyatov")
def get_inoyatov(x: float, y: float ):
    return {"result": inoyatov(x, y)}
@app.post("/inoyatov")
def post_inoyatov(data: TwoNumbers):
    return {"result": inoyatov(data.x, data.y)}

@app.get("/Shakirjanov")
def get_p1(x: float, y: float):
    return {"result": p1(x, y)}

@app.post("/Shakirjanov")
def post_p1(data: TwoNumbers):
    return {"result": p1(data.x,data.y)}

@app.get("/soliyev")
def get_soliyev(x: float, y: float):
    return {"result": s.func_soliyev(x, y)}

@app.post("/soliyev")
def post_soliyev(data: TwoNumbers):
    return {"result": s.func_soliyev(data.x, data.y)}

# Ilyas: вычислить гипотенузу (c2)
@app.get("/c2")
def get_c2_ilyas(x: float, y: float):
    """Возвращает гипотенузу для прямоугольного треугольника: sqrt(x^2 + y^2)"""
    return {"result": (x**2 + y**2) ** 0.5}

@app.post("/c2")
def post_c2_ilyas(data: TwoNumbers):
    """POST: принимает JSON {x, y} и возвращает hypot"""
    return {"result": (data.x**2 + data.y**2) ** 0.5}

@app.get("/Rashidov")
def get_rashidov(x: float, y: float):
    return {"result": rashidov(x, y)}

@app.post("/Rashidov")
def post_rashidov(data: TwoNumbers):
    return {"result": rashidov(data.x, data.y)}

@app.get("/")
def read_root():
    """Возвращает index.html при открытии корневого URL"""
    try:
        file_path = Path(__file__).parent / "index.html"
        print(f"Trying to open: {file_path}")
        print(f"File exists: {file_path.exists()}")
        if file_path.exists():
            return FileResponse(str(file_path), media_type="text/html")
        else:
            return {"error": f"File not found: {file_path}"}
    except Exception as e:
        print(f"Error: {e}")
        return {"error": str(e)}