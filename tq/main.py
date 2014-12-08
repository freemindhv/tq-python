import argparse
import sys
import urllib.request
import json


def get_featured(url):
    response = urllib.request.urlopen(url).read()
    streams = json.loads(response.decode('utf8'))
    for stream in streams["featured"]:
        print("Channel: {:<20}{}".format(stream["stream"]["channel"]["name"],
              stream["stream"]["channel"]["url"]))

def get_games(url):
    response = urllib.request.urlopen(url).read()
    streams = json.loads(response.decode('utf8'))
    for stream in streams["top"]:
        print("{}".format(stream))


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
    if args.games:
        get_games("https://api.twitch.tv/kraken/games/top")
