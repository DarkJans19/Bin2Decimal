import binary_conversions
from fastapi import FastAPI, Form, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import uvicorn

app = FastAPI()
template = Jinja2Templates(directory="templates")

app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
def index(req: Request):
    return template.TemplateResponse(
        request=req,
        name="index.html",
        context={}
    )


@app.post("/")
def process_form(req: Request, number: str = Form(), conversion_type: str = Form()):
    result = None
    error_msg = None
    try:
        if conversion_type == "bin2dec":
            result = binary_conversions.convert_binary_to_decimal(number)
        else:
            result = binary_conversions.convert_decimal_to_binary(number)
    except ValueError as e:
        error_msg = str(e)

    return template.TemplateResponse(
        request=req,
        name="index.html",
        context={
            "resultado": result,
            "error_detectado": error_msg,
            "numero_previo": number,
            "tipo_conversion": conversion_type
        }
    )


if __name__ == "__main__":
    uvicorn.run("main:app")



