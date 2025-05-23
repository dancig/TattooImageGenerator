import pytest
from Server import app
from Server import imageGen

@pytest.fixture()
def testapp():
    testapp = app
    yield testapp


@pytest.fixture()
def client(testapp):
    return testapp.test_client()


def test_process_request_1(client):
    imageGen.isBusy = False
    response = client.get("/123")
    assert response.status_code == 404


def test_process_request_2(client):
    imageGen.isBusy = False
    response = client.get("/")
    assert response.status_code == 200
    assert "<h1>Генератор изображений татуировок</h1>" in response.data.decode()


def test_process_request_3(client):
    imageGen.isBusy = False
    response = client.post("/")
    assert response.status_code == 200
    assert "Некорректный ввод." in response.data.decode()


def test_process_request_4(client):
    imageGen.isBusy = False
    response = client.post("/", data={'prompt': ""})
    assert response.status_code == 200
    assert "Некорректный ввод." in response.data.decode()


def test_process_request_5(client):
    imageGen.isBusy = False
    response = client.post("/", data={'prompt': ("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                                                 "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                                                 "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                                                 "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                                                 "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                                                 "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                                                 "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                                                 "aaaaaaaaaaaaaaaaaa")})
    assert response.status_code == 200
    assert "Некорректный ввод." in response.data.decode()


def test_process_request_6(client, testapp):
    imageGen.isBusy = True
    response = client.post("/", data={'prompt': "image"})
    assert response.status_code == 200
    assert "Попробуйте позже." in response.data.decode()


def test_process_request_7(client):
    imageGen.isBusy = False
    response = client.post("/", data={'prompt': "image of a cat"})
    assert response.status_code == 200
    assert "СгенерированноеИзображение" in response.data.decode()


def test_process_request_8(client):
    imageGen.isBusy = False
    response = client.post("/", data={'prompt': "Изображение кота"})
    assert response.status_code == 200
    assert "СгенерированноеИзображение" in response.data.decode()


def test_process_request_9(client):
    imageGen.isBusy = False
    response = client.post("/", data={'prompt': ("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                                                 "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                                                 "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                                                 "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                                                 "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                                                 "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                                                 "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                                                 "aaaaaaaaaaaaaaaaa")})
    assert response.status_code == 200
    assert "СгенерированноеИзображение" in response.data.decode()


def test_process_request_10(client):
    imageGen.isBusy = False
    response = client.post("/", data={'prompt': "Изображение числа 8"})
    assert response.status_code == 200
    assert "СгенерированноеИзображение" in response.data.decode()