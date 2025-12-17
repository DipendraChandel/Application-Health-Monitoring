# Health Monitor

A comprehensive health monitoring system for robotic applications that tracks system resources, sensor status, and provides automated maintenance capabilities.

## Features

### System Monitoring

- **CPU Monitoring**: Tracks CPU usage with configurable thresholds and alerts
- **Memory Monitoring**: Monitors RAM usage and detects memory pressure
- **Disk Monitoring**: Monitors disk space and I/O operations
- **Network Monitoring**: Tracks network interface statistics and connectivity

### Sensor Simulation

- **Camera Simulator**: Simulates camera sensor operations and health checks
- **GPS Simulator**: Simulates GPS positioning and signal quality monitoring

### Automated Maintenance

- **Log Cleanup**: Automated log rotation and cleanup utilities
- **Service Restart**: Automated service restart capabilities for fault recovery

### Logging & Configuration

- Centralized logging configuration with rotating file handlers
- Structured logging with different log levels and categories
- Configurable monitoring thresholds and intervals

## Project Structure

```
health-monitor/
├── main.py                 # Main application entry point
├── logger_config.py        # Logging configuration
├── requirements.txt        # Python dependencies
├── Dockerfile             # Docker container configuration
├── docker-compose.yml     # Docker Compose deployment
├── monitor/               # System monitoring modules
│   ├── cpu_monitor.py
│   ├── memory_monitor.py
│   ├── disk_monitor.py
│   └── network_monitor.py
├── sensors/               # Sensor simulation modules
│   ├── camera_simulator.py
│   └── gps_simulator.py
├── auto_fix/              # Automated maintenance scripts
│   ├── cleanup_log.py
│   ├── cleanup_logs
│   └── restart_service.py
└── logs/                  # Application logs directory
```

## Installation

### Prerequisites

- Python 3.8 or higher
- Docker and Docker Compose (for containerized deployment)

### Local Installation

1. Clone the repository:

```bash
git clone https://github.com/DipendraChandel/Application-Health-Monitoring.git
cd Application-Health-Monitoring
```

2. Create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

### Running Locally

Start the health monitoring system:

```bash
python main.py
```

The application will start monitoring system resources and log to the `logs/` directory.

### Docker Deployment

1. Build the Docker image:

```bash
docker-compose build
```

2. Start the service:

```bash
docker-compose up -d
```

3. View logs:

```bash
docker-compose logs -f
```

4. Stop the service:

```bash
docker-compose down
```

## Configuration

### Monitoring Thresholds

Modify the threshold values in the respective monitor files:

- `CPU_THRESHOLD` in `monitor/cpu_monitor.py`
- `MEMORY_THRESHOLD` in `monitor/memory_monitor.py`
- `DISK_THRESHOLD` in `monitor/disk_monitor.py`

### Logging Configuration

Adjust logging settings in `logger_config.py`:

- Log levels
- File rotation policies
- Log format

## Automated Maintenance

### Log Cleanup

Run the log cleanup script:

```bash
python auto_fix/cleanup_log.py
```

### Service Restart

Execute the service restart utility:

```bash
python auto_fix/restart_service.py
```

## Development

### Adding New Monitors

1. Create a new monitor file in the `monitor/` directory
2. Implement the monitoring function following the pattern:

```python
def monitor_[resource](stop_event):
    while not stop_event.is_set():
        # Monitoring logic
        # Logging
        time.sleep(interval)
```

3. Import and add the monitor thread in `main.py`

### Adding New Sensors

1. Create sensor simulator in the `sensors/` directory
2. Implement sensor health checks and data simulation
3. Integrate with the main monitoring loop if needed

## Dependencies

- `psutil==7.1.3`: System and process utilities for monitoring

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For issues and questions, please open an issue on the GitHub repository.
