import time
import os
from playsound import playsound

def count(t):
    print()
    while t>0:
        print(f'\r{t}', end='')
        t-=1
        time.sleep(1)
        print('               ', end='')
    print("\n\nTime's Up!")
    playsound('./commands/Ping1.wav')

