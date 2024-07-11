from typing import Dict, Tuple, List
from sqlite3 import Connection

class EmailsToInviteRepository:
    def __init__(self, conn: Connection) -> None:
        self.__conn = conn
    
    def registry_email(self, emails_infos: Dict) -> None:
        cursor = self.__conn.cursor();
        cursor.execute(
            '''
                INSERT INTO emails_to_invite (
                 id_invite, trip_id, email)
                VALUES(?, ?, ?)

            ''', (
                emails_infos["id_invite"],
                emails_infos["trip_id"],
                emails_infos["email"]
            )
        )
        self.__conn.commit();

    ## Buscar exemplos no banco de dados
    def find_email_from_trip(self, trip_id: str) -> list[Tuple]:
        cursor = self.__conn.cursor();
        cursor.execute(
        ''' SELECT * FROM emails_to_invite WHERE trip_id = ?''', (trip_id,)
        )
        emails = cursor.fetchall()
        return emails
    
   