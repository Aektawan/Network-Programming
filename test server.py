import asyncio
from aiohttp import web
import socketio
from json import dumps

# Configure the connection timeout and ping interval
sio = socketio.AsyncServer(
    async_mode='aiohttp',
    ping_interval=25,  # Interval in seconds at which the server pings the client
    ping_timeout=120,  # Time in seconds before a connection is considered lost if no ping response is received
    max_http_buffer_size=10_000_000,  # Maximum buffer size for incoming HTTP data
)

app = web.Application()
sio.attach(app)

@sio.event
async def join_chat(sid, message):
    print(message.get('name', sid) + ' joined to {}'.format(message['room']))
    await sio.enter_room(sid, message['room'])

@sio.event
async def exit_chat(sid, message):
    await sio.leave_room(sid, message['room'])

@sio.event
async def send_chat_room(sid, message):
    await sio.emit('get_message', {'message': message['message'], 'from': message['name']}, room=message['room'])

@sio.event
async def connect(sid, environ):
    await sio.emit('my_response', {'data': 'Connected', 'count': 0}, room=sid)

@sio.event
def disconnect(sid):
    print('Client disconnected')

if __name__ == '__main__':
    # Run the server on localhost (127.0.0.1) at port 8080
    web.run_app(app, host='127.0.0.1', port=8080)
