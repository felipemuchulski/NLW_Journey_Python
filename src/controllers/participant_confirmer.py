from typing import Dict

class ParticipantConfirmer:
    def __init__(self, partipants_repository) -> None:
        self.__partipants_repository = partipants_repository

    def confirm(self, trip_id) -> Dict:
        try:
            self.__partipants_repository.update_participant_status(trip_id)
            return {"body": None, "status_code": 204}

        except Exception as exception:
            return {
                "body": {"error": "Bad request", "message": str(exception)},
                "status_code": 400
            }
