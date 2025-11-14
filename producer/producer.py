#!/usr/bin/env python3
# producer.py

from kafka import KafkaProducer
from kafka.errors import KafkaError
import csv
import os
import sys
import json 

KAFKA_BROKER = os.getenv('KAFKA_BROKER', 'kafka:9092')
KAFKA_TOPIC = os.getenv('KAFKA_TOPIC', 'customer')

# Kafka Producer configuration
producer = KafkaProducer(
    bootstrap_servers=[KAFKA_BROKER],
    value_serializer=lambda m: json.dumps(m).encode('utf-8')
)


def produce_events(file_path, flush_interval=10000):
    with open(file_path, mode='r') as file:
        reader = csv.DictReader(file)
        count = 0
        topic = KAFKA_TOPIC

        for row in reader:
            message = row

            # Asynchronously send a message
            future = producer.send(topic, value=message)
            count += 1

            try:
                # Block for 'synchronous' sends
                record_metadata = future.get(timeout=1)
                print(record_metadata.topic)
                print(record_metadata.partition)
                print(record_metadata.offset)
                print()
            except KafkaError:
                # Decide what to do if produce request failed...
                print('Message delivery failed.')

            # Flush every N messages
            if count % flush_interval == 0:
                producer.flush()
                print(f"Flushed {count} messages")

    # Final flush to ensure everything is sent
    producer.flush()
    print(f"Finished sending {count} messages")


if __name__ == "__main__":
    file_path = 'customers-1000000.csv'
    produce_events(file_path, flush_interval=10000)
