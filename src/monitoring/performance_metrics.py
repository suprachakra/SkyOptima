"""
performance_metrics.py: Collects and calculates performance metrics for SkyOptima.
"""

import time
import logging
import psutil  # To monitor system performance

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("PerformanceMetrics")

def get_cpu_usage():
    """Return current CPU usage percentage."""
    return psutil.cpu_percent(interval=1)

def get_memory_usage():
    """Return current memory usage percentage."""
    return psutil.virtual_memory().percent

def measure_response_time(func, *args, **kwargs):
    """Measure execution time of a function.
    
    Returns:
        float: Elapsed time in seconds.
    """
    start = time.time()
    result = func(*args, **kwargs)
    end = time.time()
    elapsed = end - start
    return elapsed, result

if __name__ == "__main__":
    cpu = get_cpu_usage()
    memory = get_memory_usage()
    logger.info("Current CPU Usage: %.2f%%", cpu)
    logger.info("Current Memory Usage: %.2f%%", memory)
    
    # Example: Measure response time of a dummy function
    def dummy_function():
        time.sleep(1)
    elapsed, _ = measure_response_time(dummy_function)
    logger.info("Dummy function response time: %.2f seconds", elapsed)
