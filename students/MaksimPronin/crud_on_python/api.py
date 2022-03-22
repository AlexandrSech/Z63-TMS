from flask import Flask, request
from server import Server
import json


app = Flask(__name__)


@app.route("/data", methods=['GET'])
def list_data():
    all_records = server.get_list_of_records()
    response = json.dumps(all_records)
    return response


@app.route("/data/<int:id>", methods=['GET'])  #TODO
def retrieve_data(id):
    pass


@app.route("/data", methods=['POST'])
def create_data():
    new_record = server.create_record(request.data)
    response = json.dumps(new_record)
    return response


@app.route("/data/<int:id>", methods=['PUT'])   #TODO
def update_data(id):
    pass


@app.route("/data/<int:id>", methods=['DELETE'])   #TODO
def delete_data(id):
    pass


if __name__ == "__main__":
    server = Server()
    app.run(debug=True)
