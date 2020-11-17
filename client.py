import socket as s
import random

socket = s.socket(s.AF_INET, s.SOCK_STREAM)
socket.connect(('127.0.0.1', 80))
letters = ''
vowels = 'eeeeeeeeeeeeaaaaaaaaaiiiiiiiiioooooooouuuu'
consonants = 'nnnnnnrrrrrrttttttllllssssddddgggbbccmmppffhhvvwwyykjxqz'
while letters == '':
    i = 0
    while i < 6:
        print('Vowel(0) or Consonant(1)?', end=' ')
        option = int(input())
        if option == 0:
            ind = random.randint(0, len(vowels)-1)
            letters += vowels[ind]
        else:
            ind = random.randint(0, len(consonants)-1)
            letters += consonants[ind]
        i += 1
    print(f"Letters: {letters}")
    socket.send(bytes(letters, "utf-8"))
    # pass1
    print("What's your word?", end=' ')
    word = input()
    socket.send(bytes(word, "utf-8"))
    # pass2
    message = socket.recv(1024).decode("utf-8")
    print(message)
