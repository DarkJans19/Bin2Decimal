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


def convert_binary_to_decimal(binary):
    if len(binary) > 8:
        raise ValueError("You can only convert 8 binary length")
    
    for i in range(len(binary)):
        if binary[i] != '1' and binary[i] != '0':
            raise ValueError("The binary number can only have 1 or 0")

    result = 0

    for bit in binary:
        print(result)
        result = result * 2 + int(bit)

    return result


@app.post("/")
def process_form(req: Request, binary_number: str = Form()):
    result = None
    error_msg = None
    try:
        result = convert_binary_to_decimal(binary_number)
    except ValueError as e:
        error_msg = str(e)

    return template.TemplateResponse(
        request=req,
        name="index.html",
        context={
            "resultado_decimal": result,
            "error_detectado": error_msg,
            "numero_previo": binary_number
        }
    )


if __name__ == "__main__":
    uvicorn.run("main:app")



