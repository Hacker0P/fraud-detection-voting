import websockets
import asyncio

async def listen():
    url = "ws://127.0.0.1:8000/ws"  # WebSocket URL
    async with websockets.connect(url) as websocket:
        print("Connected to WebSocket server. Listening for real-time updates...")
        while True:
            message = await websocket.recv()
            print(f"New vote received: {message}")

# Run the WebSocket listener
asyncio.run(listen())
