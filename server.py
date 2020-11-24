import socket as s


class Dictionary:
    def __init__(self):
        self.data = {
            "a": list(),
            "b": list(),
            "c": list(),
            "d": list(),
            "e": list(),
            "f": list(),
            "g": list(),
            "h": list(),
            "i": list(),
            "j": list(),
            "k": list(),
            "l": list(),
            "m": list(),
            "n": list(),
            "o": list(),
            "p": list(),
            "q": list(),
            "r": list(),
            "s": list(),
            "t": list(),
            "u": list(),
            "v": list(),
            "w": list(),
            "x": list(),
            "y": list(),
            "z": list(),
            "all": list()
        }

    def insert(self, char, word_inp):
        self.data[char].append(word_inp)

    def refer(self, char):
        return self.data[char]


dictionary = Dictionary()
f = open('words.txt', 'r')
while True:
    line = f.readline().replace('\n', '')
    if line:
        dictionary.insert(line[0], line)
        dictionary.insert("all", line)
    else:
        break

socket = s.socket(s.AF_INET, s.SOCK_STREAM)
socket.bind(('127.0.0.1', 80))
socket.listen()
client_open = False

while True:
    client, address = socket.accept()
    client_open = True
    print(f"Connected to {address}")

    while client_open:
        message = client.recv(1024).decode("utf-8")
        if message == "2":
            client_open = False
            break
        letters = set(message)
        if ' ' in letters:
            letters.remove(' ')

        size = 0
        word = client.recv(1024).decode("utf-8")
        if word == "2":
            client_open = False
            break
        word_set = set(word)

        maxima = 0
        max_word = ''
        for words in dictionary.refer("all"):
            S = set(words)
            if S.issubset(letters):
                if maxima < len(words):
                    maxima = len(words)
                    max_word = words

        if max_word == '':
            client.send(bytes('It is not possible to make a valid word!Hence this round won\'t be counted', 'utf-8'))
        else:
            if word in dictionary.refer(word[0]):
                if word_set.issubset(letters):
                    client.send(bytes(f"You scored {len(word)}/{len(max_word)}!"
                                      f"Longest word: {max_word}", 'utf-8'))
                else:
                    client.send(bytes(f"You scored 0/{len(max_word)}! "
                                      f"Subset check failed!Longest word: {max_word}", 'utf-8'))
            else:
                client.send(bytes(f'You scored 0/{len(max_word)}!Your word wasn\'t present in the dictionary!'
                                  f'Longest word: {max_word}', 'utf-8'))

        # client_open = False

    client.close()
