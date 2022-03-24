from flask import Flask
import json
import byeserver
import time
from mcstatus import MinecraftServer
app = Flask(__name__)



@app.route('/')
def showInfo():
    # You can pass the same address you'd enter into the address field in minecraft into the 'lookup' function
    # If you know the host and port, you may skip this and use MinecraftServer("example.org", 1234)
    server = MinecraftServer.lookup("mc.byecorps.com")

    # Compile it into a dict
    status = server.status()
    latency = server.ping()
    query = server.query()

    playerArray = byeserver.getPlayers(query)
    serverinfo = byeserver.toDir(status, server, query, playerArray)
    return json.dumps(serverinfo)
    

if __name__ == '__main__':
    app.run()