📊 Application Health Monitoring Service

A containerized application health monitoring service that continuously tracks system resource usage (CPU, memory, disk), logs metrics, and runs reliably as a background service using Docker and Docker Compose.

This project demonstrates Linux system monitoring, Python automation, logging best practices, and containerized deployment.

🚀 Features

📈 CPU Usage Monitoring

🧠 Memory Usage Monitoring

💾 Disk Usage Monitoring

📝 Structured logging with log rotation

🔁 Automatic restart on failure (Docker restart policy)

📦 Fully containerized using Docker

📄 Single YAML-based deployment using Docker Compose

📂 Persistent logs stored on host system

🛠️ Tech Stack

Python 3

psutil – system metrics

Docker

Docker Compose

Linux

📂 Project Structure robot-health-monitor/ ├── monitor/ │ ├── cpu_monitor.py │ ├── memory_monitor.py │ └── disk_monitor.py ├── auto_fix/ │ └── cleanup_logs.py ├── logs/ ├── logger_config.py ├── main.py ├── Dockerfile ├── docker-compose.yml ├── requirements.txt └── README.md

⚙️ How It Works

Each monitor runs continuously in its own thread

Resource usage is logged at fixed intervals

Logs are rotated automatically to prevent disk exhaustion

The service runs as a container with restart policies for reliability

Logs are mounted as volumes so they persist across restarts

▶️ Running the Application 1️⃣ Build Docker Image docker build -t app-health-monitor:1.0 .

2️⃣ Start Service Using Docker Compose docker-compose up -d

3️⃣ Verify docker ps ls logs

You should see log files like:

cpu.log memory.log disk.log auto_fix.log

4️⃣ Stop Service docker-compose down

Logs will remain available on the host system.

📝 Logging Strategy

Uses rotating log files

Prevents uncontrolled log growth

Logs are separated by concern (CPU, memory, disk, auto-fix)

Logs persist even if the container restarts

🎯 Use Cases

Application health monitoring

Linux system monitoring

Learning Docker + Python automation

Base framework for reliability and observability tools

📌 Future Improvements

Identify top resource-consuming processes

Size-based log cleanup

Healthcheck integration

Alerting (email / webhook)

Metrics API endpoint

👤 Author

Dipendra Singh Chandel Learning-focused project showcasing system monitoring and containerized deployment.
