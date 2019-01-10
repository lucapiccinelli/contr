import requests
import sys
from sys import argv

if __name__ == "__main__":
    # proxies = {
    #     "http": "http://127.0.0.1:8080",
    #     "https": "http://127.0.0.1:8080",
    # }

    # print(requests.get(argv[1], verify=False, proxies=proxies).text,)
    print(requests.get(argv[1], verify=False).text,)