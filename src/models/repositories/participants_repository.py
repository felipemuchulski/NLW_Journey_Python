from sqlite3 import Connection
from typing import Dict, List, Tuple

class ParticipantsRepository:
    def __init__(self, conn: Connection) -> None:
        self.__conn__ = conn;

    def registry_participant(self, participant_infos: Dict) -> None:
        cursor = self.__conn.cursor();
        cursor.execute(
            '''
            INSERT INTO participant (id, trip_id, emails_to_invite_id, name) 
            VALUES (?, ?, ?, ?)
            ''', (
                participant_infos["id"],
                participant_infos["trip_id"],
                participant_infos["emails_to_invite_id"],
                participant_infos["name"]
            )
        )
        self.__conn__.commit()
    def find_participants_from_trip(self, trip_id: str) -> List[Tuple]: