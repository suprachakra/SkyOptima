"""
alerting.py: Implements an alerting mechanism that triggers notifications based on system events.
This example simulates sending alerts via logging.
"""

import logging
import smtplib
from email.mime.text import MIMEText

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("Alerting")

def send_email_alert(subject: str, message: str, recipients: list):
    """Send an email alert.
    
    Args:
        subject (str): Email subject.
        message (str): Email body.
        recipients (list): List of recipient email addresses.
    """
    # NOTE: Replace with actual SMTP server configuration.
    smtp_server = "smtp.example.com"
    smtp_port = 587
    sender_email = "alert@skyoptima.com"
    sender_password = "password"  # Use secure method to manage passwords
    
    msg = MIMEText(message)
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = ", ".join(recipients)
    
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, recipients, msg.as_string())
        server.quit()
        logger.info("Alert email sent successfully.")
    except Exception as e:
        logger.error("Failed to send alert email: %s", e)

def check_and_alert(metric: float, threshold: float):
    """
    Check a performance metric and send an alert if it exceeds the threshold.
    
    Args:
        metric (float): The current value of the metric.
        threshold (float): The threshold value.
    """
    if metric > threshold:
        subject = "Alert: Performance Metric Exceeded"
        message = f"Metric value {metric} exceeds threshold {threshold}."
        send_email_alert(subject, message, ["ops@skyoptima.com"])
    else:
        logger.info("Metric is within acceptable range.")

if __name__ == "__main__":
    # Example: Check if a simulated response time exceeds 2 seconds
    simulated_response_time = 2.5  # seconds
    check_and_alert(simulated_response_time, 2.0)
