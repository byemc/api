from flask import Flask
import json
import byeserver
app = Flask(__name__)


@app.route('/')
def showAsJson():
    jsonThing = byeserver.toDir()
    return json.dumps(jsonThing)
    

if __name__ == '__main__':
    app.run()