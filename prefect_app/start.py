import subprocess, os

# Set required environment variables
os.environ["PREFECT_API_DATABASE_CONNECTION_URL"] = "sqlite+aiosqlite:///prefect.db"
os.environ["PREFECT_API_PORT"] = "4200"

print("🚀 Starting Prefect Server on 0.0.0.0:4200")
subprocess.run([
    "prefect", "server", "start",
    "--host", "0.0.0.0",  # THIS IS CRITICAL
    "--port", "4200"
])

