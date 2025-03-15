"""
stream_data.py: Implements a simple Kafka consumer to stream data in real time.
This module is designed to ingest data continuously from Kafka topics.
"""

import json
import logging
from kafka import KafkaConsumer

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("StreamData")

def stream_from_kafka(topic: str, bootstrap_servers: list):
    """Consume messages from a Kafka topic and process them.
    
    Args:
        topic (str): Kafka topic name.
        bootstrap_servers (list): List of Kafka server addresses.
    """
    consumer = KafkaConsumer(
        topic,
        bootstrap_servers=bootstrap_servers,
        auto_offset_reset='earliest',
        enable_auto_commit=True,
        group_id='skyoptima-group',
        value_deserializer=lambda x: json.loads(x.decode('utf-8'))
    )
    
    logger.info("Started consuming from topic %s", topic)
    try:
        for message in consumer:
            data = message.value
            logger.info("Received message: %s", data)
            # Process the message (e.g., store to database or pass to processing pipeline)
    except Exception as e:
        logger.error("Error while consuming Kafka messages: %s", e)
    finally:
        consumer.close()

if __name__ == "__main__":
    stream_from_kafka("skyoptima_topic", ["localhost:9092"])
