import uvicorn
from prefect.server.api.server import app

if __name__ == "__main__":
    print("🔌 Launching Prefect API server on 0.0.0.0:4200")
    uvicorn.run(app, host="0.0.0.0", port=4200)

