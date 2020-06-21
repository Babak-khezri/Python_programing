from os import system
from random import choice
from threading import Thread
from click import getchar
from time import sleep
system('mode con:cols=75 lines=10')


def change_color():
    while True:
        sleep(0.5)
        colors_list = ['00', '01', '02', '03', '04', '05', '06',
                       '07', '08', '09', 'A', 'B', 'C', 'D', 'E', 'F']
        color = choice(colors_list)
        system("color {}".format(color))


def back_space(sentence):
    if sentence == '':
        return sentence
    sentence = list(sentence)
    sentence.pop(-1)
    return "".join(sentence)


def Enter(Sentence):
    return Sentence + '\n'


def typer():
    Sentence = ''
    while True:
        key = getchar()
        if ord(key) == ord('\b'):
            Sentence = back_space(Sentence)
        elif ord(key) == ord('\n') or ord(key) == 13:
            Sentence = Enter(Sentence)
        else:
            Sentence += key
        system('cls')
        print(Sentence)


Thread(target=change_color).start()
typer()
