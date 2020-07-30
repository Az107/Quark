import os
import sys
from time import sleep

import threading
import window
import comunication
import DisplayActions
debugMode = True




def main():

    print("starting...",end='')
    state = True
    print("[" +  ("OK" if state else "ERROR" ) + "]")
    winThread.start()
    comunication.start()


winThread = threading.Thread(target=window.start)


if __name__ == '__main__':
    main()