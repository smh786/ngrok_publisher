from Publisher.Publisher import Publisher
import sys
import os

def main():
    # print command line arguments
    p = Publisher("2EfZ5ribW1zR3kE37vMZ1bM8nXo_4KsCxoXoknrjszs2wAHUX")
    print(str(p.host) + " " + str(p.port))
    args = sys.argv
    for arg in args:
        if arg == '-C':
            print(f"ssh root@{p.host} -p {p.port}")


if __name__ == "__main__":
    main()
