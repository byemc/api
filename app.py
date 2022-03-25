from flask import Flask, request, jsonify
import json
import byeserver
import time
from mcstatus import MinecraftServer
import socket
import parsetheJSON
app = Flask(__name__)

def getServerInfo():
    # You can pass the same address you'd enter into the address field in minecraft into the 'lookup' function
    # If you know the host and port, you may skip this and use MinecraftServer("example.org", 1234)
    server = MinecraftServer.lookup("mc.byecorps.com")

    try:
        status = server.status()
        latency = server.ping()
        query = server.query()
    except socket.timeout:
        return (None, None, None, server)
    
    return (status, latency, query, server)

def simpleHTMLRedirect(url):
    return "<html><head><meta http-equiv=\"refresh\" content=\"0; url=" + url + "\"></head></html>"

@app.route('/')
def showInfo():
    
    info = getServerInfo()
    status = info[0]
    latency = info[1]
    query = info[2]
    server = info[3]
    if status is None:
        return jsonify({"error": "Server is probably offline"}, status=503), 503

    serverinfo = byeserver.toDir(status, server, query)
    return jsonify(serverinfo)

@app.route("/humanreadable")
def showHumanReadable():
    response = showInfo()
    return parsetheJSON.produceDebugString(response)

# Anywhere in the /docs/ directory, including the root, will redirect to the documentation
@app.route("/docs/<path:path>")
def redirectToDocs(path):
    return simpleHTMLRedirect("https://byecorps.com/byes-server/docs/" + path)

@app.route("/player/<username>")
def isPlayerOnline(username):
    '''Checks if the username, which should not be case sensitive, is online'''
    info = getServerInfo()
    query = info[2]
    if info[0] is None:
        return jsonify({"error": "Server is probably offline"}, status=503), 503
        
    players = byeserver.getPlayers(query)
    if username.lower() in [player.lower() for player in players]:
        return jsonify({"online": True})
    else:
        return jsonify({"online": False})
    
@app.route("/status/json")
def serverUpDown():
    info = getServerInfo()
    if info[0] is None:
        return jsonify({"online": False})
    else:
        return jsonify({"online": True})

@app.route("/status/")
def serverStatusRedirect():
    return simpleHTMLRedirect("https://status.byecorps.com/")

@app.errorhandler(404)
def page_not_found(e):
    return jsonify({"error": "The page you requested was not found.", "code": 404}), 404

if __name__ == '__main__':
    app.run()