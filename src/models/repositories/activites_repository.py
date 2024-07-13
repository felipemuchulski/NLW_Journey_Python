from typing import Dict, Tuple, List
from sqlite3 import Connection

class ActiviesRepository:
    def __init__(self, conn: Connection) -> None:
        self.__conn = conn
    
    def registry_activivty(self, acitivity_infos: Dict) -> None:
        cursor = self.__conn.cursor();
        cursor.execute(
            '''
                INSERT INTO activities (
                 id, trip_id, title, occurs_at)
                VALUES(?, ?, ?, ?)

            ''', (
                acitivity_infos["id"],
                acitivity_infos["trip_id"],
                acitivity_infos["title"],
                acitivity_infos["occurs_at"]
            )
        )
        self.__conn.commit();

    ## Buscar exemplos no banco de dados
    def find_activies_trip(self, trip_id: str) -> list[Tuple]:
        cursor = self.__conn.cursor();
        cursor.execute(
        ''' SELECT * FROM activities WHERE trip_id = ?''', (trip_id,)
        )
        activities = cursor.fetchall()
        return activities
    
   