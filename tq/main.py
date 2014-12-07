import argparse
import sys
import urllib.request
import json

""" crap
Class Stream(object):
    def __init__(self):
        pass

    def _geturl(self, url):
        self.response = urllib.request.urlopen(url)
        return self.response.read()

    def _getjson(self, url):
        self.json = json.loads(self._geturl(url).decode('utf8'))
        for results in self.json["featured"]:
            return results["stream"]["channel"]["url"]

    def getstream(self, url):
        print(json.dumps(self._getjson(url), indent=4))
"""


def get_featured(url):
    response = urllib.request.urlopen(url).read()
    streams = json.loads(response.decode('utf8'))
    for stream in streams["featured"]:
        print(stream["stream"]["channel"]["name"],
              stream["stream"]["channel"]["url"])


if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='tq')
    parser.add_argument("-f", "--featured",
                        help="Get a list of featured streams",
                        action="store_true")
    parser.add_argument("-g", "--games",
                        help="Get games by number of viewers",
                        action="store_true")
    parser.add_argument("-v", "--version",
                        action="version",
                        version="%(prog)s alpha version v0.1")
    parser.add_argument("--game",
                        help="Find games")
    args = parser.parse_args()

    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)

    if args.featured:
        get_featured("https://api.twitch.tv/kraken/streams/featured")
