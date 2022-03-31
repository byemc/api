from flask import Flask, request, jsonify
import json
import server as mcs
import time
from mcstatus import MinecraftServer
import socket
from git import Repo

app = Flask(__name__)
repo = Repo(".")

def simpleHTMLRedirect(url):
    return "<html><head><meta http-equiv=\"refresh\" content=\"0; url=" + url + "\"></head></html>"

# This first one is for servers that use TCP to redirect requests by Minecraft to the domain to the server's IP.
@app.route('/mcserver/<server>', methods=['GET'])
def serverTCPNoPort(server):
    # creates a server object
    server = MinecraftServer.lookup(f"{server}:25565")

    serverInfo = mcs.returnMCInfo(server)

    if "code" in serverInfo:
        code = serverInfo["code"]
    else:
        code = 200

    return jsonify(serverInfo), code

# misc
@app.route("/")
def index():
    # Redirects to the website.
    return simpleHTMLRedirect("https://byecorps.com/api")


@app.route("/info")
def apiInfo():
    # Returns a JSON object with the git commit hash, and date of the commit

    # Get the short commit hash
    commitShortHash = repo.head.commit.hexsha[:7]
    
    # Get the commit time
    commitDate = repo.head.commit.authored_datetime

    return jsonify({"verison": f"{commitShortHash}", "committed": f"{commitDate}"})

@app.route("/status/")
def serverStatusRedirect():
    return simpleHTMLRedirect("https://status.byecorps.com/")

@app.errorhandler(404)
def page_not_found(e):
    return jsonify({"error": "The page you requested was not found.", "code": 404}), 404

if __name__ == '__main__':
    app.run()