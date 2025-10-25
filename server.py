from socket import*
from time import sleep
server = socket(AF_INET, SOCK_STREAM)
server.bind(('localhost',12345))
server.setblocking(False)
server.listen(5)

clients = []
while True:
    try:
        connection,address = server.accept()
        print(f'Підключився клієнт {connection}')
        connection.setbloking(False)
        clients.append(connection)
    except:
        print("Ніхто не підключається")
    for client in clients:
        try:
            client.send('Ви онлайн на сервері!'.encode())
        except:
            print('Хтось відключився від сервера ')
            clients.remove(client)
    sleep(0.5)