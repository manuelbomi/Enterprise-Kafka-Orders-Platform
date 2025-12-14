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

-- Platform engineers

-- Backend developers learning Kafka correctly
