from pathlib import Path
from logger_config import setup_logger

logger = setup_logger("AUTO_FIX", 'auto_fix.log')

def cleanup_old_logs(max_log_files=5):
    """
    Keeps only latest N log files, deletes older ones
    """
    log_dir=Path(__file__).resolve().parent.parent / "logs"

    log_files=sorted(
        log_dir.glob("*.log"),
        key=lambda f: f.stat().st_mtime
    )

    if len(log_files) <= max_log_files:
        logger.info("No log clean up needed.")
        return
    
    files_to_delete = log_files[:-max_log_files]

    for log_files in files_to_delete:
        try:
            log_files.unlink()
            logger.warning(f"Deleted old log file: {log_file.name}")
        
        except Exception as e:
            logger.error(f"Failed to delete {log_file.name}: {e}")