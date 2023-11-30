from fastapi import FastAPI
import time
import hashlib

app = FastAPI()

def consume_memory():
    # Consumes approximately 200MB of RAM
    n = 50 * 1024 * 1024  # Number of characters (assuming each character is 4 bytes)
    large_string = ' ' * n
    return large_string

def consume_cpu():
    # CPU-intensive task
    for _ in range(1000000):
        hashlib.sha256(b'some random bytes').hexdigest()
@app.get("/")
async def read_root():
    consume_cpu()
    _ = consume_memory()
    # Simulate a delay
    time.sleep(0.3)  # 300 milliseconds
    return {"message": "OK"}
