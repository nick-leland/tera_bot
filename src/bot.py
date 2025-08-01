import interception
import time
import math
import ctypes

global_ALT_KEY = True


def move_mouse_to(x, y):
    interception.move_to(x, y)

def move_circle(radius, speed):
    current_position = interception.mouse_position()
    for i in range(0, 360, speed):
        x = int(radius * math.cos(i))
        y = int(radius * math.sin(i))
        move_mouse_to(current_position[0] + x, current_position[1] + y)
        time.sleep(0.1)

if __name__ == "__main__":
    # interception.auto_capture_devices()
    # while True:
    #     interception.move_to(resolution[0] // 2, resolution[1] // 2)
    #     print(f"Moved to center: {resolution[0] // 2}, {resolution[1] // 2}")
    #     time.sleep(1)
    #     move_circle(100, 1)
    #     print("Moved in a circle")
    #     time.sleep(1)

    user32 = ctypes.windll.user32

    # Get foreground window handle
    hwnd = user32.GetForegroundWindow()

    while True:
        # Buffer for window text
        length = user32.GetWindowTextLengthW(hwnd)
        buffer = ctypes.create_unicode_buffer(length + 1)
        user32.GetWindowTextW(hwnd, buffer, length + 1)

        print(f"Active window title: {buffer.value}")
        time.sleep(1)

