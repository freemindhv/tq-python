import urllib.request
import json


class StreamHandler:
    def __init__(self, limit):
        self.url = None
        self.limit = limit

    def get_stream(self):
        raise Warning("StreamHandler has no get_stream function")

    def get_json(self):
        req = urllib.request.Request(self.url)
        req.add_header("Accept", "application/vnd.twitchtv.v2")
        response = urllib.request.urlopen(req).read()
        content = json.loads(response.decode('utf8'))
        return content

    def get_url(self, x):
        querys = {"featured": "https://api.twitch.tv/kraken/streams/featured",
                  "top": "https://api.twitch.tv/kraken/games/top",
                  "search_games":
                      "https://api.twitch.tv/kraken/search/streams?q="
                  }
        apistring = querys[x] + "?limit=" + str(self.limit)
        return apistring


class FeaturedStream(StreamHandler):
    def get_stream(self):
        self.url = self.get_url("featured")
        content = self.get_json()
        for c in content["featured"]:
            name = c["stream"]["channel"]["name"]
            url = c["stream"]["channel"]["url"]
            print("Channel: {:<20}{}".format(name, url))


class TopGames(StreamHandler):
    def get_stream(self):
        self.url = self.get_url("top")
        content = self.get_json()
        for c in content["top"]:
            print("{:<40} Viewers:{}".format(c["game"]["name"], c["viewers"]))


class SearchGames(StreamHandler):
    def get_stream(self):
        self.url = self.get_url("search_games")
        content = self.get_json()
        for c in content["streams"]:
            name = c["channel"]["name"]
            url = c["channel"]["url"]
            print("{:<20}{}".format(name, url))