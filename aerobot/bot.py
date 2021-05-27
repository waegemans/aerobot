import requests

class Bot:
    def __init__(self, token, url) -> None:
        self.api_url = url+token+"/"
        self.last_msg_update_id = 0
    
    def getMessages(self, msg_callback) -> None:
        query_url = self.api_url + 'getUpdates'
        r = requests.get(query_url, {'offset': self.last_msg_update_id+1, 'allowed_updates': ['message']})
        data = r.json()

        for ri in data['result']:
            self.last_msg_update_id = max(self.last_msg_update_id, ri['update_id'])
            if 'message' not in ri.keys():
                continue
            
            print(data)
            sender_id, msg = ri['message']['from']['id'], ri['message']['text']
            rdata = {'chat_id': sender_id,
                    'text': msg_callback(msg)}
            requests.post(self.api_url + 'sendMessage', data=rdata)