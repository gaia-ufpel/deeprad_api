import uvicorn
from fastapi import FastAPI

from utils import HOST, PORT

app = FastAPI()

if __name__ == "__main__":
    uvicorn.run(app, host=HOST, port=PORT, reload=True)