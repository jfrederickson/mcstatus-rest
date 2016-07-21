import json, configparser
from mcstatus import MinecraftServer
from flask import Flask
app = Flask(__name__)

def _init():
    config = configparser.ConfigParser()
    config.read("config.ini")
    hostname = config['DEFAULT']['server']

    server = MinecraftServer.lookup(hostname)
    return server

@app.route("/players")
def players():
    server = _init()
    query = server.query()
    return json.dumps(query.players.names)

@app.route("/status")
def status():
    server = _init()
    query = server.query()
    ret = {
        "players": query.players.names,
        "online": query.players.online,
        "max": query.players.max
    }
    return json.dumps(ret)

if __name__ == "__main__":
    app.run()
