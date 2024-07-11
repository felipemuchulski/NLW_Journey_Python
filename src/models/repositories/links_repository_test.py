import pytest
import uuid
from src.models.settings.db_connection_handler import db_connection_handler
from .links_repository import LinksRepository

db_connection_handler.connect();
trip_id = str(uuid.uuid4())
link_id = str(uuid.uuid4())

@pytest.mark.skip(reason='interação com o banco')
def test_registry_link():
    conn = db_connection_handler.get_connection();
    links_repository = LinksRepository(conn)

    link_info = {
        "id": link_id,
        "trip_id": trip_id,
        "link": "youtube.com",
        "title": "Youtube"
    }

    links_repository.registry_link(link_info)

@pytest.mark.skip(reason='interação com o banco')
def teste_find_link_from_trip():
    conn = db_connection_handler.get_connection();
    links_repository = LinksRepository(conn)

    response = links_repository.find_link_from_trip(trip_id)
    print()
    print(response)

    assert isinstance(response, list);
    assert isinstance(response[0], tuple);