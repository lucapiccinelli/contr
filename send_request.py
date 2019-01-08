import requests
import sys
from sys import argv

if __name__ == "__main__":
   print(requests.get(argv[1]).text)