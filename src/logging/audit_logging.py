"""
audit_logging.py: Implements detailed audit logging for SkyOptima.
All system events, data transformations, model updates, and API transactions are logged.
"""

import logging
from logging.handlers import RotatingFileHandler

# Configure a rotating file handler for audit logs
handler = RotatingFileHandler("logs/audit.log", maxBytes=5*1024*1024, backupCount=5)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

logger = logging.getLogger("AuditLogger")
logger.setLevel(logging.INFO)
logger.addHandler(handler)

def log_event(event: str, details: dict):
    """Log an event with details.
    
    Args:
        event (str): Event description.
        details (dict): Additional details to log.
    """
    logger.info("Event: %s | Details: %s", event, details)

if __name__ == "__main__":
    log_event("Data Ingestion Completed", {"rows": 1000, "source": "bookings.csv"})
