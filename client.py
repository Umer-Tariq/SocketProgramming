import socket

s = socket.socket()
s.connect(('localhost', 9993))
while True:
    recv_msg = s.recv(1024).decode()
    if recv_msg == 'exit':
        break
    else:
        print(recv_msg)
        flag = input('Do you want to send a message: ')
        if flag == 'no':
            s.send(bytes('exit', 'utf-8'))
            break
        else:
            msg = input('Enter your message: ')
            s.send(bytes(msg, 'utf-8'))
s.close()