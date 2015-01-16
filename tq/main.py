from lib.query import FeaturedStream, TopGames, SearchGames, DebugPrint
from lib.argparser import parser


if __name__ == '__main__':
    args = parser.parse_args()
    streams = []

    if args.featured:
        streams.append(FeaturedStream(args.limit))

    if args.top:
        streams.append(TopGames(args.limit))

    if args.streams:
        streams.append(SearchGames(args.streams, args.limit))

    if args.debug:
        streams.append(DebugPrint(args.debug))

    for stream in streams:
        stream.get_results()
