import time
import threading
import numpy as np
from pynput import mouse


class MouseLogger:
    def __init__(self, save=True, interval=60) -> None:
        # Logs all the mouse clicks in 2D list format, where each element is a list of 4 elements: [time, x, y, Action]
        self.log = np.array([["Time", "X", "Y", "Action"]])

        with mouse.Listener(on_click=self.on_click, on_move=self.on_move, on_scroll=self.on_scroll) as listener:
            if(save):
                threading.Timer(interval, self.save).start()
            listener.join()
    
    def on_click(self, x, y, button, pressed):
        if pressed:
            button = str(button).replace("Button.", "")
            self.log = np.append(self.log, [[round(time.time()), x, y, button]], axis=0)
            # print("Mouse clicked at: " + str(x) + ", " + str(y))

        # Exits on right click
        # if(button == mouse.Button.right):
        #     print(self.log)
        #     print(self.log.shape)
        #     # with open("log.csv", "w") as f:
        #     #     np.savetxt(f, self.log, delimiter=",", fmt="%s")
        #     return False

    def on_move(self, x, y):
        self.log = np.append(self.log, [[round(time.time()), x, y, "MOVE"]], axis=0)

    def on_scroll(self, x, y, dx, dy):
        scroll = "Scroll_"
        if(dy > 0):
            scroll += "Up"
        elif(dy < 0):
            scroll += "Down"
        elif(dx > 0):
            scroll += "Right"
        elif(dx < 0):
            scroll += "Left"
        self.log = np.append(self.log, [[round(time.time()), x, y, scroll]], axis=0)

    def save(self):
        with open("mouse-click.csv", "w") as f:
            np.savetxt(f, self.log, delimiter=",", fmt="%s")