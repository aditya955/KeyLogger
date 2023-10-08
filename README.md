# KeyLogger
A Simple KeyLogger made in python. It can perform various operations while running in the background.

## Functions Available
- Mail
- KeyLogger
- Mouse Clicks
- Mouse Position
- POST data to server
- Get System Information

## Installation
### 1. Clone this repository
```bash
git clone https://github.com/aditya955/KeyLogger.git
cd KeyLogger
```

### 2. Install the requirements
```bash
pip install -r requirements.txt
```

*Note:* Some distributions of Linux may require you to use their own package manager like `apt` for debian based distributions and `pacman` for arch based distributions to install the requirements.
Example:
```bash
sudo apt install python3-requests
sudo pacman -S python-requests
```

## Configuration
Configure `config.json` to your needs.

### 1. Keystrokes
To log the keystrokes.

`save`: Whether to save the keystrokes to a file or not. (Default = True)

`interval`: The interval in seconds after which the keystrokes are saved to the file. (Default = 60 ie. 1 minute)


### 2. Mail
To send the logs to your mail.

`email`: This is the email address from which you want to send the logs. (The email is sent to itself)

`password`: This is the password of the email address from which you want to send the logs.

`host`: This is the SMTP host of the email address from which you want to send the logs. (Default = Google SMTP)

`port`: This is the SMTP port of the email address from which you want to send the logs. (Default = 465)


### 3. Mouse
To log the mouse clicks, scrolls and position.

`save`: Whether to save the Mouse Records to a file or not. (Default = True)

`interval`: The interval in seconds after which the keystrokes are saved to the file. (Default = 60 ie. 1 minute)


### 4. POST Request
To send the logs to a server.

`url`: This is the URL of the server to which you want to send the logs.

`confirmation`: Whether to receive POST confirmation or not. It returns true if server responds with status 200, otherwise false. (Default = False ie. Don't return confirmation).


## Running the Script
```bash
python3 main.py
```