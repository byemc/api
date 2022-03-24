from mcstatus import MinecraftServer
import json

def getPlayers(query):
    players = []
    for player in query.players.names:
        players.append(player)
    return players

def toDir(status, server, query, playerArray):
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
                "names": playerArray,
            },
            "online": status.players.online
        },
        "latency": server.ping()
    }
    return serverinfo