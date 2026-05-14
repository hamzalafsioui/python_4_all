"""
PROJECT: The High-Performance Stock Ticker (Simulator)

Goal: Simulate a real-time system that fetches stock prices for multiple companies concurrently.

Requirements:

1. The Coroutine 'fetch_stock_price(ticker)':
   - Prints "Fetching price for [ticker]..."
   - Awaits 'asyncio.sleep(1)' to simulate a network request.
   - Returns a random price (e.g., round(random.uniform(100, 500), 2)).

2. The Main Task:
   - Create a list of 10 tickers: ["AAPL", "GOOGL", "MSFT", "AMZN", "TSLA", "META", "NVDA", "NFLX", "ADBE", "PYPL"].
   - Use 'asyncio.gather' to fetch all 10 prices at once.
   - Time the execution. It MUST take approximately 1 second in total.

3. Output:
   - Print the final list of fetched prices.
   - Print the total execution time.

Real-World Logic:
- This is how modern trading platforms and dashboards work. They don't refresh one widget at a time; they fire off dozens of async requests and update the whole screen as soon as the data arrives.
"""

import asyncio
import time
import random

# TODO: Implement the Stock Ticker Simulator

async def fetch_stock_price(ticker):
    print(f"Fetching price for {ticker}...")
    await asyncio.sleep(1)
    return round(random.uniform(100, 500), 2)

async def main():
    start_time = time.perf_counter()
    tickers = ["AAPL", "GOOGL", "MSFT", "AMZN", "TSLA", "META", "NVDA", "NFLX", "ADBE", "PYPL"]
    prices = await asyncio.gather(*[fetch_stock_price(ticker) for ticker in tickers])
    print(f"Prices: {prices}")
    end_time = time.perf_counter()
    print(f"Total time taken: {end_time - start_time:.2f} seconds")

if __name__ == "__main__":
    asyncio.run(main())
