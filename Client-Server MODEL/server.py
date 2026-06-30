import socket               # This is the module we are going to use to make our socket point
import threading            # This is the module we are going to use to run processes in parallel
                            # to avoid any delay of one process because of other



HEADER = 64                 # This is the lenght of the msg that will tell the size of the main incoming message
PORT = 8080
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = '!DISCONNECT'

# print(socket.gethostname())   # This command actually prints your hostname
# print(socket.gethostbyname(socket.gethostname()))       # This command actually prints your local IPV4 address

SERVER = socket.gethostbyname(socket.gethostname())
print(SERVER)

# Creating a socket to open us to other connections
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Here I have created a socket variable and passed the IPV4 format acceptance and TCP stream Protocol
# for accepting any data

# Binding the server with an address and a port
ADDR = (SERVER, PORT)
server.bind(ADDR)

def handle_client(conn, addr):
    print(f'[NEW CONNCECTION] {addr} connected')
    # print(conn)

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)                 #This is a blocking line of code which means the code will not move further until this code gets something
        
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)

            if msg == DISCONNECT_MESSAGE:
                connected = False   

            print(f"[{addr[0]} : {addr[1]}] | {msg}")
            conn.send("Msg Received".encode(FORMAT))
    
    conn.close()

def start():
    server.listen()
    print(f'[LISTENING] Server is listening on {ADDR}')
    while (True):
        conn, addr = server.accept()       #This is a blocking line of code which means the code will not move further until this code gets something
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f'[ACTIVE CONNECTIONS] {threading.active_count() - 1}')

print("[STARTING] The server is starting.....")
start()
