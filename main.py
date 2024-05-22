from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import aiofiles
import uvicorn

app = FastAPI()

app.mount("/static", StaticFiles(directory="public"), name="static")

@app.get("/", response_class=HTMLResponse)
async def read_index():
    async with aiofiles.open("public/index.html", mode="r") as file:
        content = await file.read()
        print(content)
    return HTMLResponse(content=content)

if __name__ == '__main__':
    uvicorn.run(app, host="localhost", port=8080)