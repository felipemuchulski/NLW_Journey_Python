import pytest
import uuid
from src.models.settings.db_connection_handler import db_connection_handler
from .participants_repository import ParticipantsRepository
db_connection_handler.connect();

trip_id = str(uuid.uuid4());
parti_id = str(uuid.uuid4());
to_invite = str(uuid.uuid4());

@pytest.mark.skip(reason='interação com o banco')
def test_registry_participant():
    conn = db_connection_handler.get_connection();
    participants_repository = ParticipantsRepository(conn)

    participants_info = {
        "id": parti_id,
        "trip_id": trip_id,
        "emails_to_invite_id":to_invite,
        "name": "Felipe Teste"
    }

    participants_repository.registry_participant(participants_info)

@pytest.mark.skip(reason='interação com o banco')
def teste_update_participante_status():
    conn = db_connection_handler.get_connection();
    participants_repository = ParticipantsRepository(conn)
    
    participants_repository.update_participante_status();