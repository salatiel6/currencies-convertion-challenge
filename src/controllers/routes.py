from server import server
from git import Repo
from flask import request

app, api = server.app, server.api


@app.route("/home")
def home():
    return f"Grupo SBF Challenge API - {api.version}", 200


@app.route("/deploy", methods=["POST"])
def deploy():
    if request.method == "POST":
        repo = Repo("./gabriel-salatiel-eng-gruposbf-backend-python")

        origin = repo.remotes.origin
        origin.pull()

        return "Updated PythonAnywhere successfully", 200

    return "Wrong event type", 400
