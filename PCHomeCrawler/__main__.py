import sys
from PCHomeCrawler.crawler import *

def main(args=None):
    """The main routine."""
    if args is None:
        args = sys.argv[1:]

    PCHomeCrawler(args)

    # Do argument parsing here (eg. with argparse) and anything else
    # you want your project to do.

if __name__ == "__main__":
    main()