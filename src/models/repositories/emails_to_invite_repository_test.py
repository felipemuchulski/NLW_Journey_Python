import pytest
import uuid
from src.models.settings.db_connection_handler import db_connection_handler
from .emails_to_invite_repository import EmailsToInviteRepository

db_connection_handler.connect();
trip_id = str(uuid.uuid4)

@pytest.mark.skip(reason='interação com o banco')
def test_registry_email():
    conn = db_connection_handler.get_connection();
    emails_to_invite_repository = EmailsToInviteRepository(conn)

    email_trips_info = {
        "id_invite": str(uuid.uuid4()),
        "trip_id": trip_id,
        "email": "olaMundo@gmail.com"
    }

    emails_to_invite_repository.registry_email(email_trips_info)

@pytest.mark.skip(reason='interação com o banco')
def teste_find_email_to_invite():
    conn = db_connection_handler.get_connection();
    emails_to_invite_repository = EmailsToInviteRepository(conn)

    emails = emails_to_invite_repository.find_email_from_trip(trip_id)
    print()
    print(emails)