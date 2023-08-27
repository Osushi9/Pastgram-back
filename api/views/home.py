from flask import Blueprint, jsonify
from flask_login import login_required

home = Blueprint("home", __name__)


@home.route("/", methods=["GET"])
@login_required
def index():
    return jsonify({"message": "Hello World!"}), 200
