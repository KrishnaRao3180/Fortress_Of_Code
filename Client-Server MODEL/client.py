import socket

HEADER = 64                 # This is the lenght of the msg that will tell the size of the main incoming message
PORT = 8080
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = '!DISCONNECT'
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)          # Info about the port we wish to connect to

try:
    client.connect(ADDR)

    def send(msg):
        message = msg.encode(FORMAT)
        msg_length = len(message)
        send_length = str(msg_length).encode(FORMAT)
        send_length += b' ' * (HEADER - len(send_length))
        client.send(send_length)
        client.send(message)
        print(client.recv(2048).decode(FORMAT))

    send("Hello World")

except socket.error as e:
    print(f"Connection failed {e}")