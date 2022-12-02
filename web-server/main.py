import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/")
def get_list():
    return [1, 2, 3]

@app.get("/contact",response_class=HTMLResponse)
async def read_items():
    return """
    <html>
        <head>
            <title>Contactos</title>
        </head>
        <body>
            <h1>Compren</h1>
            <p>No se hagan weyes</p>
        </body>
    </html>
    """
#def get_list():
#    return {"name":"Marco"}



def run():
    store.get_categories()

if __name__ == '__main__':
    run()