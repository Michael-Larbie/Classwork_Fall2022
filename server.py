# server.py

from flask import Flask
import request
import json

app = Flask(__name__)


@app.route("/", methods=["GET"])
def server_status():
    return "Server is on."


@app.route("/info", methods=["GET"])
def informaiton():
    x = "This website will calculate blood cholesterol levels."
    x += "It is writted by David Ward."
    return x


@app.route("/hdl_check", methods=["POST"])
def hdl_check_from_internet():
    """

        incoming_json = {"name": <name_str>,
                         "hdl_value": <hdl_value_int}
    """
    from blood_calcualateor import check_HDL
    in_data = request.get_json()
    hdl_value = in_data["hdl_value"]
    print("The recieved value was {}".format(hdl_value))
    answer = check_HDL(hdl_value)
    return answer


@app.route("/add_numbers", methods=["POST"])
def add_numbesr():
    in_data = request.get_json()
    answer = in_data["a"] + in_data["b"]
    answer jsonify(answer)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
