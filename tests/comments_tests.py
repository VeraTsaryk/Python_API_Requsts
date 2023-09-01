import requests
from configuration import API_URL
from constants.routes import COMMENTS_URL
from models.comment_model import CommentModel
from models.json_body_model import Post_body_comment_test,Put_body_comment_test
from models.short_model import ShortModel
from models.responce_model import Responce
from constants.errors import FALSEANSWERJSON




def test_get_list():
    new_object = requests.get(API_URL + COMMENTS_URL)
    responce = Responce(new_object)
    responce.check_status_code(200)
    responce.validate(CommentModel)


def test_get_by_id():
    new_object = requests.get(url=API_URL + COMMENTS_URL + "/2")
    responce = Responce(new_object)
    responce.check_status_code(200)
    responce.validate(CommentModel)


def test_post():
    new_object = requests.post(url=API_URL + COMMENTS_URL, json=Post_body_comment_test)
    responce = Responce(new_object)
    responce.check_status_code(201)
    responce.validate(ShortModel)


def test_put():
    new_object = requests.put(url=API_URL + COMMENTS_URL + "/2", json=Put_body_comment_test)
    responce = Responce(new_object)
    responce.check_status_code(200)
    responce.validate(ShortModel)


def test_delete():
    new_object = requests.delete(url=API_URL + COMMENTS_URL + "/1")
    responce = Responce(new_object)
    responce.check_status_code(200)
    assert responce.responce_value == {}, FALSEANSWERJSON
