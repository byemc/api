import json

def produceDebugString(response):
    if type(response) is dict:
        print()
    else:
        response = json.loads(response)

    formatted = f'''Status
    \tOnline:\t{response["status"]["online"]}\n
    \tDescription:\t{response["status"]["desc"]}\n
    \tVersion:\t{response["status"]["version"]}\n
    \tProtocol:\t{response["status"]["protocol"]}\n
    \tPlayers\n
    \t\tMax:\t{response["status"]["players"]["max"]}\n
    \t\tOnline:\t{response["status"]["players"]["online"]}\n
    \tLatency:\t{response["status"]["latency"]}\n
    \n
    Query\n
    \tPlayers\n
    \t\tNames:\t{response["query"]["players"]["names"]}\n'''

    formatted = formatted.replace("\n", "<br>")

    return formatted
