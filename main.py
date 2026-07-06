from fastapi import FastAPI
import socket

app = FastAPI()

@app.get("/")
def read_root():
    # 返回主机名，方便我们验证是不是新容器在运行
    hostname = socket.gethostname()
    return {"message": "Hello CI/CD!", "server_hostname": hostname, "version": "v1.0"}
