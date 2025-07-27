import pyautogui
import time


def move_cursor(x, y):
    pyautogui.moveRel(x, y, duration=0)
    print(pyautogui.position())
    time.sleep(0.05)


def check_cursor():
    base_position = pyautogui.position()
    pyautogui.moveRel(10, 0, duration=0)
    if pyautogui.position() != base_position:
        pyautogui.moveRel(-10, 0, duration=0)
        return True
    # pyautogui.moveRel(0, 10, duration=0)
    # if pyautogui.position() != base_position:
    #     pyautogui.moveRel(0, -10, duration=0)
    #     return True
    return False


if __name__ == "__main__":
    pyautogui.FAILSAFE = True
    while True:
        # print(pyautogui.position())
        # time.sleep(0.001)
        time.sleep(2)
        move_cursor(-10, 0)
        move_cursor(0, -10)
        move_cursor(10, 0)
        move_cursor(0, 10)
        move_cursor(-10, 0)
        move_cursor(0, -10)
        move_cursor(10, 0)
        move_cursor(0, 10)
