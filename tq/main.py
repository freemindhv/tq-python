import argparse
import urllib.request
import json


class Stream(object):
    def __init__(self):
        pass

    def _geturl(self, url):
        self.response = urllib.request.urlopen(url)
        return self.response.read()

    def _getjson(self, url):
        self.json = json.loads(self._geturl(url).decode('utf8'))
        return self.json

    def getstream(self, url):
        print(self._getjson(url))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.parse_args()
    url = "https://api.twitch.tv/kraken/streams/featured"
    x = Stream()
    x.getstream(url)