import random
import re
import socket as s

import pygame

socket = s.socket(s.AF_INET, s.SOCK_STREAM)
socket.connect(('127.0.0.1', 80))
letters = ''
word = ''
message = ''
vowels = 'eeeeeeeeeeeeaaaaaaaaaiiiiiiiiioooooooouuuu'
consonants = 'nnnnnnrrrrrrttttttllllssssddddgggbbccmmppffhhvvwwyykjxqz'
my_score = 0
total_score = 0
i = 0
v = 0

# initialisation of game
pygame.init()

res = (800, 600)
screen = pygame.display.set_mode(res)

# background, title, icon
background = pygame.image.load("bg.jpeg")
pygame.display.set_caption("Guess The Longest Word!")
icon = pygame.image.load("icon.png")
pygame.display.set_icon(icon)

game_state = "ready"

# other text
heading = pygame.font.Font('freesansbold.ttf', 50)
subheading = pygame.font.Font('freesansbold.ttf', 32)
titleX = 70
titleY = 150


def score_update(msg):
    global my_score
    global total_score
    if '/' in msg:
        scores = re.findall(r'\d{1,2}/\d{1,2}', msg)[0]
        scores = scores.split('/')
        my_score += int(scores[0])
        total_score += int(scores[1])


def title(x, y):
    name = heading.render("Guess The Longest Word!", True, (0, 0, 0))
    start = subheading.render("Press Enter to Play", True, (0, 0, 0))
    screen.blit(name, (x, y))
    screen.blit(start, (x + 170, y + 150))


def display_letters(x, y, w):
    input_letters = heading.render("Your letters : " + str(w), True, (0, 0, 0))
    screen.blit(input_letters, (x, y))


def ask(x, y):
    ques = subheading.render("Vowel(0) or Consonant(1)?", True, (0, 0, 0))
    screen.blit(ques, (x, y))


def display_word(x, y, w):
    input_word = subheading.render("Your word : " + str(w), True, (0, 0, 0))
    screen.blit(input_word, (x, y))


def display_score():
    score = subheading.render(f"SCORE : {str(my_score)}/{str(total_score)}", True, (0, 0, 0))
    screen.blit(score, (0, 0))


def final(w):
    w = w.split('!')
    y = 150
    for line in w:
        result1 = subheading.render(line, True, (0, 0, 0))
        screen.blit(result1, (70, y))
        y += 40

    start = subheading.render("Press Enter to Replay", True, (0, 0, 0))
    screen.blit(start, (220, y + 40))


# game loop
running = True
while running:
    screen.fill((255, 255, 255))  # RGB
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            socket.send(bytes("2", "utf-8"))
            running = False

        # detecting keystrokes
        if event.type == pygame.KEYDOWN:
            if game_state == "ready":
                # start choosing
                if event.key == pygame.K_RETURN:
                    game_state = "choosing"

            elif game_state == "choosing":
                if event.key == pygame.K_0:
                    ind = random.randint(0, len(vowels) - 1)
                    while vowels[ind] in letters:
                        ind = random.randint(0, len(vowels) - 1)
                    letters += vowels[ind] + " "
                elif event.key == pygame.K_1:
                    ind = random.randint(0, len(consonants) - 1)
                    while consonants[ind] in letters:
                        ind = random.randint(0, len(consonants) - 1)
                    letters += consonants[ind] + " "

            elif game_state == "waiting":
                if event.key == pygame.K_a:
                    word += 'a'
                elif event.key == pygame.K_b:
                    word += 'b'
                elif event.key == pygame.K_c:
                    word += 'c'
                elif event.key == pygame.K_d:
                    word += 'd'
                elif event.key == pygame.K_e:
                    word += 'e'
                elif event.key == pygame.K_f:
                    word += 'f'
                elif event.key == pygame.K_g:
                    word += 'g'
                elif event.key == pygame.K_h:
                    word += 'h'
                elif event.key == pygame.K_i:
                    word += 'i'
                elif event.key == pygame.K_j:
                    word += 'j'
                elif event.key == pygame.K_k:
                    word += 'k'
                elif event.key == pygame.K_l:
                    word += 'l'
                elif event.key == pygame.K_m:
                    word += 'm'
                elif event.key == pygame.K_n:
                    word += 'n'
                elif event.key == pygame.K_o:
                    word += 'o'
                elif event.key == pygame.K_p:
                    word += 'p'
                elif event.key == pygame.K_q:
                    word += 'q'
                elif event.key == pygame.K_r:
                    word += 'r'
                elif event.key == pygame.K_s:
                    word += 's'
                elif event.key == pygame.K_t:
                    word += 't'
                elif event.key == pygame.K_u:
                    word += 'u'
                elif event.key == pygame.K_v:
                    word += 'v'
                elif event.key == pygame.K_w:
                    word += 'w'
                elif event.key == pygame.K_x:
                    word += 'x'
                elif event.key == pygame.K_y:
                    word += 'y'
                elif event.key == pygame.K_z:
                    word += 'z'
                elif event.key == pygame.K_BACKSPACE:
                    x = len(word) - 1
                    temp = word[:x]
                    word = temp
                elif event.key == pygame.K_RETURN:
                    if not word:
                        word = "dummystring"
                    game_state = "result"
            elif game_state == "finished":
                if event.key == pygame.K_RETURN:
                    game_state = "choosing"

    if game_state == "ready":
        title(titleX, titleY)

    elif game_state == "choosing":
        display_score()
        display_letters(titleX, titleY, letters)

        if len(letters) < 10:
            ask(titleX, titleY + 150)
        elif len(letters) >= 10:
            game_state = "waiting"
            socket.send(bytes(letters, "utf-8"))

    elif game_state == "waiting":
        display_score()
        display_letters(titleX, titleY, letters)
        display_word(titleX, titleY + 150, word)

    elif game_state == "result":
        display_score()
        socket.send(bytes(word, "utf-8"))
        message = socket.recv(1024).decode("utf-8")
        score_update(message)
        print(message)
        final(message)
        letters = ""
        word = ""
        game_state = "finished"

    elif game_state == "finished":
        display_score()
        final(message)

    pygame.display.update()
