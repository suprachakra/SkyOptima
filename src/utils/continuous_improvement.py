"""
Automates feedback collection and anomaly detection,
triggering change management actions in response to system performance issues.
"""

import time
import logging
import psutil

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("ContinuousImprovement")

def collect_system_metrics() -> dict:
    """Collect and return system metrics."""
    metrics = {
        "cpu_usage": psutil.cpu_percent(interval=1),
        "memory_usage": psutil.virtual_memory().percent,
        "disk_io": psutil.disk_io_counters().read_bytes
    }
    logger.info("Collected system metrics: %s", metrics)
    return metrics

def detect_anomalies(metrics: dict, thresholds: dict) -> dict:
    """Detect anomalies if any metric exceeds its threshold."""
    anomalies = {}
    for metric, value in metrics.items():
        if value > thresholds.get(metric, float('inf')):
            anomalies[metric] = value
    if anomalies:
        logger.warning("Anomalies detected: %s", anomalies)
    return anomalies

def trigger_change_management(anomalies: dict):
    """Trigger a change management process if anomalies are detected."""
    if anomalies:
        logger.info("Triggering Change Management process due to anomalies: %s", anomalies)
        print("Change Management Triggered: Review anomalies and initiate sprint retrospective.")
    else:
        logger.info("No anomalies detected. System operating within thresholds.")

if __name__ == "__main__":
    thresholds = {
        "cpu_usage": 80.0,
        "memory_usage": 85.0,
        "disk_io": 1e9
    }
    metrics = collect_system_metrics()
    anomalies = detect_anomalies(metrics, thresholds)
    trigger_change_management(anomalies)
