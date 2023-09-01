from constants.errors import INAPPROPRIATESTATUSCODE


class Responce:
    def __init__(self, responce):
        self.responce = responce
        self.status_code = responce.status_code
        self.responce_value = responce.json()

    def validate(self, schema):
        if isinstance(self.responce_value, list):
            for item in self.responce_value:
                schema.parse_obj(item)
        else:
            schema.parse_obj(self.responce_value)

    def check_status_code(self, status_code):
        assert self.status_code == status_code, INAPPROPRIATESTATUSCODE
