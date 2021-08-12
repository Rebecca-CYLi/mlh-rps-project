from flask_socketio import SocketIO


socketio = SocketIO(
    logger=True,
    engineio_logger=True,
    always_connect=True,
    cors_allowed_origins=["https://localhost", "http://localhost:5000"],
)
