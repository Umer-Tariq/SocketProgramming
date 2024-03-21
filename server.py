import socket

s = socket.socket()
s.bind(('localhost', 9993))
s.listen(5)
c, addr = s.accept()
msg = 'Hello'
while True:
    c.send(bytes(msg, 'utf-8'))
    recv_msg = c.recv(1024).decode()
    if recv_msg == 'exit':
        break
    else:
        print(recv_msg)
        flag = input('Do you want to send another message?')
        if flag == 'no':
            c.send(bytes('exit', 'utf-8'))
            break
        else:
            msg = input('Enter your message: ')
c.close()
