import json

from flask import Flask, escape, request, render_template, jsonify, Response
from fritzconnection.lib.fritzcall import FritzCall

app = Flask(__name__, template_folder='src')


@app.route('/fritz/box/calls', methods=['POST'])
def get_all_calls():
    data = request.get_json()
    password = data['password']
    if password != 'fx8320xtred':
        return 'Unauthorized. Nice try'
    fc = FritzCall(address='192.168.178.1', password='9c8-b78-ghu-386')
    calls = fc.get_calls()
    callsString = []
    for call in calls:
        callsString.append(str(call))
        #print(string)
    name = request.args.get("name", "World")
    return Response(json.dumps(callsString),  mimetype='application/json')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=1337, debug=True)
