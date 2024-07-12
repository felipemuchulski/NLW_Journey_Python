from flask import jsonify, Blueprint , request# Ajuda a dar um nome para as rotas e sabermos o que elas são


trips_routes_bp = Blueprint("trip_routes", __name__);

# importação de controllers
from src.controllers.trip_creator import TripCreator
from src.controllers.trip_finder import TripFinder

# Importação de repositorios
from src.models.repositories.trips_repository import TripsRepository
from src.models.repositories.emails_to_invite_repository import EmailsToInviteRepository

# Importando o gerente de Conexões
from src.models.settings.db_connection_handler import db_connection_handler


@trips_routes_bp.route("/trips", methods=["POST"])
def create_trip():
    conn = db_connection_handler.get_connection();
    trips_repository = TripsRepository(conn)
    emails_repository = EmailsToInviteRepository(conn);
    controller = TripCreator(trips_repository, emails_repository)

    response = controller.create(request.json)

    return jsonify(response["body"]), response["status_code"];

@trips_routes_bp.route("/trips/<tripId>", methods=["GET"])
def find_trip(tripId):
    conn = db_connection_handler.get_connection();
    trips_repository = TripsRepository(conn);
    controller = TripFinder(trips_repository);

    response = controller.find_trip_details(tripId);

    return jsonify(response["body"]), response["status_code"]