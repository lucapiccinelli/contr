import typing
import requests
import mitmproxy
from mitmproxy.tools.main import mitmweb
from sys import argv
from threading import Thread
import time
from mitmproxy import ctx

def main(argv: typing.List) -> str:
    mitmweb(["-s", "contr_proxy.py", "--no-web-open-browser"])

    master = ctx.master
    proxy_addon = master.addons.get("proxy")

    return proxy_addon.get_test_output()


if __name__ == '__main__':
    main(argv[1:])
