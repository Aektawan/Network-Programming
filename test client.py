import asyncio
import socketio

# Create a Socket.IO client instance
sio = socketio.AsyncClient()

@sio.event
async def connect():
    print('Successfully connected to the server')
    # Join a chat room
    await sio.emit('join_chat', {'name': 'Client1', 'room': 'room1'})

@sio.event
async def disconnect():
    print('Disconnected from the server')

@sio.event
async def my_response(data):
    print('Server response:', data)

@sio.event
async def get_message(data):
    print(f"Message from {data['from']}: {data['message']}")

async def main():
    # Connect to the server at localhost on port 8080
    await sio.connect('http://127.0.0.1:8080')
    
    # Wait for messages and interact with the server
    await sio.emit('send_chat_room', {'name': 'Client1', 'message': 'Hello, World!', 'room': 'room1'})
    
    # Keep the connection alive
    await sio.wait()

if __name__ == '__main__':
    asyncio.run(main())
