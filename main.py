from Publisher.Publisher import Publisher
import sys
import os


def main():
    # print command line arguments
    adcp_key = "2ElNZmQ7DTWWfr1OKqkf4OdI26R_2u7tjCrPNNdx6yfU3Nhrr"
    das_key = "2EfZ5ribW1zR3kE37vMZ1bM8nXo_4KsCxoXoknrjszs2wAHUX"
    args = sys.argv
    for arg in args:
        if arg == 'das':
            p = Publisher(das_key)
            for tunnel in p.tunnels:
                print(tunnel['public_url'])
        elif arg == 'adcp':
            p = Publisher(adcp_key)
            for tunnel in p.tunnels:
                print(tunnel['public_url'])


if __name__ == "__main__":
    main()
