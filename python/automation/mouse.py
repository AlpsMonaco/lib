import pyautogui as a
import time


def get_position():
    return a.position()
    pass


if __name__ == "__main__":
    while True:
        print("\r                              ",end="",flush=False)
        print("\r{}".format(get_position()),end="",flush=False)
        time.sleep(0.3)
    pass
