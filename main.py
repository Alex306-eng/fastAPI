from fastapi import FastAPI
from fastapi.responses import HTMLResponse

# object of app
app = FastAPI()

# функция, которая будет обрабатывать запросы к приложеню
# в данной реализации это запросы к корню веб-приложения
@app.get('/')
def read_root():
    # when client make request to address he get this content
    html_content = "<h2>Hello METANIT.com <\h2>"
    return HTMLResponse(content=html_content)