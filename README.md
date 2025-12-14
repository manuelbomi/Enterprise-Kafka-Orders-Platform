# Enterprise Kafka Orders Platform -- <sub>End-to-End Kafka Setup with Docker, KRaft, and Python (Confluent Kafka)</sub>

## Overview

##### This repository provides a minimal yet enterprise-grade Apache Kafka platform demonstrating how modern organizations build event-driven applications using:

- Apache Kafka (KRaft mode, no ZooKeeper)

- Docker & Docker Compose

- Python Producers and Consumers

- Confluent Kafka client (librdkafka)

##### The project simulates a real enterprise workload:

- Order events produced by an application and consumed by downstream services.

#### Despite using a single Kafka node, the configuration mirrors real production architecture and can be scaled horizontally with minimal changes.

--- 

## Why This Project Matters for Enterprise Applications

##### Modern enterprises rely on streaming platforms to:

- Decouple services (microservices architecture)

- Process events in real time

- Enable analytics, monitoring, and automation

- Guarantee durability and fault tolerance

<ins>This project demonstrates</ins>:

✔ Kafka broker + controller in KRaft mode

✔ Topic-based messaging for business events

✔ Reliable delivery using Confluent Kafka client

✔ Dockerized infrastructure for portability

✔ Production-style configs with minimal complexity

#### It is ideal for:

- Enterprise architects

- Data engineers

- Platform engineers

- Backend developers learning Kafka correctly

---

## Architecture (Single-Node KRaft)

```python
+---------------------+
|  Python Producer    |
|  (Orders Service)   |
+----------+----------+
           |
           v
+------------------------------+
|  Kafka Broker + Controller   |
|  (KRaft Mode, Docker)        |
|  Topic: orders               |
+------------------------------+
           |
           v
+---------------------+
|  Python Consumer    |
|  (Order Tracker)    |
+---------------------+


```

---

## Project Structure

```python
kafka_projects/
│
├── docker-compose.yaml        # Kafka (KRaft mode) Docker setup
│
├── producer.py                # Enterprise-style Kafka producer
├── consumer_orders.py         # Kafka consumer service
│
├── .venv/                     # Python virtual environment (local)
│
└── README.md                  # Project documentation

```

---

## Kafka Configuration Highlights

```python
KAFKA_NODE_ID: 1
KAFKA_PROCESS_ROLES: broker, controller
KAFKA_CONTROLLER_QUORUM_VOTERS: 1@kafka:9093
KAFKA_OFFSETS_TOPIC_REPLICATION_FACTOR: 1

```

### Why This Matters

- Uses KRaft mode (modern Kafka, no ZooKeeper)

- Mirrors production roles (broker + controller)

- Simplifies enterprise onboarding

- Can scale to multi-broker clusters later

---

## Prerequisites

- Docker Desktop (Windows 11 supported)

- Python 3.9+

- pip

- Git

---

## Setup Instructions
<ins>Clone the Repository</INS>

```python
git clone https://github.com/your-username/enterprise-kafka-orders-platform.git
cd enterprise-kafka-orders-platform
```


