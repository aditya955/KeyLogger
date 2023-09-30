import requests

class PostToServer:
    def __init__(self, url, data, confirmation=True):
        self.url = url  # URL to post data to
        self.data = data    # Data to post (Preferably JSON)
        self.confirm = confirmation # Confirmation of data being posted

    # This method is used to post data to the server
    # Returns True if Successful, else False
    def post(self):
        try:
            response = requests.post(self.url, data=self.data)
            if(self.confirm):
                if response.status_code == 200:
                    return True
                else:
                    return False
        except:
            if(self.confirm):
                return False