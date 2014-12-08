import argparse
import sys
import urllib.request
import json


def get_featured(url):
    req = urllib.request.Request(url)
    req.add_header('Accept', 'application/vnd.twitchtv.v2+json')
    response = urllib.request.urlopen(req).read()
    content = json.loads(response.decode('utf8'))
    for c in content["featured"]:
        print("Channel: {:<20}{}".format(c["stream"]["channel"]["name"],
              c["stream"]["channel"]["url"]))


def get_games(url):
    req = urllib.request.Request(url)
    req.add_header('Accept', 'application/vnd.twitchtv.v2+json')
    response = urllib.request.urlopen(req).read()
    content = json.loads(response.decode('utf8'))
    for c in content["top"]:
        print("{}".format(c))


def get_streams(url):
    req = urllib.request.Request(url)
    req.add_header('Accept', 'application/vnd.twitchtv.v2+json')
    response = urllib.request.urlopen(req).read()
    content = json.loads(response.decode('utf8'))
    for c in content["streams"]:
        print("{}".format(c))


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
    parser.add_argument("-s", "--streams",
                        help="Find Sreams of <GAME>")
    args = parser.parse_args()

    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)

    if args.featured:
        get_featured("https://api.twitch.tv/kraken/streams/featured")

    if args.games:
        get_games("https://api.twitch.tv/kraken/games/top")

    if args.streams:
        url = "https://api.twitch.tv/kraken/search/streams?q=" + args.streams
        get_streams(url)
