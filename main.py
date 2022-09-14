from Publisher.Publisher import Publisher
import sys
import os


def main():
    # print command line arguments
    adcp_key = "2ElNZmQ7DTWWfr1OKqkf4OdI26R_2u7tjCrPNNdx6yfU3Nhrr"
    das_key = "2EfZ5ribW1zR3kE37vMZ1bM8nXo_4KsCxoXoknrjszs2wAHUX"
    p = Publisher("2EfZ5ribW1zR3kE37vMZ1bM8nXo_4KsCxoXoknrjszs2wAHUX")
    print(str(p.host) + " " + str(p.port))
    args = sys.argv
    for arg in args:
        if arg == 'das':
            p = Publisher(das_key)
            print(f"ssh root@{p.host} -p {p.port}")
        elif arg == 'adcp':
            p = Publisher(adcp_key)



if __name__ == "__main__":
    main()
