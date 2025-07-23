import subprocess
import os

# Port and database
os.environ["PREFECT_API_PORT"] = "4200"
os.environ["PREFECT_SERVER_ALLOW_EPHEMERAL_MODE"] = "false"
os.environ["PREFECT_ORION_DATABASE_CONNECTION_URL"] = "sqlite+aiosqlite:///prefect.db"

print("🚀 Starting Prefect Server")
subprocess.run(["prefect", "server", "start"])

