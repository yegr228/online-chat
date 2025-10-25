from socket import*
from threading import Thread
server = socket(AF_INET, SOCK_STREAM)
server.bind(('localhost',12345))
server.setblocking(False)


name=input("Enter your name: ")
server.send(f'{name} has joined the chat'.encode())

def send_messages():
    while True:
        message =input()
        if message.lower== 'exit':
            server.send(f'{name} has joined the chat'.encode())
            server.close()
            break
Thread(target=send_messages, daemon=True).start()
while True:
    try:    
        data=server.recv(1024)
        if data:
            print(data.decode())
    except BlockingIOError:
        pass
    