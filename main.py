from funcartur import artur, inoyatov
from fastapi import FastAPI
from pydantic import BaseModel


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

