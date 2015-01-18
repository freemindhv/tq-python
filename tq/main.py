from lib.query import FeaturedStream, TopGames, SearchGames, BookMarks
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

    if args.bookmark:
        streams.append(BookMarks(args.bookmark))

    for stream in streams:
        stream.get_results()
