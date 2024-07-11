from flask import jsonify, Blueprint # Ajuda a dar um nome para as rotas e sabermos o que elas são


trips_routes_bp = Blueprint("trip_routes", __name__);

@trips_routes_bp.route("/trips", methods=["POST"])
def create_trip():
    return jsonify({"Ola" : "mundo"}), 200;