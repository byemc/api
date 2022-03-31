from mcstatus import MinecraftServer
import json

def returnMCInfo(server):
    try:
        # 'status' is supported by all Minecraft servers that are version 1.7 or higher.
        status = server.status()
        print(f"The server has {status.players.online} players and replied in {status.latency} ms")

        try:
            # 'query' has to be enabled in a servers' server.properties file!
            # It may give more information than a ping, such as a full player list or mod information.
            query = server.query()
            print(f"The server has the following players online: {', '.join(query.players.names)}")
            
            serverInfo = {
                "status": {
                    "players": {
                        "online": status.players.online,
                        "max": status.players.max
                    },
                    "latency": status.latency
                },
                "query": {
                    "players": {
                        "names": query.players.names,
                        "list": query.players.list
                    }
                }
            }
        except:
            serverInfo = {
                "status": {
                    "players": {
                        "online": status.players.online,
                        "max": status.players.max
                    },
                    "latency": status.latency
                },
                "query": {
                    "players": {
                        "names": "The server doesn't allow querying.",
                        "list": ["NoQuery"]
                    }
                },
                "error": "The server doesn't allow querying, or something has gone wrong with the query."
            }
    except:
        serverInfo = {"error": "The server may be offline.", "code": 503}
        return serverInfo
    

    return serverInfo


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