from lib.streamhandler import FeaturedStream, TopGames, SearchGames
from lib.argparser import parser


if __name__ == '__main__':
    args = parser.parse_args()
    streams = []

    if args.featured:
        streams.append(FeaturedStream())

    if args.top:
        streams.append(TopGames())

    if args.streams:
        streams.append(SearchGames(args.streams))

    for stream in streams:
        stream.get_stream()
