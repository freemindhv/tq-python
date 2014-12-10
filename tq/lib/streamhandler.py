import urllib.request
import json


class StreamHandler:
    def __init__(self):
        self.url = None

    def get_stream(self):
        print("not implemented yet")

    def get_json(self):
        req = urllib.request.Request(self.url)
        req.add_header("Accept", "application/vnd.twitchtv.v2")
        response = urllib.request.urlopen(req).read()
        content = json.loads(response.decode('utf8'))
        return content


class FeaturedStream(StreamHandler):
    def __init__(self):
        self.url = "https://api.twitch.tv/kraken/streams/featured"

    def get_stream(self):
        content = self.get_json()
        for c in content["featured"]:
            name = c["stream"]["channel"]["name"]
            url = c["stream"]["channel"]["url"]
            print("Channel: {:<20}{}".format(name, url))


class TopGames(StreamHandler):
    def __init__(self):
        self.url = "https://api.twitch.tv/kraken/games/top"

    def get_stream(self):
        content = self.get_json()
        for c in content["top"]:
            print("{:<40} Viewers:{}".format(c["game"]["name"], c["viewers"]))


class SearchGames(StreamHandler):
    def __init__(self, query):
        self.url = "https://api.twitch.tv/kraken/search/streams?q={}".format(
            query)

    def get_stream(self):
        content = self.get_json()
        for c in content["streams"]:
            name = c["channel"]["name"]
            url = c["channel"]["url"]
            print("{:<20}{}".format(name, url))