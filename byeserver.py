from mcstatus import MinecraftServer
import json

# You can pass the same address you'd enter into the address field in minecraft into the 'lookup' function
# If you know the host and port, you may skip this and use MinecraftServer("example.org", 1234)
server = MinecraftServer.lookup("mc.byecorps.com")

# Compile it into a dict
status = server.status()
latency = server.ping()
query = server.query()

def getPlayers():
    players = []
    for player in query.players.names:
        players.append(player)
    return players

def toDir():
    serverinfo = {
        "status": {
            "players": {
                "online": status.players.online,
            },
            "latency":  status.latency
        },
        "query": {
            "desc": status.description,
            "version": status.version.name,
            "protocol": status.version.protocol,
            "players": {
                "max": status.players.max,
                "online": status.players.online,
                "names": getPlayers()
            },
            "online": status.players.online
        },
        "latency": server.ping()
    }
    return serverinfo