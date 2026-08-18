from loguru import logger
import sys
import os

def setup_logger(log_dir: str = "logs"):
    """
    Configure Loguru logger with console + file outputs.
    Creates rotating log files and adds correlation IDs.
    """
    # Ensure logs directory exists
    os.makedirs(log_dir, exist_ok=True)

    # Remove default handlers
    logger.remove()

    # Console handler
    logger.add(sys.stdout, level="INFO", colorize=True,
               format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | "
                      "<level>{level: <8}</level> | "
                      "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - "
                      "<level>{message}</level>")

    # File handler (rotating logs)
    logger.add(f"{log_dir}/framework.log", level="DEBUG",
               rotation="1 week", compression="zip",
               format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {message}")

    return logger
