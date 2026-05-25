# CRYPTEX 🚀
### High-Performance Cryptocurrency Matching Engine

<p align="center">
  <img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExaXUyY2g1dDV4eGV4OW1tY3J5cG9qZTB5bHFlODd6MmZ2MnRrOGNlYiZlcD12MV9naWZzX3NlYXJjaCZjdD1n/l0HlBO7eyXzSZkJri/giphy.gif" width="700"/>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.12-blue?style=for-the-badge&logo=python"/>
  <img src="https://img.shields.io/badge/FastAPI-Backend-green?style=for-the-badge&logo=fastapi"/>
  <img src="https://img.shields.io/badge/WebSocket-Realtime-orange?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Performance-111K%2B_orders/sec-red?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Architecture-Low_Latency-black?style=for-the-badge"/>
</p>

---

# 📌 Overview

CRYPTEX is a high-performance cryptocurrency matching engine built using **Python, FastAPI, asyncio, and WebSockets**.

The project simulates the core infrastructure of modern electronic trading systems by implementing:

- ⚡ Real-time order matching
- 📈 Level-2 Order Books
- 🔄 WebSocket Market Data Streaming
- 💹 Best Bid & Offer (BBO)
- 🧠 FIFO Price-Time Priority
- 📊 Trade Execution Reporting
- 🛡️ Decimal Precision Financial Calculations

Designed using **REG NMS-inspired principles**, CRYPTEX focuses on scalability, reliability, low-latency execution, and real-time distributed market infrastructure.

---

# ✨ Features

## ⚡ Matching Engine
- FIFO Price-Time Priority Matching
- High-throughput order execution
- Multi-symbol trading support
- Low latency execution engine

## 📈 Market Data Infrastructure
- Real-time trade dissemination
- Level-2 Order Book streaming
- Best Bid & Offer (BBO)
- WebSocket broadcasting

## 🔥 Supported Order Types
- Market Orders
- Limit Orders
- IOC (Immediate-Or-Cancel)
- FOK (Fill-Or-Kill)
- Stop Loss Orders
- Stop Limit Orders
- Take Profit Orders

## 🌐 APIs
- REST APIs
- WebSocket APIs
- Async event broadcasting

## 🧪 Testing & Benchmarking
- Unit testing suite
- Async testing support
- Performance benchmarking tools

---

# 🏗️ Project Architecture

```bash
cryptex/
├── main.py
├── requirements.txt
├── dashboard.html
│
├── engine/
│   ├── models.py
│   ├── order_book.py
│   ├── matching_engine.py
│   ├── manager.py
│   ├── fees.py
│   └── persistence.py
│
├── api/
│   └── server.py
│
├── tests/
│   └── test_matching_engine.py
│
└── benchmarks/
    └── benchmark.py
```

---

# ⚙️ Tech Stack

## 🔹 Backend
- Python 3.12
- FastAPI
- asyncio
- WebSockets

## 🔹 Data Structures
- SortedContainers
- deque
- Decimal Precision Arithmetic

## 🔹 Testing
- Pytest
- Async Testing
- Benchmark Suite

---

# 🚀 Performance Benchmarks

| Benchmark | Result |
|---|---|
| ⚡ Order Throughput | 111K+ orders/sec |
| 📈 Trade Matching | 41K+ matches/sec |
| ⏱️ P99 Latency | < 55µs |
| 📊 Depth Snapshot | 85K+ reads/sec |

---

# 📡 REST API Endpoints

## Submit Order

```http
POST /api/orders
```

## Cancel Order

```http
DELETE /api/orders/{order_id}
```

## Get Order Book Depth

```http
GET /api/depth/{symbol}
```

## Get Best Bid & Offer

```http
GET /api/bbo/{symbol}
```

---

# 🔌 WebSocket APIs

| Endpoint | Description |
|---|---|
| `/ws/trades/{symbol}` | Live trade execution stream |
| `/ws/bbo/{symbol}` | Real-time BBO updates |
| `/ws/depth/{symbol}` | Full Level-2 order book |

---

# ▶️ Quick Start

## 1️⃣ Clone Repository

```bash
git clone https://github.com/Adarshmishra87/cryptex.git
cd cryptex
```

---

## 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 3️⃣ Start Server

```bash
python main.py
```

---

## 4️⃣ Open Dashboard

```bash
http://localhost:8000/dashboard
```

---

## 5️⃣ Swagger Documentation

```bash
http://localhost:8000/docs
```

---

# 🧪 Run Tests

```bash
python main.py --test
```

---

# 📊 Run Benchmarks

```bash
python main.py --benchmark
```

---

# 💡 Core Concepts Implemented

- Matching Engine Architecture
- Price-Time Priority
- REG NMS Inspired Matching
- Distributed Systems
- Real-Time APIs
- WebSocket Broadcasting
- Financial Precision Handling
- Async Programming
- Backend System Design
- Market Data Dissemination
- Low-Latency Infrastructure

---

# 📚 Learning Outcomes

This project was built to gain practical experience with:

- Exchange Infrastructure
- Distributed Trading Systems
- Financial Market Microstructure
- High-Performance Python Systems
- Backend Engineering
- Async Architectures
- Real-Time Data Streaming
- Scalable API Design

---

# 🖥️ Demo Preview

<p align="center">
  <img src="https://media.giphy.com/media/coxQHKASG60HrHtvkt/giphy.gif" width="700"/>
</p>

---

# 🏷️ GitHub Topics

`python` `fastapi` `websocket` `cryptocurrency`
`matching-engine` `trading-system`
`backend` `system-design`
`low-latency` `distributed-systems`
`asyncio` `fintech`
`exchange-engine` `market-data`
`orderbook` `realtime`

---

# 👨‍💻 Author

## Adarsh Mishra
Backend & Systems Engineering Enthusiast

<p align="center">
  <img src="https://media.giphy.com/media/f3iwJFOVOwuy7K6FFw/giphy.gif" width="500"/>
</p>

---

# ⭐ If you like this project

Give it a ⭐ on GitHub and support the project.
