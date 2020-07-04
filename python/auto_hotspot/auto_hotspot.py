import pyautogui as a
import time
import os
import sys


def call_notify():
    a.keyDown('winleft')
    a.keyDown('a')
    a.keyUp('winleft')
    a.keyUp('a')
    time.sleep(3)


def show_position():
    while True:
        print('\r',end='',flush=True)
        print('                    ',end='',flush=True)
        print('\r',end='',flush=True)
        x, y = a.position()
        print('x={},y={}'.format(x,y), end='',flush=True)
        time.sleep(0.1)


if __name__ == "__main__":
    show_position()
    pass
