import sys
import argparse

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
mainarguments.add_argument("-b", "--bookmark",
                           help="Bookmark a stream")
mainarguments.add_argument("-D", "--debug",
                           help="Print the argparse input")
optionarguments = parser.add_argument_group("Option Arguments")
optionarguments.add_argument("--limit",
                             type=int,
                             default=25,
                             help="limit query to <limit> results")
if len(sys.argv) == 1:
    parser.print_help()
    sys.exit(1)