"""
Crypto Matching Engine — Main Entry Point

Usage:
    python main.py                 # Start server on port 8000
    python main.py --port 8080     # Custom port
    python main.py --benchmark     # Run benchmarks
    python main.py --test          # Run unit tests
"""

import argparse
import logging
import sys
import os

# Add project root to path so all packages resolve correctly
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)-8s %(name)s: %(message)s",
    datefmt="%H:%M:%S",
)
logging.getLogger("uvicorn.access").setLevel(logging.WARNING)


def run_server(host: str = "0.0.0.0", port: int = 8000):
    import uvicorn
    from api.server import app
    uvicorn.run(app, host=host, port=port, log_level="warning")


def run_benchmarks():
    from benchmarks.benchmark import (
        bench_add_orders, bench_matching, bench_market_sweep,
        bench_concurrent_symbols, bench_depth_snapshot,
    )
    print("\n🚀 MATCHING ENGINE PERFORMANCE BENCHMARKS")
    bench_add_orders(10_000)
    bench_matching(5_000)
    bench_market_sweep(50)
    bench_concurrent_symbols(10, 1000)
    bench_depth_snapshot(10_000)


def run_tests():
    import pytest
    sys.exit(pytest.main(["-v", "tests/"]))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Crypto Matching Engine")
    parser.add_argument("--host", default="0.0.0.0")
    parser.add_argument("--port", type=int, default=8000)
    parser.add_argument("--benchmark", action="store_true")
    parser.add_argument("--test", action="store_true")
    args = parser.parse_args()

    if args.benchmark:
        run_benchmarks()
    elif args.test:
        run_tests()
    else:
        print(f"🚀 Starting Crypto Matching Engine on {args.host}:{args.port}")
        print(f"   API docs:  http://localhost:{args.port}/docs")
        print(f"   Dashboard: http://localhost:{args.port}/dashboard")
        print(f"   WS trades: ws://localhost:{args.port}/ws/trades/BTC-USDT")
        run_server(args.host, args.port)
