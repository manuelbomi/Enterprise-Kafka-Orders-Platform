import json
import uuid

from confluent_kafka import Producer

producer_config = {
    "bootstrap.servers": "localhost:9092"
}

producer = Producer(producer_config)

def topic_delivery_report(err, msg):
    if err:
        print(f" ✓ ✅ Delivery to topic failed: {err}")
    else:
        print(f" ✓ ✅ Message delivered to topic {msg.value().decode("utf-8")}")
        print(f" ✓ ✅ Message delivered to {msg.topic()} : partition {msg.partition()} : at offset {msg.offset()}")

orders = {
    "order_id": str(uuid.uuid4()),
    "user": "Emm Oyekanlu",
    "item": "Ford f450",
    "quantity": 18
}

values = json.dumps(orders).encode("utf-8")

producer.produce(
    topic="orders",
    value=values,
    callback=topic_delivery_report
)

producer.flush()