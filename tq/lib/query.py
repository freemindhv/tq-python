import urllib.request
import json


class Query:
    base_url = "https://api.twitch.tv/kraken/"

    def get_results(self):
        raise AttributeError("StreamHandler has no get_stream function")

    def get_json(self, url):
        req = urllib.request.Request(url)
        req.add_header("Accept", "application/vnd.twitchtv.v2")

        response = urllib.request.urlopen(req).read()

        return json.loads(response.decode('utf8'))


class FeaturedStream(Query):
    def __init__(self, limit):
        self.url = "{}streams/featured?limit={}".format(Query.base_url, limit)

    def get_results(self):
        content = self.get_json(self.url)

        print("[ Featured ]:")

        for c in content["featured"]:
            name = c["stream"]["channel"]["name"]
            url = c["stream"]["channel"]["url"]

            print("   Channel: {:20}{}".format(name, url))


class TopGames(Query):
    def __init__(self, limit):
        self.url = "{}games/top?limit={}".format(Query.base_url, limit)

    def get_results(self):
        content = self.get_json(self.url)

        print("[ Top ]:")

        for c in content["top"]:
            print("   {:40} Viewers:{}".format(c["game"]["name"],
                                               c["viewers"]))


class SearchGames(Query):
    def __init__(self, searchstring, limit):
        self.searchstring = searchstring
        self.url = "{}search/streams?q={}&limit={}".format(Query.base_url,
                                                       self.searchstring, limit)

    def get_results(self):
        content = self.get_json(self.url)

        print("[ Streams tagged with ={}= ]:".format(self.searchstring))

        for c in content["streams"]:
            name = c["channel"]["name"]
            url = c["channel"]["url"]
            print("   {:20}{}".format(name, url))