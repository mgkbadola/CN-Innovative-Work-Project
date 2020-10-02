#!/usr/bin/python3
import socket as s
import random
import re

socket = s.socket(s.AF_INET, s.SOCK_STREAM)
socket.bind((s.gethostname(), 1024))
socket.listen(5)
client_open = False

while True:
    client, address = socket.accept()
    client_open = True
    print(f"Connected to {address}")
    
    while client_open:
        message = client.recv(1024).decode("utf-8")
        letters = set(message)
        
        size = 0
        word = client.recv(1024).decode("utf-8")
        wordset = set(word)
        
        #implement dictionary checking
        isword = random.randint(0,1)
        if isword == 1:
            for value in letters:
                regex = re.search(f'[a-zA-Z]*{value}[a-zA-Z]*',word)
                if regex:
                    size += 1
        else:
            client.send(bytes('It is not a valid word','utf-8'))
        
        if size == len(wordset):
            client.send(bytes("x points to you, well done!",'utf-8'))
        else:
            client.send(bytes('Your word failed the regex check','utf-8'))

        client_open = False
    
    client.close()
