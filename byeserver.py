from mcstatus import MinecraftServer
import json

def getPlayers(query):
    players = []
    for player in query.players.names:
        players.append(player)
    return players

def toDir(status, server, query):
    serverinfo = {
        "status": {
            "online": status.players.online,
            "desc": status.description,
            "version": status.version.name,
            "protocol": status.version.protocol,
            "players": {
                "max": status.players.max,
                "online": status.players.online,
                
            },
        },
        "query": {
            "players": {
                "names": list(query.players.names),
            },
        },
    }
    return serverinfo