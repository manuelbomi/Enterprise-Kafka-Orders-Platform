import json
from confluent_kafka import Consumer

consumer_config = {
    "bootstrap.servers": "localhost:9092",
    "group.id": "order-tracker",
    "auto.offset.reset": "earliest"
}

consumer = Consumer(consumer_config)

consumer.subscribe(["orders"])

print("🟢 Kafka consumer is running and subscribed to orders topic")

try:
    while True:
        msg = consumer.poll(1.0)
        if msg is None:
            continue
        if msg.error():
            print(" Error, Topic or message not seen:", msg.error())
            continue

        value = msg.value().decode("utf-8")
        order = json.loads(value)
        print(f"📦 Received order. Thank you: {order['quantity']} x {order['item']} from {order['user']}")
except KeyboardInterrupt:
    print("\n Stopping consumer")

finally:
    consumer.close()