import Modules.KeyStroke as KeyStroke
import Modules.MouseRecorder as MouseRecorder

if __name__ == '__main__':
    try:
        print("Started KeyStroke Logger")
        KeyStroke.KeyLogger()
        # print("Started Mouse Logger")
        # MouseRecorder.MouseLogger()
    except KeyboardInterrupt as e:
        pass