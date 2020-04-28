import requests
import json
import configparser as cfg

class Telegram_Bot():
    def __init__ (self, config):
        self.token = self.read_from_config_file(config)
        self.base = 'https://api.telegram.org/bot{}/'.format(self.token)

    def getUpdates(self, offset=None):
        url = self.base + 'getUpdates?timeout=100'
        if offset:
            url = url + '&offset={}'.format(offset + 1)
        r = requests.get(url)
        return json.loads(r.content)

    def sendMessage(self, message, chat_id):
        url = self.base + 'sendMessage?chat_id={}&text={}'.format(chat_id, message)
        if message is not None:
            requests.get(url)

    def read_from_config_file(self, config):
        parser = cfg.ConfigParser()
        parser.read(config)
        return parser.get('creds', 'token')