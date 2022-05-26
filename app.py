# with fastapi create get method /image
import fastapi
from fastapi.responses import FileResponse

app = fastapi.FastAPI()

@app.get("/image/{malid}")
async def read_image(malid):
    return FileResponse(f"./imagedata/{malid}.png")