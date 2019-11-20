from settings import api_host, api_port
import uvicorn

if __name__ == '__main__':
    uvicorn.run("main:app", host=api_host, port=api_port, reload=True)
