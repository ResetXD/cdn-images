import uvicorn
import os

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=os.environ['PORT'], log_level="info")
