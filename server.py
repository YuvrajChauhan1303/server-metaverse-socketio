from flask import Flask, request
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*", async_mode="eventlet")  # eventlet for WebSocket support

@app.route('/')
def index():
    return "Flask-SocketIO Server Running on Render!"

# Handle ESP32 Data
@socketio.on('esp_data')
def handle_esp_data(data):
    print(f"ESP Data Received: {data}")
    socketio.emit('voltage_current_data', data, broadcast=True)

# Handle Unity Commands
@socketio.on('unity_command')
def handle_unity_command(data):
    print(f"Unity Command Received: {data}")
    socketio.emit('esp_command', data, broadcast=True)

if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=10000)  # Use Render's allowed port
