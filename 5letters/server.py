import socket

#Создается сокет с помощью функции
#протокол TCP используется для создания сервера, который может принимать соединения от клиентов.
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#Сокету назначается адрес с помощью функции
sock.bind(('', 40000))
#Сокету устанавливается режим прослушивания с помощью функции sock.listen(2). Это означает, что сокет будет ожидать подключений от двух клиентов.
sock.listen(2)
#Сервер ожидает подключение от первого клиента с помощью функции sock.accept(),
#которая возвращает кортеж из двух элементов: соединения (conn1) и адреса (addr1) клиента.
conn1, addr1 = sock.accept()
conn2, addr2 = sock.accept()
words = []

with open('data/words.txt', 'r', encoding='utf-8') as file:
    line = file.read().split()
    for i in line:
        words.append(i)


def check(word):
    global words
    if word not in words:
        return '2'
    else:
        return '1'


conn1.send('1'.encode('utf-8'))
conn2.send('2'.encode('utf-8'))

#С помощью метода recv() клиент 1 (conn1) получает слово, которое он хочет угадать.
#Сервер вызывает функцию check(input_word) для проверки предположения клиента 2. Результат проверки отправляется клиенту 2 с помощью метода send().
while True:
    word = conn1.recv(1024).decode('utf-8')
    conn1.send(check(word).encode('utf-8'))
    if check(word) == '1':
        conn2.send(word.encode('utf-8'))
        while True:
            input_word = conn2.recv(1024).decode('utf-8')
            conn2.send(check(input_word).encode('utf-8'))
