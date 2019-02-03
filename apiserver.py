from flask import Flask, request
from api import proxyapi
from model import Proxy
app = Flask(__name__)

@app.route("/proxy/addlist", methods = ["POST"])
def addlist():
    proxyliststr = request.form["proxys"]
    proxys = proxyliststr.split(",")
    for proxy in proxys:
        proxy = proxy.split(":")
        if len(proxy) == 2:
            proxyapi.add(Proxy(ip = proxy[0], port = proxy[1]))

    return ""



def run():        
    app.run(host = "0.0.0.0")
