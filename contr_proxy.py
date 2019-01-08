
from mitmproxy import ctx
from mitmproxy.http import HTTPResponse
from mitmproxy.net.http import Headers

from io import StringIO
import subprocess

class Proxy:
    def __init__(self):
        self.num = 0
        self.test_endpoint_host = "www.google.com"
        self.test_endpoint = f"http://{self.test_endpoint_host}"
        self.stdout = open("test", "w+")

    def sendrequest(self):
        self.pid = subprocess.Popen(["python", "send_request.py", f"{self.test_endpoint}"], stdout=self.stdout)

    def response(self, flow):
        if flow.request.host == self.test_endpoint_host:
            flow.response.content = bytes("ok", "utf-8")
            ctx.master.shutdown()

    def running(self):
        self.sendrequest()

    def get_test_output(self):
        self.stdout.flush()
        self.stdout.seek(0)
        output = self.stdout.readline()
        self.stdout.close()
        self.pid.kill()

        import os
        os.remove("test")

        return output

addons = [
    Proxy()
]