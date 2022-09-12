from Publisher.Publisher import Publisher
import sys


def main():
    # print command line arguments
    p = Publisher("2EfZ5ribW1zR3kE37vMZ1bM8nXo_4KsCxoXoknrjszs2wAHUX")
    args = sys.argv
    if args[1] == 'host':
        return p.host

    if args[1] == 'port':
        return p.port
    print("Please provide a suitable arguemnt (host | port)")


if __name__ == "__main__":
    print(main())
