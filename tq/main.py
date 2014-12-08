import argparse
import sys
import urllib.request
import json


apiversion = 2
apiurl = "https://api.twitch.tv/kraken"


class StreamURL(object):
    def __init__(self):
        self.apiurl = "https://api.twitch.tv/kraken"

    def build_url(self, option):
        options = {"featured": "/streams/featured",
                   "top": "/games/top",
                   "search": "/search/streams?q="
        }
        return self.apiurl + options[option]


def get_data(url):
    req = urllib.request.Request(url)
    req.add_header('Accept', 'application/vnd.twitchtv.v{}+json'.format(
        apiversion))
    response = urllib.request.urlopen(req).read()
    content = json.loads(response.decode('utf8'))
    return content


def handle_featured(url):
    content = get_data(url)
    for c in content["featured"]:
        name = c["stream"]["channel"]["name"]
        url = c["stream"]["channel"]["url"]
        print("Channel: {:<20}{}".format(name, url))


def get_games(url):
    content = get_data(url)
    for c in content["top"]:
        print("{:<40} Viewers:{}".format(c["game"]["name"], c["viewers"]))


def get_streams(url):
    content = get_data(url)
    for c in content["streams"]:
        print("{}".format(c))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='tq')
    mainarguments = parser.add_argument_group("Main Arguments")
    mainarguments.add_argument("-f", "--featured",
                               help="Get a list of featured streams",
                               action="store_true")
    mainarguments.add_argument("-t", "--top",
                               help="Get games by number of viewers",
                               action="store_true")
    mainarguments.add_argument("-v", "--version",
                               action="version",
                               version="%(prog)s alpha version v0.1")
    mainarguments.add_argument("-s", "--streams",
                               help="Find Sreams of <GAME>")
    optionarguments = parser.add_argument_group("Option Arguments")
    optionarguments.add_argument("--limit",
                                 type=int,
                                 default=25,
                                 help="limit query to <limit> results")
    args = parser.parse_args()

    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)

    s = StreamURL()
    urls = []

    if args.featured:
        urls.append(s.build_url("featured"))
    if args.top:
        urls.append(s.build_url("top"))
    if args.streams:
        urls.append(s.build_url("search") + args.streams)

    print(urls)
